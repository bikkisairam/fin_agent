"""
Reasoning Agent
---------------
Uses fraud reasoning to create analytic output.
"""

from src.tools.fraud_reasoner_tool import FraudReasonerTool


class ReasoningAgent:

    def __init__(self):
        self.reasoner = FraudReasonerTool()

    def run(self, user_query: str, evidence: list[str]):
        reasoning_output = self.reasoner.analyze(user_query, evidence)

        return {
            "query": user_query,
            "reasoning": reasoning_output
        }
