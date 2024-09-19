import openai
import logging
from app.services.interfaces.openai_service_interace import IOpenAIService

class OpenAIService(IOpenAIService):
    def __init__(self):
        self.client = openai.OpenAI(api_key="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")

    async def analyze_data(self, data: dict, schema: str = None) -> str:
        try:
            logging.debug("Schema provided: %s", schema)

            # Provide a structured prompt to OpenAI, including the schema
            prompt = f"""
                Given the following player data in JSON format and a list of alternative players, 
                compare the player with each alternative based on their performance and cost.
                Consider key attributes such as points per game, goals scored, assists, influence, creativity, 
                threat, and overall cost-effectiveness. 

                Respond according to this JSON schema:
                {schema}

                Data: {data}
            """
            
            # Log the final prompt before sending the request
            logging.debug("Final prompt being sent to OpenAI: %s", prompt)

            response = self.client.chat.completions.create(
                model="gpt-4", 
                messages=[
                    {"role": "system", "content": "You are an expert in player comparison."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000
            )
            
            
            logging.debug("Received response from OpenAI: %s", response)

            # return response.choices[0].message['content'].strip()
        
        except Exception as e:
            # Log any errors that occur during the OpenAI request
            logging.error("Error occurred while calling OpenAI: %s", e, exc_info=True)
            raise
