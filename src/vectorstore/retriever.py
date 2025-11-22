"""
Vectorstore Retriever
---------------------
Provides a clean API for similarity search.
"""

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

class VectorRetriever:

    def __init__(self, index_path: str):
        model = OpenAIEmbeddings(model="text-embedding-3-small")
        self.db = FAISS.load_local(index_path, model, allow_dangerous_deserialization=True)

    def search(self, query: str, k: int = 5):
        return self.db.similarity_search(query, k=k)
