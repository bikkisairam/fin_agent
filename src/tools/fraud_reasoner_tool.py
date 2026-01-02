"""
Fraud Reasoner Tool
-------------------
Performs analytical reasoning using retrieved policy evidence.
Simulates a fraud investigation analyst.
"""

from langchain_openai import ChatOpenAI


class FraudReasonerTool:

    def __init__(self, model="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, temperature=0.0)

    def analyze(self, query: str, evidence: list[str]) -> str:
        evidence_text = "\n\n".join(evidence)

        prompt = f"""
        You are a fraud investigator at a major US bank.
        Your responsibility is to interpret policy rules and provide a clear reasoning output.

        CUSTOMER QUERY:
        {query}

        RELEVANT POLICY EVIDENCE:
        {evidence_text}

        Provide:
        - Key policy rules involved
        - Fraud reasoning steps
        - What the investigator should check next
        - A recommended preliminary action
        """

        response = self.llm.invoke(prompt)
        return response.content
