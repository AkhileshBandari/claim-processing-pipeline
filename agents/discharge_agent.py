from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from utilities.json_utils import safe_json_parse

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def discharge_agent(state):
    pages = state["classified_pages"].get("discharge_summary", [])

    if not pages:
        state["discharge_data"] = {}
        return state

    combined_text = "\n".join([p["text"] for p in pages])

    prompt = f"""
    Extract:
    - diagnosis
    - admission_date
    - discharge_date
    - treating_physician

    Return JSON only.

    Text:
    {combined_text[:6000]}
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["discharge_data"] = safe_json_parse(response.content)

    return state