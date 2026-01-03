"""
Summarizer Tool
---------------
Summarizes long financial policy text into clear, structured bullet points.
Used by PolicyAgent and ReasoningAgent.
"""
from src.config.env_loader import load_env
load_env()


from langchain_openai import ChatOpenAI


class SummarizerTool:

    def __init__(self, model="gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, temperature=0.2)

    def summarize(self, text: str) -> str:
        prompt = f"""
        You are a senior compliance analyst at a major bank.
        Summarize the following policy text into 3-5 bullet points.
        Keep terminology and definitions accurate.

        POLICY TEXT:
        {text}
        """

        response = self.llm.invoke(prompt)
        return response.content
