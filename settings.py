import os
from dotenv import load_dotenv


class Settings:
    load_dotenv()

    user_id = os.getenv('USER_ID')
    user_secret_key = os.getenv('USER_SECRET_KEY')


settings = Settings()
