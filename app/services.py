from openai import OpenAI
from fastapi import HTTPException
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)
def query_openai(prompt: str) -> str:
    """Send a query to the OpenAI API and return the response as text."""
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to contact OpenAI: {str(e)}")
