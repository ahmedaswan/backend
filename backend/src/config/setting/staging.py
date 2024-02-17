from src.config.setting.base import BackendBaseSetting
from src.config.setting.environment import Environment

class BackendStagingSetting(BackendBaseSetting):
    DESCRIPTION: str|None = "Backend FastAPI Application - STAGING"
    ENVIRONMENT: Environment = Environment.STAGING
    DEBUG: bool = True

