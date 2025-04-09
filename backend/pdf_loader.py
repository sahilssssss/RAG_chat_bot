import pdfplumber
import os

def load_pdfs(pdf_folder):
    docs = []
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            path = os.path.join(pdf_folder, file)
            text = ""
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    content = page.extract_text()
                    if content:
                        text += content + "\n"
            docs.append({"title": file, "content": text})
    return docs
