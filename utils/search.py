# utils/search.py
import os
import requests
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

SERPER_KEY = os.getenv("SERPER_API_KEY")
_SERPER_URL = "https://google.serper.dev/search"
_ddg = DuckDuckGoSearchAPIWrapper()

def serper_search(query: str, num_results: int = 10) -> list[dict]:
    headers = {"X-API-KEY": SERPER_KEY}
    payload = {"q": query, "num": num_results}
    try:
        resp = requests.post(_SERPER_URL, headers=headers, json=payload, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        return data.get("organic", [])
    except Exception as exc:
        print(f"[Serper] fallback to DuckDuckGo ({exc})")
        return [{"title": r["title"], "link": r["href"], "snippet": r["body"]}
                for r in _ddg.results(query, max_results=num_results)]
