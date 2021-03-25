import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from modules.mcmodel import MCModel
import config


def get_settings():
    return config.Settings()


settings = get_settings()

mc_model = MCModel()
mc_model.load_model(settings.mc_model_path)


class Query(graphene.ObjectType):
    markovify = graphene.String()

    def resolve_markovify(self, info):
        return mc_model.generate_sentence()


app = FastAPI()
app.add_route('/', GraphQLApp(schema=graphene.Schema(query=Query)))
