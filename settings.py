import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    service_name: str
    prod: bool = False
    test: bool = False

    user_id: int = 1
    user_secret_key: str = ""

    logging_level: int = 10


settings = Settings(
    _env_file=os.path.join(os.getcwd(), '.env'),
    _env_file_encoding='utf-8',
)