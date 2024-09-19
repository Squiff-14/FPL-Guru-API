from typing import Optional
from fastapi import APIRouter, Depends, Query
from app.services.interfaces.player_service_interface import IPlayerService
from app.di import get_player_service
from app.models.filters.player_filter import PlayerFilter

# Initialize the router
router = APIRouter()

# Endpoint to get all players
@router.get("/players")
async def get_players(
    player_service: IPlayerService = Depends(get_player_service),
    team: Optional[int] = Query(None),
    first_name: Optional[str] = Query(None),
    second_name: Optional[str] = Query(None),
    id: Optional[int] = Query(None)
):
    # Create a PlayerFilter instance using the query parameters
    player_filter = PlayerFilter(
        team=team,
        first_name=first_name,
        second_name=second_name,
        id=id
    )

    # Pass the filter to the service method
    return await player_service.get_all_players(player_filter)

# Endpoint to get a specific player by ID
@router.get("/players/{player_id}")
async def get_player(player_id: int, player_service: IPlayerService = Depends(get_player_service)):
    return await player_service.get_player(player_id=player_id)
