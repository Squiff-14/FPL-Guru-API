# player_comparison_request.py
from typing import List
from pydantic import BaseModel

from app.models.entities.player import Player

class PlayerComparisonRequest(BaseModel):
    player: Player
    other_players: List[Player]