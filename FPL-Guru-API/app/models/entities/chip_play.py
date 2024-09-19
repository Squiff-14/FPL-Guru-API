from pydantic import BaseModel

class ChipPlay(BaseModel):
    chip_name: str
    num_played: int