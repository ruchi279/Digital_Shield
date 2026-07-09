import re

class ScamScriptDetector:
    def __init__(self):
        self.high_risk_keywords = {
            "authority": [r"cbi", r"customs", r"narcotics", r"ed officer", r"mha", r"supreme court"],
            "intimidation": [r"illegal passport", r"sim card tracking", r"money laundering", r"arrest warrant"],
            "isolation": [r"don't hang up", r"secret supervision", r"skype call", r"confidential room"],
            "financial": [r"verify account", r"clearance funds", r"safe custody", r"transfer fund", r"security deposit"]
        }

    def analyze_transcript(self, text: str) -> dict:
        text_lower = text.lower()
        matched_categories = {}
        score = 0

        for category, patterns in self.high_risk_keywords.items():
            matches = []
            for pattern in patterns:
                if re.search(pattern, text_lower):
                    matches.append(pattern)
            
            if matches:
                matched_categories[category] = matches
                score += 25 

        if score >= 75:
            verdict = "CRITICAL: High Probability Digital Arrest Scam"
        elif score >= 50:
            verdict = "WARNING: Suspicious Coercive Activity"
        else:
            verdict = "SAFE: Low Risk"

        return {
            "risk_score": score,
            "verdict": verdict,
            "triggered_phases": list(matched_categories.keys()),
            "evidence": matched_categories
        }