import logging
from redis import Redis
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from app.routers import fplapi_router, team_router, player_router
from app.services.fplapi_service import FplApiService
from app.services.team_service import TeamService
from app.services.player_service import PlayerService
from app.services.interfaces.fplapi_service_interface import IFplApiService
from app.services.interfaces.team_service_interface import ITeamService
from app.services.interfaces.player_service_interface import IPlayerService

# Set up Redis for caching during app lifespan
async def lifespan(app: FastAPI):
    redis = Redis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fpl_cache")
    yield  # Yield control to FastAPI
    # Optionally, add shutdown logic here
    

# Configure logging (you can set the level, format, and file location here)
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()])


# Initialize the FastAPI app with the lifespan context
app = FastAPI(lifespan=lifespan)

# Dependency override to bind interfaces to implementations
# Instead of using a lambda, pass the class directly
app.dependency_overrides[IFplApiService] = FplApiService
app.dependency_overrides[ITeamService] = TeamService
app.dependency_overrides[IPlayerService] = PlayerService

# Register the routers
app.include_router(fplapi_router.router)
app.include_router(team_router.router)
app.include_router(player_router.router)
