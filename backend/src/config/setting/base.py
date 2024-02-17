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

    