

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
