"""
Vectorstore Retriever
---------------------
Provides a clean API for similarity search.
"""
from src.config.env_loader import load_env
load_env()

from langchain_community.vectorstores import FAISS

from langchain_openai import OpenAIEmbeddings


class VectorRetriever:

    def __init__(self, index_path: str):
        model = OpenAIEmbeddings(model="text-embedding-3-small")
        self.db = FAISS.load_local(index_path, model, allow_dangerous_deserialization=True)

    def search(self, query: str, k: int = 5):
        return self.db.similarity_search(query, k=k)
