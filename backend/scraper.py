import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.angelone.in/support"

def get_all_links():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, "html.parser")
    links = set()
    for a in soup.find_all("a", href=True):
        href = urljoin(BASE_URL, a['href'])
        if "/support/" in href and BASE_URL in href:
            links.add(href)
    return list(links)

def scrape_page(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    text = ' '.join(p.text.strip() for p in soup.find_all(['p', 'li']))
    return {"url": url, "title": soup.title.text if soup.title else url, "content": text}
