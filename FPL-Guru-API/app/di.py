from app.services.interfaces.openai_service_interace import IOpenAIService
from app.services.interfaces.player_comparison_service_interface import IPlayerComparisonService
from app.services.openai_service import OpenAIService
from app.services.player_comparison_service import PlayerComparisonService
from app.services.player_service import PlayerService
from app.services.fplapi_service import FplApiService
from app.services.team_service import TeamService
from app.services.interfaces.player_service_interface import IPlayerService
from app.services.interfaces.fplapi_service_interface import IFplApiService
from app.services.interfaces.team_service_interface import ITeamService
from fastapi import Depends

# Single dependency for IFplApiService (interface for FplApiService)
def get_fpl_api_service() -> IFplApiService:
    return FplApiService()

# Dependency for IPlayerService (interface for PlayerService)
def get_player_service(fplapi_service: IFplApiService = Depends(get_fpl_api_service)) -> IPlayerService:
    return PlayerService(fplapi_service)

# Dependency for ITeamService (interface for TeamService)
def get_team_service(fplapi_service: IFplApiService = Depends(get_fpl_api_service)) -> ITeamService:
    return TeamService(fplapi_service)

def get_openai_service() -> IOpenAIService:
    return OpenAIService()

def get_player_comparison_service(openai_service: IOpenAIService = Depends(get_openai_service)) -> IPlayerComparisonService:
    return PlayerComparisonService(openai_service)