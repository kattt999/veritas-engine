# shared memory for AI agents

from typing import TypedDict, List, Annotated
import operator

class AgentState(TypedDict):
    content: str               # The raw article text
    claims: Annotated[List[str], operator.add]  # List of claims found
    evidence: List[dict]       # Search results found
    final_report: str          # Final summary