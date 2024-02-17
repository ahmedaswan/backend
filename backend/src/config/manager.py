from functools import lru_cache

import decouple

from src.config.setting.base import BackendBaseSetting
from src.config.setting.development import BackendDevSetting
from src.config.setting.production import BackendProdSetting
from src.config.setting.staging import BackendStagingSetting
from src.config.setting.environment import Environment

class BackendSettingManager:
    def __init__(self, environment: str ):
        self.environment = environment
    
    def __call__(self) -> BackendBaseSetting:
        if self.environment == Environment.DEVELOPMENT.value:
            return BackendDevSetting()
        elif self.environment == Environment.STAGING.value:
            return BackendStagingSetting()
        elif self.environment == Environment.PRODUCTION.value:
            return BackendProdSetting()
        else:
            raise ValueError('Invalid environment')

@lru_cache()
def get_setting() -> BackendBaseSetting:
    return BackendSettingManager(environment=decouple.config('ENVIRONMENT', default='DEV', cast=str))



settings : BackendBaseSetting = get_setting()

print(settings)