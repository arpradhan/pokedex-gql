import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from pokedex.db import tables


class Pokemon(SQLAlchemyObjectType):

    class Meta:
        model = tables.Pokemon
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    all_pokemon = SQLAlchemyConnectionField(Pokemon)


schema = graphene.Schema(query=Query)