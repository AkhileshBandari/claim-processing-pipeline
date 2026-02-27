from fastapi import FastAPI, UploadFile, File, Form
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

from utilities.pdf_loader import load_pdf_pages
from graph import graph

app = FastAPI()

@app.post("/api/process")
async def process_claim(
    claim_id: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        pages = load_pdf_pages(file.file)

        result = graph.invoke({
            "claim_id": claim_id,
            "pages": pages,
            "classified_pages": {},
            "id_data": {},
            "discharge_data": {},
            "bill_data": {},
            "final_output": {}
        })

        return result["final_output"]

    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}