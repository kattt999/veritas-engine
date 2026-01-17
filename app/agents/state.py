# shared memory for AI agents

from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    content: str               # Raw article text
    claims: List[str]          # Extracted factual statements
    evidence: List[dict]       # Research found via SearXNG
    final_report: str          # The final AI verdict