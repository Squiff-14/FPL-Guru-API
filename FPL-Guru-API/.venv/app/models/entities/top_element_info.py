from pydantic import BaseModel

class TopElementInfo(BaseModel):
    id: int
    points: int