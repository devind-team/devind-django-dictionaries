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


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
        SchemaDirectiveExtension
    ]
)
