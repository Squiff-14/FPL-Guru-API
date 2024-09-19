# player_comparison_router.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.requests.player_comparison_request import PlayerComparisonRequest
from app.services.interfaces.player_comparison_service_interface import IPlayerComparisonService
from app.services.player_comparison_service import IPlayerComparisonService
from app.di import get_player_comparison_service

router = APIRouter()

@router.post("/compare-players")
async def compare_players(
    request: PlayerComparisonRequest,
    player_comparison_service: IPlayerComparisonService = Depends(get_player_comparison_service)
):
    try:
        result = await player_comparison_service.compare_players(
            player=request.player,
            otherPlayers=request.other_players
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))