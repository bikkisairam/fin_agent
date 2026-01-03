"""
Agent Orchestrator Graph
------------------------
Defines the agent workflow using LangGraph.
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, List

from .policy_agent import PolicyAgent
from .reasoning_agent import ReasoningAgent
from .decision_agent import DecisionAgent


class AgentState(TypedDict):
    query: str
    evidence: List[str]
    summaries: List[str]
    reasoning: str
    decision: str


class Orchestrator:

    def __init__(self, index_path: str):
        self.policy_agent = PolicyAgent(index_path)
        self.reasoning_agent = ReasoningAgent()
        self.decision_agent = DecisionAgent()

    def build_graph(self):

        graph = StateGraph(AgentState)

        # ----- Nodes -----
        def policy_node(state):
            result = self.policy_agent.run(state["query"])
            return {
                "query": state["query"],
                "evidence": result["evidence"],
                "summaries": result["summaries"]
            }

        def reasoning_node(state):
            result = self.reasoning_agent.run(state["query"], state["evidence"])
            return {"reasoning": result["reasoning"]}

        def decision_node(state):
            final = self.decision_agent.run(state["reasoning"])
            return {"decision": final}

        graph.add_node("policy", policy_node)
        graph.add_node("reasoning", reasoning_node)
        graph.add_node("decision", decision_node)

        # ----- Edges -----
        graph.add_edge("policy", "reasoning")
        graph.add_edge("reasoning", "decision")
        graph.add_edge("decision", END)

        graph.set_entry_point("policy")

        return graph.compile()
