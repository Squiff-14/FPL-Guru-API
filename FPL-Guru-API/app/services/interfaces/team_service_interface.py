from abc import ABC, abstractmethod
from typing import Any
from typing import List
from app.models.entities.team import Team

class ITeamService(ABC):
    @abstractmethod
    async def get_all_teams(self) -> List[Team]:
        pass

    @abstractmethod
    async def get_team(self, team_id: int) -> Team:
        pass
