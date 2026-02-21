
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    env = "DEV"
    OPENAI_API_KEY:str | None = None
    GEMINI_API_KEY:str | None = None
    #JWT
    JWT_SECRET_KEY:str = 'my-secret'
    JWT_ALGORITHM:str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRES_MINUTES:int | None = None
    #Qdrant Vector Database
    QDRANT_API_KEY:str | None = None
    QDRANT_COLLECTION_NAME:str | None = None

    
    # Supabase
    SUPABASE_URL: str | None = None
    SUPABASE_KEY: str | None = None
    DATABASE_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file = '.env',
        case_sensitive = False
    )
# Create a single settings instance — import this everywhere
settings = Settings()




