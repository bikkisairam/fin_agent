"""
FAISS Index Builder
-------------------
Reads chunks.jsonl -> embeds -> creates FAISS index -> saves versioned index.
"""

import json
import os
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from .embedder import EmbeddingService
from .versioning import VectorstoreVersionManager

class IndexBuilder:

    def __init__(self, chunks_path: str, index_base_dir: str):
        self.chunks_path = chunks_path
        self.index_base_dir = index_base_dir

    def load_chunks(self):
        docs = []
        with open(self.chunks_path, "r") as f:
            for line in f:
                item = json.loads(line)
                docs.append(Document(
                    page_content=item["text"],
                    metadata=item["metadata"]
                ))
        return docs

    def build(self):
        docs = self.load_chunks()
        embedder = EmbeddingService()

        vectorstore = FAISS.from_documents(docs, embedder.model)

        save_path = VectorstoreVersionManager.get_save_path(self.index_base_dir)
        os.makedirs(save_path, exist_ok=True)

        vectorstore.save_local(save_path)
        print(f"[IndexBuilder] Saved FAISS index to {save_path}")

        return save_path
