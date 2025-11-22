"""
Text Cleaner Module
-------------------
Normalizes and sanitizes extracted text to remove noise.

Author: Sai Ram Bikki
"""

import re
from typing import Optional

class TextCleaner:

    @staticmethod
    def clean(text: Optional[str]) -> str:
        if not text:
            return ""

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text)

        # Remove non-ascii (pdf junk characters)
        text = text.encode("ascii", errors="ignore").decode()

        # Remove null bytes
        text = text.replace("\x00", "")

        return text.strip()
