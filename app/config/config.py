from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CRUD API"
    database_uri: str = ""

    model_config = SettingsConfigDict(env_file=".env")
