from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from utilities.json_utils import safe_json_parse, clean_number

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def bill_agent(state):
    pages = state["classified_pages"].get("itemized_bill", [])

    if not pages:
        state["bill_data"] = {}
        return state

    combined_text = "\n".join([p["text"] for p in pages])

    prompt = f"""
    Extract all bill line items.

    Each item must include:
    - item_name
    - quantity
    - unit_cost
    - total_cost

    Return JSON:
    {{
        "items": [
            {{
                "item_name": "",
                "quantity": 0,
                "unit_cost": 0,
                "total_cost": 0
            }}
        ]
    }}

    Text:
    {combined_text[:8000]}
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    data = safe_json_parse(response.content)

    items = data.get("items", [])

    calculated_total = 0
    for item in items:
        total_cost = clean_number(item.get("total_cost", 0))
        calculated_total += total_cost

    data["calculated_total"] = calculated_total
    state["bill_data"] = data

    return state