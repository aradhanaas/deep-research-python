from tavily import TavilyClient
tavily = TavilyClient(api_key="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")
result = tavily.search(query="Singapore insurance", max_results=5)
print(result)  # Print the whole dict
print(f"DEBUG: Tavily raw search result: {result}")

# If you want just the data list:
print(result.get("data"))