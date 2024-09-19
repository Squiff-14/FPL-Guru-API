from pydantic import BaseModel


class PlayerStat(BaseModel):
    label: str
    name: str
