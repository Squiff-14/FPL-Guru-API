from abc import ABC, abstractmethod

class IOpenAIService(ABC):
    @abstractmethod
    async def analyze_data(self, data: dict, prompt: str = None, schema: str = None) -> str:
        pass