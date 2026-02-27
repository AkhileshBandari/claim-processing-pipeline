def aggregator(state):
    state["final_output"] = {
        "claim_id": state["claim_id"],
        "identity": state.get("id_data", {}),
        "discharge_summary": state.get("discharge_data", {}),
        "bill": state.get("bill_data", {})
    }

    return state