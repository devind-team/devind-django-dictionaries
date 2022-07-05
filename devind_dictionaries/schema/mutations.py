from strawberry_django_plus import gql
from strawberry_django_plus.permissions import HasPerm
from ..tasks import update_organizations


@gql.type
class UpdateOrganizations:
    """For start celery task which updated districts, regions and organizations."""
    @gql.mutation(directives=[
        HasPerm('devind_dictionaries.change_district'),
        HasPerm('devind_dictionaries.change_region'),
        HasPerm('devind_dictionaries.change_organization'),
    ])
    def update_organization(self) -> bool:
        """Start celery task."""
        update_organizations.delay()
        return True
