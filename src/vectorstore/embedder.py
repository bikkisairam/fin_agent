"""
Embedding Service
-----------------
Encapsulates the embedding model.
"""

import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

class EmbeddingService:

    def __init__(self, model_name: str = "text-embedding-3-small"):
        self.model = OpenAIEmbeddings(model=model_name)

    def embed_documents(self, docs):
        return self.model.embed_documents(docs)

    def embed_query(self, query: str):
        return self.model.embed_query(query)
