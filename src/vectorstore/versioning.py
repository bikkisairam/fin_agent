"""
Vectorstore Version Manager
---------------------------
Handles versioning, naming, and lifecycle of FAISS indexes.
"""

import os
from datetime import datetime

class VectorstoreVersionManager:

    @staticmethod
    def generate_version_name() -> str:
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        return f"policy_index_{timestamp}"

    @staticmethod
    def get_save_path(base_dir: str) -> str:
        version_name = VectorstoreVersionManager.generate_version_name()
        return os.path.join(base_dir, version_name)
