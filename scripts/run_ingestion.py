import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from src.ingestion.ingestion_pipeline import IngestionPipeline

RAW_DIR = "data/raw"
OUTPUT = "data/processed/policy_chunks.jsonl"

pipeline = IngestionPipeline(RAW_DIR, OUTPUT)
pipeline.run()
