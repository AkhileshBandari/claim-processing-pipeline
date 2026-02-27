from pypdf import PdfReader

def load_pdf_pages(file):
    reader = PdfReader(file)
    pages = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        pages.append({
            "page_number": i + 1,
            "text": text if text else ""
        })

    return pages