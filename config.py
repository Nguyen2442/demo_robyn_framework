from typing import Optional, List, Union, Tuple
from pydantic import BaseSettings
import os


class AppEnvConfig(BaseSettings):
    APP_DB_MONGO_URI: Optional[str] = None
    APP_DB_MONGO_NAME: Optional[str] = None

    class Config:
        case_sensitive = True
        validate_assignment = True


settings = AppEnvConfig(_env_file=".env")

if __name__ == "__main":
    pass
