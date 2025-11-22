"""
PDF Reader Module
-----------------
Responsible for reading PDF files and extracting raw text.
Designed for enterprise-grade ingestion pipelines.

Author: Sai Ram Bikki
"""

import pypdf
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class PDFReader:
    """Reads PDF files and extracts text."""

    @staticmethod
    def read_pdf(path: str) -> Optional[str]:
        try:
            reader = pypdf.PdfReader(path)
            text = "\n".join([page.extract_text() or "" for page in reader.pages])
            logger.info(f"[PDFReader] Loaded PDF: {path}")
            return text
        except Exception as e:
            logger.error(f"[PDFReader] Failed to read {path}: {e}")
            raise
