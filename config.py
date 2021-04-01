from pydantic import BaseSettings


class Settings(BaseSettings):
    mc_model_path: str

    class Config:
        env_file = '.env'

    def get_mc_model(self, index):
        return self.mc_model_path.split(' ')[index]
