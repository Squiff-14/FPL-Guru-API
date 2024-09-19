from pydantic import BaseModel
from typing import Optional

class PlayerFilter(BaseModel):
    team: Optional[int]
    first_name: Optional[str]
    second_name: Optional[str]
    id: Optional[int]
