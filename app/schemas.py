# defines how data looks

from pydantic import BaseModel, HttpUrl
from typing import List, Optional

class Claim(BaseModel):
    text: str
    verdict: Optional[str] = "Unverified"
    confidence: float = 0.0

class ArticleResponse(BaseModel):
    id: str
    url: HttpUrl
    claims: List[Claim]