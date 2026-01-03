import os, sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)


from src.vectorstore.index_builder import IndexBuilder

CHUNKS = "data/processed/policy_chunks.jsonl"
INDEX_BASE = "vectorstore/"

builder = IndexBuilder(CHUNKS, INDEX_BASE)
builder.build()
