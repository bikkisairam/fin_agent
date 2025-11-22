"""
Ingestion Pipeline
------------------
Reads raw PDFs -> cleans -> chunks -> attaches metadata ->
saves JSONL file for vector indexing.

Author: Sai Ram Bikki
"""

import os
import json
from typing import List

from .pdf_reader import PDFReader
from .text_cleaner import TextCleaner
from .chunker import Chunker
from .metadata import MetadataExtractor

class IngestionPipeline:

    def __init__(self, raw_dir: str, output_path: str):
        self.raw_dir = raw_dir
        self.output_path = output_path

    def run(self):
        processed = []

        for filename in os.listdir(self.raw_dir):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(self.raw_dir, filename)

                raw = PDFReader.read_pdf(pdf_path)
                cleaned = TextCleaner.clean(raw)
                chunks = Chunker.chunk(cleaned)

                for index, chunk in enumerate(chunks):
                    meta = MetadataExtractor.extract(filename, f"{filename}_chunk_{index}")
                    processed.append({"text": chunk, "metadata": meta})

        # write output JSONL
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        with open(self.output_path, "w") as f:
            for item in processed:
                f.write(json.dumps(item) + "\n")

        print(f"[IngestionPipeline] Completed — Total chunks: {len(processed)}")
