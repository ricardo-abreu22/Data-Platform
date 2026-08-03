from pydantic_settings import BaseSettings, SettingsConfigDict
from app.config.enums import Environment
from pydantic import computed_field # to make the URL avaiable for Pydantic. Now @property gets the value by running the function behind the scenes

class Settings(BaseSettings):
    app_name: str = "Data Platform" # O Pydantic não se preocupa se no .env as vars tão upper or lower, fica tudo lower
    environment: Environment = Environment.DEVELOPMENT # default é development a não ser que uma env variable faça override

    source_url: str
    output_dir: str = "data/raw"
    output_file: str = "users.json"

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str
    postgres_user: str
    postgres_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
