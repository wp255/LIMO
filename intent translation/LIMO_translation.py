import os
import re
import json
import pickle
import faiss
import numpy as np
from typing import List, Dict, Any, Optional

from openai import OpenAI
from sentence_transformers import SentenceTransformer


INDEX_PATH = "intent_kb.faiss"
META_PATH = "intent_kb_meta.pkl"
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"

# 这里换成微调模型服务地址
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:8000/v1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "EMPTY")
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "your-finetuned-intent-model")


INTENT_TRANSLATION_SYSTEM_PROMPT = """
You are an expert intent parser for intent-driven 6G RAN management and orchestration.

Your task is to convert a user's natural language service intent into a structured network intent JSON.

You must use the retrieved domain knowledge as the primary reference.
You must not invent unsupported requirements.
If the user does not explicitly provide a QoS value, infer a reasonable default according to the retrieved knowledge and mark it in the explanation.

Output requirements:
1. Output valid JSON only.
2. Do not output Markdown.
3. Do not output any extra text outside JSON.
4. The JSON must follow the required schema.
5. serviceType must be one of: URLLC, eMBB, mMTC.
6. latency must use ms, for example "<10ms".
7. throughput must use Mbps, for example "20Mbps".
8. priority must be a string from "1" to "5".

Required JSON fields:
{
  "serviceType": "",
  "latency": "",
  "throughput": "",
  "reliability": "",
  "priority": "",
  "region": "",
  "time": "",
  "application": "",
  "explanation": ""
}
"""


INTENT_VALIDATION_SYSTEM_PROMPT = """
You are an expert validator for structured network intents in intent-driven 6G RAN management.

You must evaluate whether the structured JSON intent correctly reflects the user's natural language intent.

You need to perform three checks:

1. Format Checking:
- Check whether all required fields exist.
- Check whether field values follow the expected format.
- Check whether serviceType is one of URLLC, eMBB, and mMTC.
- Check whether latency, throughput, reliability, and priority are formatted correctly.

2. Semantic Validation:
- Check whether the structured intent preserves the original meaning of the user's natural language request.
- Check whether the serviceType mapping is semantically correct.
- Check whether QoS values are reasonable for the user request.

3. Consistency Assessment:
- Check whether fields contradict each other.
- For example, URLLC with very high latency is inconsistent.
- eMBB with extremely low throughput is inconsistent.
- mMTC with very high throughput per device is usually inconsistent.

Scoring rules:
- Each dimension starts from 10 points.
- Missing required field: deduct 1 point.
- Type or format mismatch: deduct 5 points.
- Critical semantic mismatch: deduct 10 points.
- Invalid QoS value: deduct 5 points.
- Cross-field logical conflict: deduct 5 points.
- If any score is lower than threshold, the intent is unqualified.

Output valid JSON only. Do not output Markdown.
"""


INTENT_REPAIR_SYSTEM_PROMPT = """
You are an expert repair agent for structured network intents.

Given the original user intent, the retrieved domain knowledge, the previous structured intent JSON, and the validation result, repair the structured intent.

Requirements:
1. Keep the repaired JSON faithful to the original user intent.
2. Use retrieved domain knowledge to fix missing fields, wrong serviceType, unreasonable QoS values, and cross-field conflicts.
3. Output valid JSON only.
4. Do not output Markdown or explanations outside the JSON.
"""


class RAGRetriever:
    def __init__(
        self,
        index_path: str = INDEX_PATH,
        meta_path: str = META_PATH,
        embedding_model: str = EMBEDDING_MODEL
    ):
        self.index = faiss.read_index(index_path)

        with open(meta_path, "rb") as f:
            self.docs = pickle.load(f)

        self.model = SentenceTransformer(embedding_model)

    def retrieve(self, query: str, top_k: int = 4) -> List[Dict[str, Any]]:
        query_emb = self.model.encode(
            [query],
            normalize_embeddings=True
        ).astype("float32")

        scores, indices = self.index.search(query_emb, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue

            item = dict(self.docs[idx])
            item["score"] = float(score)
            results.append(item)

        return results

    @staticmethod
    def format_context(results: List[Dict[str, Any]]) -> str:
        parts = []
        for i, r in enumerate(results, start=1):
            parts.append(
                f"[Retrieved Document {i}]\n"
                f"Source: {r['source']}\n"
                f"Score: {r['score']:.4f}\n"
                f"Content:\n{r['text']}"
            )
        return "\n\n".join(parts)


class FineTunedLLMClient:
    def __init__(
        self,
        base_url: str = LLM_BASE_URL,
        api_key: str = LLM_API_KEY,
        model_name: str = LLM_MODEL_NAME
    ):
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key
        )
        self.model_name = model_name

    def chat(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1024
    ) -> str:
        resp = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        return resp.choices[0].message.content


def build_intent_translation_prompt(user_intent: str, retrieved_context: str) -> str:
    return f"""
Retrieved domain knowledge:
{retrieved_context}

User natural language intent:
{user_intent}

Please convert the user intent into the required structured network intent JSON.
Remember: output JSON only.
"""


def build_validation_prompt(
    user_intent: str,
    structured_intent: Dict[str, Any],
    retrieved_context: str,
    threshold: int = 9
) -> str:
    return f"""
Retrieved domain knowledge:
{retrieved_context}

Original user intent:
{user_intent}

Structured intent JSON:
{json.dumps(structured_intent, ensure_ascii=False, indent=2)}

Threshold:
{threshold}

Please evaluate the structured intent using Format Checking, Semantic Validation, and Consistency Assessment.

Return JSON only in this format:
{{
  "formatChecking": {{
    "score": 10,
    "problems": [],
    "comment": ""
  }},
  "semanticValidation": {{
    "score": 10,
    "problems": [],
    "comment": ""
  }},
  "consistencyAssessment": {{
    "score": 10,
    "problems": [],
    "comment": ""
  }},
  "qualified": true,
  "repairSuggestion": "",
  "finalConclusion": ""
}}
"""


def build_repair_prompt(
    user_intent: str,
    previous_intent: Dict[str, Any],
    validation_result: Dict[str, Any],
    retrieved_context: str
) -> str:
    return f"""
Retrieved domain knowledge:
{retrieved_context}

Original user intent:
{user_intent}

Previous structured intent JSON:
{json.dumps(previous_intent, ensure_ascii=False, indent=2)}

Validation result:
{json.dumps(validation_result, ensure_ascii=False, indent=2)}

Please repair the structured intent JSON.
Output JSON only.
"""


def extract_json(text: str) -> Dict[str, Any]:
    """
    Extract JSON from model output.
    This is not used for rule-based intent parsing.
    It is only used to make the LLM output machine-readable.
    """
    text = text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError(f"No JSON object found in model output:\n{text}")

    return json.loads(match.group(0))


class LIMOIntentRAGPipeline:
    def __init__(
        self,
        retriever: Optional[RAGRetriever] = None,
        llm: Optional[FineTunedLLMClient] = None,
        threshold: int = 9,
        top_k: int = 4
    ):
        self.retriever = retriever or RAGRetriever()
        self.llm = llm or FineTunedLLMClient()
        self.threshold = threshold
        self.top_k = top_k

    def parse_intent(self, user_intent: str) -> Dict[str, Any]:
        retrieved_docs = self.retriever.retrieve(user_intent, top_k=self.top_k)
        retrieved_context = self.retriever.format_context(retrieved_docs)

        prompt = build_intent_translation_prompt(
            user_intent=user_intent,
            retrieved_context=retrieved_context
        )

        raw_output = self.llm.chat(
            system_prompt=INTENT_TRANSLATION_SYSTEM_PROMPT,
            user_prompt=prompt,
            temperature=0.1,
            max_tokens=1024
        )

        structured_intent = extract_json(raw_output)

        return {
            "structuredIntent": structured_intent,
            "retrievedDocs": retrieved_docs,
            "rawModelOutput": raw_output
        }

    def validate_intent(
        self,
        user_intent: str,
        structured_intent: Dict[str, Any],
        retrieved_docs: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        retrieved_context = self.retriever.format_context(retrieved_docs)

        prompt = build_validation_prompt(
            user_intent=user_intent,
            structured_intent=structured_intent,
            retrieved_context=retrieved_context,
            threshold=self.threshold
        )

        raw_output = self.llm.chat(
            system_prompt=INTENT_VALIDATION_SYSTEM_PROMPT,
            user_prompt=prompt,
            temperature=0.0,
            max_tokens=1024
        )

        validation_result = extract_json(raw_output)

        return {
            "validationResult": validation_result,
            "rawValidationOutput": raw_output
        }

    def repair_intent(
        self,
        user_intent: str,
        previous_intent: Dict[str, Any],
        validation_result: Dict[str, Any],
        retrieved_docs: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        retrieved_context = self.retriever.format_context(retrieved_docs)

        prompt = build_repair_prompt(
            user_intent=user_intent,
            previous_intent=previous_intent,
            validation_result=validation_result,
            retrieved_context=retrieved_context
        )

        raw_output = self.llm.chat(
            system_prompt=INTENT_REPAIR_SYSTEM_PROMPT,
            user_prompt=prompt,
            temperature=0.1,
            max_tokens=1024
        )

        repaired_intent = extract_json(raw_output)

        return {
            "repairedIntent": repaired_intent,
            "rawRepairOutput": raw_output
        }

    def run(self, user_intent: str, enable_repair: bool = True) -> Dict[str, Any]:
        parse_result = self.parse_intent(user_intent)

        structured_intent = parse_result["structuredIntent"]
        retrieved_docs = parse_result["retrievedDocs"]

        validation = self.validate_intent(
            user_intent=user_intent,
            structured_intent=structured_intent,
            retrieved_docs=retrieved_docs
        )

        validation_result = validation["validationResult"]

        final_intent = structured_intent
        repair_result = None

        if enable_repair and not validation_result.get("qualified", False):
            repair_result = self.repair_intent(
                user_intent=user_intent,
                previous_intent=structured_intent,
                validation_result=validation_result,
                retrieved_docs=retrieved_docs
            )

            final_intent = repair_result["repairedIntent"]

            second_validation = self.validate_intent(
                user_intent=user_intent,
                structured_intent=final_intent,
                retrieved_docs=retrieved_docs
            )
        else:
            second_validation = validation

        return {
            "userIntent": user_intent,
            "retrievedKnowledge": [
                {
                    "source": d["source"],
                    "chunk_id": d["chunk_id"],
                    "score": d["score"],
                    "text": d["text"]
                }
                for d in retrieved_docs
            ],
            "initialStructuredIntent": structured_intent,
            "initialValidation": validation_result,
            "repairResult": repair_result,
            "finalStructuredIntent": final_intent,
            "finalValidation": second_validation["validationResult"]
        }


if __name__ == "__main__":
    user_intent = (
        "I plan to initiate an important remote video conference in Xi'an on June 20. "
        "The session must remain stable throughout. Please generate an appropriate "
        "network configuration for this service."
    )

    pipeline = LIMOIntentRAGPipeline(
        threshold=9,
        top_k=4
    )

    result = pipeline.run(user_intent, enable_repair=True)

    print(json.dumps(result, ensure_ascii=False, indent=2))