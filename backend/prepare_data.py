from scraper import get_all_links, scrape_page
from pdf_loader import load_pdfs
from retriever import SimpleRetriever
import json
import os

pdf_folder = "../data/support_pdfs"

# Step 1: Scrape webpages
urls = get_all_links()
web_docs = [scrape_page(url) for url in urls]

# Optional: Save raw HTML/text
with open("../data/raw_html.json", "w") as f:
    json.dump(web_docs, f)

# Step 2: Load PDF docs
pdf_docs = load_pdfs(pdf_folder)

# Step 3: Combine
all_docs = web_docs + pdf_docs

# Step 4: Fit retriever
retriever = SimpleRetriever()
retriever.fit(all_docs)
retriever.save("knowledge_base.pkl")
print("✅ Knowledge base created and saved.")
