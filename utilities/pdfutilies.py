import fitz

def extract_pages_from_pdf(pdf_bytes: bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append({
            "page_number": i + 1,
            "text": text
        })

    return pages