# agents/research.py
import os
import re
from bs4 import BeautifulSoup
import requests
from langchain_groq import ChatGroq    
from utils.search import serper_search


llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192",
    temperature=0.3,
)

def _scrape(url: str, max_chars: int = 3000) -> str:
    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(" ", strip=True)
        return text[:max_chars]
    except Exception:
        return ""

def run_research(target: str) -> dict:
    hits = serper_search(f"{target} industry overview", 5)
    corpus = " ".join(_scrape(h["link"]) for h in hits)
    prompt = f"""You are an industry analyst.
Summarize the key offerings, strategic focus areas, and recent AI trends for the target below in max 120 words.

TARGET: {target}
SOURCE TEXT:
{corpus}
"""
    result = llm.invoke(prompt)
    result_content = result.content   # ✅ Extract plain string
    offerings = re.findall(r"•\s*(.+)", result_content) or []
    return {"summary": result_content, "offerings": offerings}
