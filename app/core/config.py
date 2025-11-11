from pydantyc_settings import BaseSettings 

class Settings(BaseSettings):
    PROJECT_NAME:   str = "Mi Mecanica Run Run"
    DATABASE_URL:  str 
    SECRET_KEY: str
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    settings = Settings()
    
