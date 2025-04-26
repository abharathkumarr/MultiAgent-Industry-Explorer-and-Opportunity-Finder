# agents/resources.py
import os
from kaggle.api.kaggle_api_extended import KaggleApi
from utils.search import serper_search

_kaggle = KaggleApi()
_kaggle.authenticate()

def _kaggle_find(keyword: str, max_items: int = 2) -> list[tuple[str, str]]:
    try:
        ds = _kaggle.dataset_list(search=keyword, max_size=None, page_size=max_items)
        return [(d.title, f"https://www.kaggle.com/datasets/{d.ref}") for d in ds]
    except Exception:
        return []

def _hf_find(keyword: str) -> list[tuple[str, str]]:
    q = f"{keyword} site:huggingface.co/datasets"
    hits = serper_search(q, 3)
    return [(h["title"], h["link"]) for h in hits]

def collect_resources(usecase_title: str) -> list[tuple[str, str]]:
    key = usecase_title.lower().split()[0:3]
    query = " ".join(key)
    resources = _kaggle_find(query) + _hf_find(query)
    return resources[:4]
