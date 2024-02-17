import logging
import pathlib

import decouple

import pydantic
from pydantic_settings import BaseSettings

ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent.parent.resolve()
print(ROOT_DIR)
class BackendBaseSetting(BaseSettings):
    TITLE: str = "Backend FastAPI Application"
    VERSION: str = "0.1.0"
    TIMEZONE: str = "UTC"
    DESCRIPTION: str = "Backend FastAPI Application"
    DEBUG: bool = False

    SERVER_HOST: str = decouple.config("BACKEND_SERVER_HOST", cast=str)
    SERVER_PORT: int = decouple.config("BACKEND_SERVER_PORT", cast=int)
    SERVER_WORKERS: int = decouple.config("BACKEND_SERVER_WORKERS", cast=int)
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: str = "/redoc"
    OPENAPI_PREFIX: str = ""
    
    DB_POSTGRES_HOST: str = decouple.config("POSTGRES_HOST", cast=str)  # type: ignore
    DB_MAX_POOL_CON: int = decouple.config("DB_MAX_POOL_CON", cast=int)  # type: ignore
    DB_POSTGRES_NAME: str = decouple.config("POSTGRES_DB", cast=str)  # type: ignore
    DB_POSTGRES_PASSWORD: str = decouple.config("POSTGRES_PASSWORD", cast=str)  # type: ignore
    DB_POOL_SIZE: int = decouple.config("DB_POOL_SIZE", cast=int)  # type: ignore
    DB_POOL_OVERFLOW: int = decouple.config("DB_POOL_OVERFLOW", cast=int)  # type: ignore
    DB_POSTGRES_PORT: int = decouple.config("POSTGRES_PORT", cast=int)  # type: ignore
    DB_POSTGRES_SCHEMA: str = decouple.config("POSTGRES_SCHEMA", cast=str)  # type: ignore
    DB_TIMEOUT: int = decouple.config("DB_TIMEOUT", cast=int)  # type: ignore
    DB_POSTGRES_USERNAME: str = decouple.config("POSTGRES_USERNAME", cast=str)  # type: ignore

    IS_DB_ECHO_LOG: bool = decouple.config("IS_DB_ECHO_LOG", cast=bool)  # type: ignore
    IS_DB_FORCE_ROLLBACK: bool = decouple.config("IS_DB_FORCE_ROLLBACK", cast=bool)  # type: ignore
    IS_DB_EXPIRE_ON_COMMIT: bool = decouple.config("IS_DB_EXPIRE_ON_COMMIT", cast=bool)  # type: ignore


    LOGGING_LEVEL: int = logging.INFO
    LOGGERS: tuple[str,str] = ("uvicorn.asgi",  "uvicorn.access")

    class Config(pydantic.ConfigDict):
        env_file = ROOT_DIR / ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        validate_assignment = True
    
    @property
    def set_backend_app_attributes(self) -> dict:
        '''
        set all "FastAPI" class attributes with custom values defined in this "BackendBaseSetting" class
        '''
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "debug": self.DEBUG,
            "description": self.DESCRIPTION,
            "docs_url": self.DOCS_URL,
            "openapi_url": self.OPENAPI_URL,
            "redoc_url": self.REDOC_URL,
            "openapi_prefix": self.OPENAPI_PREFIX
        }

    