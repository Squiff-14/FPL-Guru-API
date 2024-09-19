from fastapi import APIRouter, Depends
from app.services.interfaces.fplapi_service_interface import IFplApiService
from app.services.fplapi_service import FplApiService  # assuming this is your implementation

router = APIRouter()

# Dependency injection function
def get_fpl_service() -> IFplApiService:
    return FplApiService()

@router.get("/bootstrap-static")
async def get_bootstrap_static(fpl_service: IFplApiService = Depends(get_fpl_service)):
    return await fpl_service.get_bootstrap_static()
