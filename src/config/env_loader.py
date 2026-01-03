import os
from dotenv import load_dotenv

def load_env():
    # Find .env in the project root
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    env_path = os.path.join(root_dir, ".env")
    load_dotenv(env_path)
