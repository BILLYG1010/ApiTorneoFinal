import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv(override=True)

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    
    # Configuración de CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:4200").split(",")
    
    @property
    def access_token_expire(self):
        return timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)

settings = Settings()