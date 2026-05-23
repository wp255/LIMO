# Expanded RAG Knowledge Base for LIMO-style Intent Translation and Validation

This package is designed for a LIMO-style intent-enabled layer:
1. Retrieve domain knowledge and examples according to the user's natural-language intent.
2. Prompt the fine-tuned LLM to translate the intent into a structured JSON.
3. Retrieve validation rules and negative examples.
4. Prompt the fine-tuned LLM to perform format checking, semantic validation, and consistency assessment.
5. Repair the JSON when validation fails.

Recommended retrieval strategy:
- For intent translation: retrieve from `01`, `02`, `03`, `04`, and `08`.
- For validation: retrieve from `01`, `04`, `05`, `06`, `07`, and `09`.
- For repair: retrieve from `04`, `07`, `09`, and `10`.

Recommended `top_k`:
- Translation: 5-8 chunks.
- Validation: 6-10 chunks.
- Repair: 6-10 chunks.

The contents are written in English because the fine-tuning and validation examples are English-style JSONL records.
