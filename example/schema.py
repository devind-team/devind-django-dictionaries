from django.contrib.auth import get_user_model
from strawberry import auto, Schema
from strawberry_django_plus import gql
from strawberry_django_plus.directives import SchemaDirectiveExtension
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

from devind_dictionaries.schema import Query, Mutation


@gql.django.type(get_user_model())
class UserType:
    id: gql.ID
    username: auto
    last_name: auto
    email: auto
    is_active: auto


schema = Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
        SchemaDirectiveExtension
    ]
)
