from src.config.setting.base import BackendBaseSetting
from src.config.setting.environment import Environment

class BackendProdSetting(BackendBaseSetting):
    ENVIRONMENT: Environment = Environment.PRODUCTION
    DESCRIPTION: str|None = "Backend FastAPI Application - PRODUCTION"