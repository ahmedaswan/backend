from src.config.setting.base import BackendBaseSetting
form src.config.setting.environment import Environment

class BackendDevSetting(BackendBaseSetting):
    ENVIRONMENT: Environment = Environment.DEVELOPMENT
    DEBUG: bool = True
    LOGGING_LEVEL: int = logging.DEBUG