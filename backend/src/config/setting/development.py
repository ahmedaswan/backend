from src.config.setting.base import BackendBaseSetting
from src.config.setting.environment import Environment
import logging
class BackendDevSetting(BackendBaseSetting):
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
    DEBUG: bool = True
    LOGGING_LEVEL: int = logging.DEBUG