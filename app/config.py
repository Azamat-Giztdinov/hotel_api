from pydantic import field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URL: str | None = None
    SECRET_KEY : str
    ALGORITHM: str

    @field_validator("DATABASE_URL", mode="before")
    def get_database_url(cls, v, values):
        # Access the validated fields from values.data
        data = values.data
        if not all(k in data for k in ("DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME")):
            raise ValueError("Missing database configuration values")
        
        return f'postgresql+asyncpg://{data["DB_USER"]}:{data["DB_PASSWORD"]}@{data["DB_HOST"]}:{data["DB_PORT"]}/{data["DB_NAME"]}'

    class Config:
        env_file = '.env'


settings = Settings()
print(settings.DATABASE_URL)
