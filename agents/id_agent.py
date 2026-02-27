from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from utilities.json_utils import safe_json_parse

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def id_agent(state):
    pages = state["classified_pages"].get("identity_document", [])

    if not pages:
        state["id_data"] = {}
        return state

    combined_text = "\n".join([p["text"] for p in pages])

    prompt = f"""
    Extract:
    - patient_name
    - date_of_birth
    - id_number
    - policy_number
    - insurance_provider

    Return JSON only.

    Text:
    {combined_text[:6000]}
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    state["id_data"] = safe_json_parse(response.content)

    return state