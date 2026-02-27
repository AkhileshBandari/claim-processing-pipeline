from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from utilities.json_utils import safe_json_parse

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

DOC_TYPES = [
    "claim_forms",
    "cheque_or_bank_details",
    "identity_document",
    "itemized_bill",
    "discharge_summary",
    "prescription",
    "investigation_report",
    "cash_receipt",
    "other"
]

def segregator_agent(state):
    pages = state["pages"]
    classified = {doc_type: [] for doc_type in DOC_TYPES}

    for page in pages:
        prompt = f"""
        Classify this medical claim document page into one of:
        {DOC_TYPES}

        Return JSON:
        {{
            "document_type": "<one_of_above>"
        }}

        Page Content:
        {page["text"][:4000]}
        """

        response = llm.invoke([HumanMessage(content=prompt)])
        result = safe_json_parse(response.content)

        doc_type = result.get("document_type", "other")

        if doc_type not in classified:
            doc_type = "other"

        classified[doc_type].append(page)

    state["classified_pages"] = classified
    return state
