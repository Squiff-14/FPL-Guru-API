from fastapi import APIRouter, Depends
from app.services.interfaces.team_service_interface import ITeamService
from typing import List
from app.di import get_team_service
from app.models.entities.team import Team

router = APIRouter()

@router.get("/teams")
async def get_bootstrap_static(team_service: ITeamService = Depends(get_team_service)) -> List[Team]:
    return await team_service.get_all_teams()

@router.get("/teams/{team_id}")
async def get_team(team_id: int, team_service: ITeamService = Depends(get_team_service)) -> Team:
    return await team_service.get_team(team_id)