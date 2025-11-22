"""
Document Chunker Module
-----------------------
Splits long text into semantically meaningful chunks for
RAG and vector indexing.

Author: Sai Ram Bikki
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

class Chunker:

    @staticmethod
    def chunk(text: str, size: int = 800, overlap: int = 150) -> List[str]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

        return splitter.split_text(text)
