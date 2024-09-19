from abc import ABC, abstractmethod
from typing import Any
from app.models.entities.fpl_data import FPLData

class IFplApiService(ABC):
    @abstractmethod
    async def get_bootstrap_static(self) -> FPLData:
        pass
