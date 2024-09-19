from typing import List, Optional
from fastapi_cache.decorator import cache
from app.models.entities.player import Player
from app.models.filters.player_filter import PlayerFilter
from app.services.interfaces.fplapi_service_interface import IFplApiService

class PlayerService:
    
    def __init__(self, fplapi_service: IFplApiService):
        self.fplapi_service = fplapi_service

    @cache(expire=300)
    async def get_all_players(self, player_filter: Optional[PlayerFilter] = None) -> List[Player]:
        # Use the fplapi_service directly to get players
        data = await self.fplapi_service.get_bootstrap_static()
        players = data.get("elements", [])
        
        # Apply filters if player_filter is provided
        if player_filter:
            players = [
                player for player in players
                if all([
                    player_filter.id is None or player["id"] == player_filter.id,
                    player_filter.team is None or player["team"] == player_filter.team,
                    player_filter.first_name is None or player_filter.first_name.lower() in player["first_name"].lower(),
                    player_filter.second_name is None or player_filter.second_name.lower() in player["second_name"].lower()
                ])
            ]

        return players

    @cache(expire=300)
    async def get_player(self, player_id: int) -> Player:
        # Use the fplapi_service directly
        data = await self.fplapi_service.get_bootstrap_static()
        players = data.get("elements", [])
        player = next((player for player in players if player["id"] == player_id), None)
        return player
