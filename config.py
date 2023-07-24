from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_password :str 
    database_hostname :str 
    database_name :str
    database_username :str 
    secret_key :str 
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".var_env"

settings = Settings()