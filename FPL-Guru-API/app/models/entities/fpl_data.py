from pydantic import BaseModel
from typing import List
from app.models.entities.game_settings import GameSettings
from app.models.entities.phase import Phase
from app.models.entities.team import Team
from app.models.entities.player import Player
from app.models.entities.player_stat  import PlayerStat  
from app.models.entities.player_type import PlayerType
from app.models.entities.event import Event

class FPLData(BaseModel):
    events: List[Event]
    game_settings: GameSettings
    phases: List[Phase]
    teams: List[Team]
    total_players: int
    elements: List[Player]
    element_stats: List[PlayerType]
    element_types: List[PlayerStat]
