from typing import TypedDict, Dict, List
from langgraph.graph import StateGraph, END

from agents.segregater import segregator_agent
from agents.id_agent import id_agent
from agents.discharge_agent import discharge_agent
from agents.bill_agent import bill_agent
from agents.aggregator import aggregator

class ClaimState(TypedDict):
    claim_id: str
    pages: List[Dict]
    classified_pages: Dict
    id_data: Dict
    discharge_data: Dict
    bill_data: Dict
    final_output: Dict

workflow = StateGraph(ClaimState)

workflow.add_node("segregator", segregator_agent)
workflow.add_node("id_agent", id_agent)
workflow.add_node("discharge_agent", discharge_agent)
workflow.add_node("bill_agent", bill_agent)
workflow.add_node("aggregator", aggregator)

workflow.set_entry_point("segregator")

workflow.add_edge("segregator", "id_agent")
workflow.add_edge("segregator", "discharge_agent")
workflow.add_edge("segregator", "bill_agent")

workflow.add_edge("id_agent", "aggregator")
workflow.add_edge("discharge_agent", "aggregator")
workflow.add_edge("bill_agent", "aggregator")

workflow.add_edge("aggregator", END)

graph = workflow.compile()