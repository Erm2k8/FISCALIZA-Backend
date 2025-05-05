import secrets
from typing import Annotated, Any, Literal
from pydantic_settings import BaseSettings, SettingsConfigDict

from pydantic import (
    AnyUrl,
    BeforeValidator,
    computed_field,
)

def parse_cors(v: any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(f"CORS PARSE: Invalid value: {v}")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_ignore_empty=True,
        extra="ignore",
    )

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = ""    # TODO generate the secret key
    
    # 60 minutes * 24 hours * 7 days = 7 days = 1 week
    ACESS_TOKEN_EXPIRES: int = 60 * 24 * 7
    FRONTEND_HOST: str = ""

    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    @computed_field
    @property
    def all_cors_origins(self) -> list[str]:
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGINS] + [
            self.FRONTEND_HOST
        ]
    
    PROJECT_NAME: str = ""
    DATABASE_SERVER: str = ""
    DATABASE_PORT:int = 1234
    DATABASE_PASSWORD: str = ""


settings = Settings() # type: ignore



