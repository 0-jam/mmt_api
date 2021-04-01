import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from modules.mcmodel import MCModel
import config


def get_settings():
    return config.Settings()


settings = get_settings()

mc_model = MCModel()


class Query(graphene.ObjectType):
    markovify = graphene.String(index=graphene.Int(default_value=0))

    def resolve_markovify(self, info, index):
        mc_model.load_model(settings.get_mc_model(index))

        return mc_model.generate_sentence()


app = FastAPI()
app.add_route('/', GraphQLApp(schema=graphene.Schema(query=Query)))
