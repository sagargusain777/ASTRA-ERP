
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env = "DEV"
    OPENAI_API_KEY:str | None = None
    GEMINI_API_KEY:str | None = None
    #JWT
    JWT_SECRET_KEY:str = 'my-secret'
    JWT_ALGORITHM:str = "HS256"
    #Qdrant Vector Database
    QDRANT_API_KEY:str|None = None
    QDRANT_COLLECTION_NAME:str|None = None

    model_config = SettingsConfigDict(
        env_file = '.env',
        case_sensitive = False
    )
# Create a single settings instance — import this everywhere
settings = Settings()

"""
📘 STEP 1: Configuration (config.py)
=====================================
WHY THIS FILE?
- Every production app needs a single place to manage settings (DB URL, secrets, etc.)
- We use Pydantic's BaseSettings to automatically read from environment variables or .env file
- This means you NEVER hardcode secrets in your code

HOW IT WORKS:
- BaseSettings reads environment variables matching the field names
- model_config tells it to also check a .env file
- You create ONE instance (settings) and import it everywhere
"""


