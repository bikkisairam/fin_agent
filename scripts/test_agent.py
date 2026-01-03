import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from src.config.env_loader import load_env
load_env()

from src.orchestrator.orchestrator_graph import Orchestrator

INDEX_PATH = "vectorstore/policy_index_20260103_010350"

orchestrator = Orchestrator(INDEX_PATH)
graph = orchestrator.build_graph()

result = graph.invoke({"query": "What happens when my overdraft protection triggers?"})

# Print ONLY the decision object
print(result["decision"])
