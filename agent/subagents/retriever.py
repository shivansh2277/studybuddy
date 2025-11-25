from ..tools.web_search import search_web

def retrieve_resources(topic: str, top_k: int = 3):
"""Return a small list of short resources for the topic (simulated)."""
results = search_web(f"{topic} concise explanation", top_k=top_k)
return results
