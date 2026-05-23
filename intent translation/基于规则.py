import re
import json
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any, List


@dataclass
class NetworkIntent:
    serviceType: Optional[str] = None       # URLLC / eMBB / mMTC
    latency: Optional[float] = None         # ms
    throughput: Optional[float] = None      # Mbps
    reliability: Optional[float] = None     # %
    priority: Optional[int] = None          # 1 highest, 5 lowest
    region: Optional[str] = None
    time: Optional[str] = None
    rawText: Optional[str] = None

    def to_limo_json(self) -> Dict[str, Any]:
        return {
            "serviceType": self.serviceType,
            "latency": f"<{self.latency:g}ms" if self.latency is not None else None,
            "throughput": f"{self.throughput:g}Mbps" if self.throughput is not None else None,
            "reliability": f"{self.reliability:g}%" if self.reliability is not None else None,
            "priority": str(self.priority) if self.priority is not None else None,
            "region": self.region,
            "time": self.time
        }


class IntentParser:
    """
    A lightweight rule-based intent parser inspired by LIMO.
    It can be replaced or enhanced by a fine-tuned LLM.
    """

    def parse(self, text: str) -> NetworkIntent:
        intent = NetworkIntent(rawText=text)

        intent.serviceType = self._detect_service_type(text)
        intent.latency = self._extract_latency(text)
        intent.throughput = self._extract_throughput(text)
        intent.reliability = self._extract_reliability(text)
        intent.priority = self._extract_priority(text)
        intent.region = self._extract_region(text)
        intent.time = self._extract_time(text)

        self._fill_default_qos(intent)

        return intent

    def _detect_service_type(self, text: str) -> str:
        t = text.lower()

        urllc_keywords = [
            "urllc", "low latency", "ultra reliable", "high reliability",
            "remote surgery", "remote control", "autonomous driving",
            "video conference", "stable", "mission critical",
            "低时延", "高可靠", "稳定", "远程会议", "自动驾驶", "远程控制", "关键任务"
        ]

        embb_keywords = [
            "embb", "high throughput", "large bandwidth", "video streaming",
            "hd video", "4k", "8k", "download", "broadband",
            "大带宽", "高吞吐", "高清视频", "视频流", "下载", "宽带"
        ]

        mmtc_keywords = [
            "mmtc", "iot", "sensor", "massive devices", "massive connection",
            "物联网", "传感器", "海量连接", "大量终端", "低功耗"
        ]

        if any(k in t for k in urllc_keywords):
            return "URLLC"
        if any(k in t for k in embb_keywords):
            return "eMBB"
        if any(k in t for k in mmtc_keywords):
            return "mMTC"

        return "eMBB"

    def _extract_latency(self, text: str) -> Optional[float]:
        patterns = [
            r"latency\s*(?:<|<=|less than|below|under)?\s*(\d+(?:\.\d+)?)\s*ms",
            r"delay\s*(?:<|<=|less than|below|under)?\s*(\d+(?:\.\d+)?)\s*ms",
            r"时延(?:小于|低于|不超过|少于|控制在)?\s*(\d+(?:\.\d+)?)\s*(?:ms|毫秒)",
            r"延迟(?:小于|低于|不超过|少于|控制在)?\s*(\d+(?:\.\d+)?)\s*(?:ms|毫秒)",
            r"(\d+(?:\.\d+)?)\s*(?:ms|毫秒)\s*(?:以内|以下)"
        ]

        for p in patterns:
            m = re.search(p, text, flags=re.IGNORECASE)
            if m:
                return float(m.group(1))

        return None

    def _extract_throughput(self, text: str) -> Optional[float]:
        patterns = [
            r"throughput\s*(?:>|>=|at least|above)?\s*(\d+(?:\.\d+)?)\s*(gbps|mbps)",
            r"bandwidth\s*(?:>|>=|at least|above)?\s*(\d+(?:\.\d+)?)\s*(gbps|mbps)",
            r"吞吐量(?:大于|高于|不低于|至少)?\s*(\d+(?:\.\d+)?)\s*(gbps|mbps|g|m)",
            r"带宽(?:大于|高于|不低于|至少)?\s*(\d+(?:\.\d+)?)\s*(gbps|mbps|g|m)",
            r"(\d+(?:\.\d+)?)\s*(gbps|mbps)\s*(?:吞吐|带宽)?"
        ]

        for p in patterns:
            m = re.search(p, text, flags=re.IGNORECASE)
            if m:
                value = float(m.group(1))
                unit = m.group(2).lower()
                if unit in ["gbps", "g"]:
                    value *= 1000
                return value

        return None

    def _extract_reliability(self, text: str) -> Optional[float]:
        patterns = [
            r"reliability\s*(?:>|>=|at least|above)?\s*(\d+(?:\.\d+)?)\s*%",
            r"可靠性(?:大于|高于|不低于|至少)?\s*(\d+(?:\.\d+)?)\s*%",
            r"稳定性(?:大于|高于|不低于|至少)?\s*(\d+(?:\.\d+)?)\s*%"
        ]

        for p in patterns:
            m = re.search(p, text, flags=re.IGNORECASE)
            if m:
                return float(m.group(1))

        if any(k in text.lower() for k in ["stable", "reliable", "稳定", "可靠", "不中断"]):
            return 99.0

        return None

    def _extract_priority(self, text: str) -> int:
        t = text.lower()

        high_keywords = ["urgent", "important", "critical", "highest", "紧急", "重要", "关键", "最高优先级"]
        low_keywords = ["low priority", "not urgent", "普通", "不紧急", "低优先级"]

        if any(k in t for k in high_keywords):
            return 1
        if any(k in t for k in low_keywords):
            return 4

        return 3

    def _extract_region(self, text: str) -> Optional[str]:
        city_patterns = [
            r"in\s+([A-Z][a-zA-Z'\-]+)",
            r"at\s+([A-Z][a-zA-Z'\-]+)",
            r"位于([\u4e00-\u9fa5]{2,10})",
            r"在([\u4e00-\u9fa5]{2,10})"
        ]

        for p in city_patterns:
            m = re.search(p, text)
            if m:
                region = m.group(1)
                stop_words = ["June", "May", "April", "March", "Monday", "Tuesday"]
                if region not in stop_words:
                    return region

        known_cities = ["Xi’an", "Xian", "Shanghai", "Beijing", "西安", "上海", "北京", "深圳", "广州", "杭州"]
        for c in known_cities:
            if c in text:
                return c

        return None

    def _extract_time(self, text: str) -> Optional[str]:
        m = re.search(r"\d{4}-\d{1,2}-\d{1,2}", text)
        if m:
            return m.group(0)

        m = re.search(
            r"(Jan|Feb|Mar|Apr|May|Jun|June|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{1,2})",
            text,
            flags=re.IGNORECASE
        )
        if m:
            month_map = {
                "jan": "01", "feb": "02", "mar": "03", "apr": "04",
                "may": "05", "jun": "06", "june": "06", "jul": "07",
                "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12"
            }
            month = month_map[m.group(1).lower()[:3]]
            day = int(m.group(2))
            return f"2025-{month}-{day:02d}"

        return None

    def _fill_default_qos(self, intent: NetworkIntent) -> None:
        """
        Fill missing QoS fields according to service type.
        These defaults are only for demonstration.
        In a real system, they should come from the network knowledge base.
        """

        if intent.serviceType == "URLLC":
            intent.latency = intent.latency if intent.latency is not None else 10.0
            intent.throughput = intent.throughput if intent.throughput is not None else 20.0
            intent.reliability = intent.reliability if intent.reliability is not None else 99.0

        elif intent.serviceType == "eMBB":
            intent.latency = intent.latency if intent.latency is not None else 50.0
            intent.throughput = intent.throughput if intent.throughput is not None else 100.0
            intent.reliability = intent.reliability if intent.reliability is not None else 95.0

        elif intent.serviceType == "mMTC":
            intent.latency = intent.latency if intent.latency is not None else 100.0
            intent.throughput = intent.throughput if intent.throughput is not None else 1.0
            intent.reliability = intent.reliability if intent.reliability is not None else 90.0


class IntentValidator:
    """
    Three-aspect validation inspired by LIMO:
    1. Format Checking
    2. Semantic Validation
    3. Consistency Assessment
    """

    def __init__(self, threshold: int = 9):
        self.threshold = threshold

    def validate(self, intent: NetworkIntent) -> Dict[str, Any]:
        format_score, format_msgs = self._format_checking(intent)
        semantic_score, semantic_msgs = self._semantic_validation(intent)
        consistency_score, consistency_msgs = self._consistency_assessment(intent)

        qualified = (
            format_score >= self.threshold
            and semantic_score >= self.threshold
            and consistency_score >= self.threshold
        )

        return {
            "structuredIntent": intent.to_limo_json(),
            "scores": {
                "formatChecking": format_score,
                "semanticValidation": semantic_score,
                "consistencyAssessment": consistency_score
            },
            "qualified": qualified,
            "messages": {
                "formatChecking": format_msgs,
                "semanticValidation": semantic_msgs,
                "consistencyAssessment": consistency_msgs
            }
        }

    def _format_checking(self, intent: NetworkIntent):
        score = 10
        msgs: List[str] = []

        mandatory_fields = ["serviceType", "latency", "throughput", "priority"]

        for field in mandatory_fields:
            if getattr(intent, field) is None:
                score -= 1
                msgs.append(f"Missing mandatory field: {field}")

        if intent.serviceType not in ["URLLC", "eMBB", "mMTC"]:
            score -= 5
            msgs.append("Invalid serviceType. Expected one of URLLC, eMBB, mMTC.")

        if intent.latency is not None and not isinstance(intent.latency, (int, float)):
            score -= 5
            msgs.append("Latency type mismatch.")

        if intent.throughput is not None and not isinstance(intent.throughput, (int, float)):
            score -= 5
            msgs.append("Throughput type mismatch.")

        if intent.priority is not None and not isinstance(intent.priority, int):
            score -= 5
            msgs.append("Priority type mismatch.")

        return max(score, 0), msgs

    def _semantic_validation(self, intent: NetworkIntent):
        score = 10
        msgs: List[str] = []

        text = intent.rawText.lower() if intent.rawText else ""

        if any(k in text for k in ["low latency", "低时延", "超低时延"]) and intent.serviceType != "URLLC":
            score -= 10
            msgs.append("Low-latency semantics should map to URLLC.")

        if any(k in text for k in ["high throughput", "大带宽", "高吞吐"]) and intent.serviceType != "eMBB":
            score -= 10
            msgs.append("High-throughput semantics should map to eMBB.")

        if any(k in text for k in ["iot", "sensor", "物联网", "传感器", "海量连接"]) and intent.serviceType != "mMTC":
            score -= 10
            msgs.append("Massive IoT semantics should map to mMTC.")

        if intent.latency is not None and intent.latency <= 0:
            score -= 5
            msgs.append("Latency must be positive.")

        if intent.throughput is not None and intent.throughput <= 0:
            score -= 5
            msgs.append("Throughput must be positive.")

        if intent.reliability is not None and not (0 < intent.reliability <= 100):
            score -= 5
            msgs.append("Reliability must be within (0, 100].")

        if intent.priority is not None and not (1 <= intent.priority <= 5):
            score -= 5
            msgs.append("Priority must be between 1 and 5.")

        return max(score, 0), msgs

    def _consistency_assessment(self, intent: NetworkIntent):
        score = 10
        msgs: List[str] = []

        if intent.serviceType == "URLLC":
            if intent.latency is not None and intent.latency > 20:
                score -= 5
                msgs.append("URLLC conflicts with latency greater than 20 ms.")
            if intent.reliability is not None and intent.reliability < 99:
                score -= 5
                msgs.append("URLLC usually requires reliability no lower than 99%.")

        if intent.serviceType == "eMBB":
            if intent.throughput is not None and intent.throughput < 10:
                score -= 5
                msgs.append("eMBB conflicts with very low throughput.")

        if intent.serviceType == "mMTC":
            if intent.throughput is not None and intent.throughput > 50:
                score -= 5
                msgs.append("mMTC usually does not require very high throughput.")

        if intent.priority == 1 and intent.latency is not None and intent.latency > 100:
            score -= 5
            msgs.append("High-priority service conflicts with excessive latency.")

        return max(score, 0), msgs


class LIMOStyleIntentModule:
    def __init__(self, threshold: int = 9):
        self.parser = IntentParser()
        self.validator = IntentValidator(threshold=threshold)

    def run(self, text: str) -> Dict[str, Any]:
        intent = self.parser.parse(text)
        result = self.validator.validate(intent)
        return result


if __name__ == "__main__":
    module = LIMOStyleIntentModule(threshold=9)

    user_intent = (
        "I plan to initiate an important remote video conference in Xi’an on June 20. "
        "The session must remain stable throughout. Please generate an appropriate "
        "network configuration for this service."
    )

    result = module.run(user_intent)

    print(json.dumps(result, ensure_ascii=False, indent=2))