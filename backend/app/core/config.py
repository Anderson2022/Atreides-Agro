from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "atreides-agro-api"
    app_env: str = "production"
    log_level: str = "INFO"
    database_url: str | None = None

    model_config = SettingsConfigDict(env_file=None, extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
