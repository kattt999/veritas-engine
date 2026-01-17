# each function here is a node in the graph
# where call Ollama locally

import requests
import os
from app.agents.state import AgentState

# Change this to your Cloudflare Tunnel URL or localhost:11434
OLLAMA_URL = os.getenv("LOCAL_AI_URL", "http://localhost:11434")

def extract_claims_node(state: AgentState):
    prompt = f"Extract only the 3 most important factual claims from this text as a list: {state['content'][:2000]}"
    
    response = requests.post(f"{OLLAMA_URL}/api/generate", 
                             json={"model": "llama3.1", "prompt": prompt, "stream": False})
    
    # Simple parsing (In production, use structured output/regex)
    result = response.json().get("response", "No claims found")
    return {"claims": [result]}

def search_evidence_node(state: AgentState):
    # This would call your local SearXNG docker
    # For now, we simulate finding evidence based on the claims
    return {"evidence": [{"source": "Web Search", "snippet": "Evidence found for claims."}]}

def analyst_node(state: AgentState):
    prompt = f"Compare these claims: {state['claims']} with this evidence: {state['evidence']}. Give a verdict: TRUE, FALSE, or UNVERIFIED."
    
    response = requests.post(f"{OLLAMA_URL}/api/generate", 
                             json={"model": "llama3.1", "prompt": prompt, "stream": False})
    
    return {"final_report": response.json().get("response", "Analysis failed")}