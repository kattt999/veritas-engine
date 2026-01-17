# each function here is a node in the graph
# where call Ollama locally

import requests
from app.agents.state import AgentState

def extract_claims_node(state: AgentState):
    # Call Local Ollama
    response = requests.post("http://localhost:11434/api/generate", 
                             json={"model": "llama3", "prompt": f"Extract 3 claims: {state['content']}"})
    # Logic to parse response...
    return {"claims": ["AI is taking over", "Coffee is healthy"]}

def search_evidence_node(state: AgentState):
    # Call Local SearXNG
    # results = requests.get("http://localhost:8080/search", params={"q": state['claims'][0]})
    return {"evidence": [{"source": "BBC", "snippet": "Research says coffee is fine."}]}