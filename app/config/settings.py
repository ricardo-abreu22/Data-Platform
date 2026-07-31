from pydantic_settings import BaseSettings, SettingsConfigDict
from app.config.enums import Environment

class Settings(BaseSettings):
    app_name: str = "Data Platform" # O Pydantic não se preocupa se no .env as vars tão upper or lower, fica tudo lower
    environment: Environment = Environment.DEVELOPMENT # default é development a não ser que uma env variable faça override

    source_url: str
    output_dir: str = "data/raw"
    output_file: str = "users.json"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )