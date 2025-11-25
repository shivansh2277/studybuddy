# Simulated search results for offline demo. Replace with a real search API (SerpAPI/Bing) or the
# course-provided MCP search tool for an online demo.


def search_web(query: str, top_k: int = 3):
sample = [
{"title": f"{query} - Concept A", "snippet": "Concise explanation A", "url": "https://example.com/a"},
{"title": f"{query} - Concept B", "snippet": "Concise explanation B", "url": "https://example.com/b"},
{"title": f"{query} - Example", "snippet": "Worked example", "url": "https://example.com/ex"}
]
return sample[:top_k]
