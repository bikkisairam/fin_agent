"""
Policy Retriever Tool
---------------------
Queries the FAISS vectorstore to fetch relevant policy text.
"""

from src.vectorstore.retriever import VectorRetriever


class PolicyRetrieverTool:

    def __init__(self, index_path: str):
        self.retriever = VectorRetriever(index_path)

    def search(self, query: str, k: int = 5):
        """
        Returns list of policy text chunks.
        """
        results = self.retriever.search(query, k=k)
        return [r.page_content for r in results]
