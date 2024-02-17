import enum

class Environment(str, enum.Enum):
    DEVELOPMENT = "DEV"
    STAGING = "STAG"
    PRODUCTION = "PROD"
