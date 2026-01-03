"""
Decision Agent
--------------
Produces structured decision output from reasoning.
"""

from src.tools.decision_tool import DecisionTool


class DecisionAgent:

    def __init__(self):
        self.decision_tool = DecisionTool()

    def run(self, reasoning_output: str):
        decision_json = self.decision_tool.decide(reasoning_output)
        return decision_json
