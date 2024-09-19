from app.services.interfaces.team_service_interface import ITeamService
from app.models.entities.team import Team
from typing import List
from fastapi_cache.decorator import cache
import logging

class TeamService(ITeamService):

    def __init__(self, fpl_api_service) -> None:
        self.fpl_api_service = fpl_api_service
        self.logger = logging.getLogger(__name__)
        super().__init__()

    @cache(expire=300)
    async def get_all_teams(self) -> List[Team]:
        try:
            data = await self.fpl_api_service.get_bootstrap_static()
            teams = data.get("teams", [])
            return teams
        except Exception as e:
            self.logger.error(f"Error fetching all teams: {e}", exc_info=True)
            raise  # Optionally re-raise the exception to propagate it if necessary

    @cache(expire=300)
    async def get_team(self, team_id: int) -> Team:
        try:
            data = await self.fpl_api_service.get_bootstrap_static()
            teams = data.get("teams", [])
            team = next((team for team in teams if team["id"] == team_id), None)
            if team is None:
                raise ValueError(f"Team with ID {team_id} not found.")
            return team
        except Exception as e:
            self.logger.error(f"Error fetching team with ID {team_id}: {e}", exc_info=True)
            raise  # Optionally re-raise the exception
