

import graphene
from typing import cast
from graphene_django.debug import DjangoDebug

import devind_dictionaries.schema


class Query(
    devind_dictionaries.schema.Query,
    graphene.ObjectType
):
    debug = graphene.Field(DjangoDebug, name='__debug')


class Mutation(
    devind_dictionaries.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=cast(graphene.ObjectType, Query), mutation=Mutation)
