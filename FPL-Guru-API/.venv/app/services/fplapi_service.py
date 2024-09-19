import httpx
from typing import List
from app.models.entities.fpl_data import FPLData
from app.models.entities.team import Team
from fastapi_cache.decorator import cache
from app.services.interfaces.fplapi_service_interface import IFplApiService  

FPL_BASE_URL = "https://fantasy.premierleague.com/api"

class FplApiService(IFplApiService):
    
    @cache(expire=300)
    async def get_bootstrap_static(self) -> FPLData:
        async with httpx.AsyncClient() as client:
            url = f"{FPL_BASE_URL}/bootstrap-static/"
            response = await client.get(url)
            response_data = response.json()
            return response_data
