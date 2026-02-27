Claim Processing Pipeline – Multi-Agent LangGraph Workflow

A FastAPI-based document processing system that uses LangGraph to orchestrate multi-agent LLM workflows for medical insurance claim extraction.

->Problem Statement
Build an API that:
Accepts a medical claim PDF
Classifies each page into document type
Routes relevant pages to extraction agents
Extracts structured information
Aggregates final JSON response

->Architecture Overview
The system uses a graph-based orchestration approach powered by LangGraph.
START
   ↓
Segregator Agent (LLM Classification)
   ↓
 ┌─────────────┬────────────────────┬───────────────────┐
 ID Agent   Discharge Agent   Itemized Bill Agent
   ↓              ↓                  ↓
              Aggregator
                 ↓
                END

->Design Principles
1️⃣ Page-Level Isolation

Each PDF page is classified independently to prevent cross-document contamination.

2️⃣ Scoped Context

Extraction agents receive only relevant pages — not the full PDF.

3️⃣ Deterministic Orchestration

LangGraph defines explicit state transitions between nodes.

->Document Types Classified
The Segregator Agent classifies pages into:
claim_forms
cheque_or_bank_details
identity_document
itemized_bill
discharge_summary
prescription
investigation_report
cash_receipt
other
Only 3 extraction agents process routed pages.

->Extraction Agents
1️⃣ ID Agent
Extracts:
patient_name
date_of_birth
id_number
policy_number
insurance_provided
2️⃣ Discharge Summary Agent
Extracts:
diagnosis
admission_date
discharge_date
treating_physician
3️⃣ Itemized Bill Agent
Extracts:
item_name
quantity
unit_cost
total_cost
Performs programmatic total calculation for validation.

->Tech Stack
FastAPI
LangGraph
LangChain
OpenAI API
PyPDF
Python 3.10+

->Aggregator Node
{
  "claim_id": "...",
  "identity": {...},
  "discharge_summary": {...},
  "bill": {...}
}

->Project Structure
claim-processing-pipeline/
│
├── agents/
│   ├── segregater.py
│   ├── id_agent.py
│   ├── discharge_agent.py
│   ├── bill_agent.py
│   └── aggregator.py
│
├── utilities/
│   ├── pdf_loader.py
│   └── json_utils.py
│
├── graph.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

Setup & Installation

Step 1 — Clone Repository
git clone https://github.com/AkhileshBandari/claim-processing-pipeline.git
cd claim-processing-pipeline
Step 2 — Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
Step 3 — Install Dependencies
pip install -r requirements.txt
Step 4 — Configure Environment Variables
Create a .env file in project root:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

⚠️ Do not commit this file.

▶️ Run Application
uvicorn main:app --reload

http://127.0.0.1:8000/docs open this in the browser....