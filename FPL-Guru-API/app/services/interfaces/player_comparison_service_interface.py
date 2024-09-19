from abc import ABC, abstractmethod
from app.models.requests.player_comparison_request import PlayerComparisonRequest

class IPlayerComparisonService(ABC):
    @abstractmethod
    async def compare_players(request: PlayerComparisonRequest):
        pass
