"""
Policy Agent
------------
Retrieves policies and prepares structured evidence.
"""

from src.tools.policy_retriever_tool import PolicyRetrieverTool
from src.tools.summarizer_tool import SummarizerTool


class PolicyAgent:

    def __init__(self, index_path: str):
        self.retriever = PolicyRetrieverTool(index_path)
        self.summarizer = SummarizerTool()

    def run(self, user_query: str):
        # Step 1: Retrieve policies
        raw_chunks = self.retriever.search(user_query, k=5)

        # Step 2: Summarize policy evidence
        summaries = [self.summarizer.summarize(chunk) for chunk in raw_chunks]

        return {
            "query": user_query,
            "evidence": raw_chunks,
            "summaries": summaries
        }
