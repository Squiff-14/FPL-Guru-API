
from typing import Optional
from pydantic import BaseModel

class Phase(BaseModel):
    id: int
    name: str
    start_event: int
    stop_event: int
    highest_score: Optional[int]
