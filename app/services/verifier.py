import os
from app.agents.state import AgentState
from app.agents.nodes import extract_claims_node, search_evidence_node, analyst_node
from app.services.scrapper import scrape_article
from langgraph.graph import StateGraph, END

def create_verifier_graph():
    workflow = StateGraph(AgentState)
    workflow.add_node("deconstruct", extract_claims_node)
    workflow.add_node("research", search_evidence_node)
    workflow.add_node("analyze", analyst_node)

    workflow.set_entry_point("deconstruct")
    workflow.add_edge("deconstruct", "research")
    workflow.add_edge("research", "analyze")
    workflow.add_edge("analyze", END)
    return workflow.compile()

veritas_brain = create_verifier_graph()

async def run_full_verification(article_url: str):
    # 1. Scrape
    markdown_content = await scrape_article(article_url)
    
    # 2. Run AI Graph
    initial_state = {"content": markdown_content, "claims": [], "evidence": [], "final_report": ""}
    final_result = await veritas_brain.ainvoke(initial_state)
    
    print(f"VERDICT: {final_result['final_report']}")
    # 3. Here you would add supabase.table("articles").insert(...)