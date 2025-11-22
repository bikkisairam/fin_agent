"""
Metadata Extractor Module
-------------------------
Extracts metadata fields from filenames and attaches them
to chunk objects for indexing and traceability.

Author: Sai Ram Bikki
"""

import re
from datetime import datetime

class MetadataExtractor:

    @staticmethod
    def extract(filename: str, chunk_id: str) -> dict:

        # detect section numbers like "3.2", "6.4.1"
        match = re.search(r"(\d+(\.\d+)+)", filename)
        section = match.group() if match else None

        return {
            "source_file": filename,
            "chunk_id": chunk_id,
            "section_hint": section,
            "ingested_at": datetime.utcnow().isoformat()
        }
