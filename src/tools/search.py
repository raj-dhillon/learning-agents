from ddgs import DDGS

def search_web(query: str, max_results: int = 3):
    BLOCKED_DOMAINS = ["youtube.com", "twitch.tv", "tiktok.com"]

    with DDGS() as ddgs:
        results = []
        for r in ddgs.text(query, max_results=max_results * 3):  
            # filter out unwanted domains
            if any(b in r["href"] for b in BLOCKED_DOMAINS):
                continue
            results.append(r)
            if len(results) >= max_results:
                break
        return results

# print(search_web)
search_web("what is a memory palace?")