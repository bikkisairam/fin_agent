"""
Decision Tool
--------------
Takes reasoning output and produces a structured decision
(approve, deny, escalate) with justification.
"""
from src.config.env_loader import load_env
load_env()

from langchain_openai import ChatOpenAI


class DecisionTool:

    def __init__(self, model="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, temperature=0.0)

    def decide(self, reasoning: str) -> str:
        prompt = f"""
        You are a senior risk manager at Discover Financial.
        
        Based on the reasoning below, produce a STRICT JSON decision:

        {{
          "decision": "approve" | "deny" | "escalate",
          "justification": "...",
          "follow_up_actions": ["...", "..."]
        }}

        FRAUD REASONING:
        {reasoning}
        """

        response = self.llm.invoke(prompt)
        return response.content
