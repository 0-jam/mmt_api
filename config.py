from pydantic import BaseSettings


class Settings(BaseSettings):
    mc_model_path: str

    class Config:
        env_file = '.env'
