import strawberry
import strawberry_django
from django.contrib.auth import get_user_model
from strawberry import auto
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from strawberry_django_plus.directives import SchemaDirectiveExtension
from strawberry_django_plus import gql

from devind_dictionaries.schema import Query, Mutation


@strawberry_django.type(get_user_model())
class UserType:
    id: gql.ID
    username: auto
    last_name: auto
    email: auto
    is_active: auto


schema = strawberry.Schema(query=Query,
                           mutation=Mutation,
                           extensions=[DjangoOptimizerExtension, SchemaDirectiveExtension])
# import graphene
# from typing import cast
#
# from graphene_django import DjangoObjectType
# from graphene_django.debug import DjangoDebug
# from django.contrib.auth import get_user_model
#
# import devind_dictionaries.schema
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username', 'last_name', 'email', 'is_active',)
#
#
# class Query(
#     devind_dictionaries.schema.Query,
#     graphene.ObjectType
# ):
#     debug = graphene.Field(DjangoDebug, name='__debug')
#
#
# class Mutation(
#     devind_dictionaries.schema.Mutation,
#     graphene.ObjectType
# ):
#     pass
#
#
# schema = graphene.Schema(query=cast(graphene.ObjectType, Query), mutation=Mutation)
