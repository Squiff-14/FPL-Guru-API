import logging
from typing import List
from app.models.entities.player import Player
from app.models.entities.player_comparison import PlayerComparisonResult
from app.services.interfaces.openai_service_interace import IOpenAIService
from app.services.interfaces.player_comparison_service_interface import IPlayerComparisonService


class PlayerComparisonService(IPlayerComparisonService):
    
    def __init__(self, openai_service: IOpenAIService):
        self.openai_service = openai_service

    async def compare_players(self, player: Player, otherPlayers: List[Player]) -> PlayerComparisonResult:
        # Prepare data for OpenAI
        data = {
            "player": player.dict(),  # Ensure the player data is serialized to dict
            "otherPlayers": [otherPlayer.dict() for otherPlayer in otherPlayers]  # Convert each Player instance to dict
        }
        
        # Generate JSON schema from Pydantic model
        schema = PlayerComparisonResult.model_json_schema()

        try:
            logging.debug(f"Schema for PlayerComparisonResult: {schema}")
            # Call OpenAI service to analyze data
            response = await self.openai_service.analyze_data(data, schema)

            # # Log the response from OpenAI for debugging
            # logging.debug(f"Response from OpenAI: {response}")

            # # Check if the response is None or not a valid dictionary
            # if response is None:
            #     raise ValueError("OpenAI returned no response (None). Please check your API or data.")
            
            # if not isinstance(response, dict):
            #     raise ValueError(f"Expected a dictionary but got {type(response)}. Response: {response}")
            
            # # Parse response from OpenAI
            # comparison_result = PlayerComparisonResult.model_validate(response)
        except Exception as e:
            logging.error(f"Error while validating response: {e}")
            raise ValueError(f"Validation error: {e}")

        return "comparison_result"
