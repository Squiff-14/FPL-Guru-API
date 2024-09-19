from abc import ABC, abstractmethod
from typing import List, Optional 
from typing import Any
from app.models.entities.player import Player
from app.models.filters.player_filter import PlayerFilter

class IPlayerService(ABC):
    @abstractmethod
    async def get_all_players(self, player_filter: Optional[PlayerFilter] = None) -> List[Player]:
        pass

    @abstractmethod
    async def get_player(self, player_id: int) -> Player:
        pass