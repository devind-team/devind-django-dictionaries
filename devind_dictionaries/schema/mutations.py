from strawberry_django_plus import gql
from devind_dictionaries.permissions import ChangeDistrict, ChangeOrganization, ChangeRegion
from ..tasks import update_organizations
from .types import OrganizationType


@gql.type
class UpdateOrganizations:
    """For start celery task which updated districts, regions and organizations."""
    @gql.mutation(directives=[ChangeDistrict, ChangeOrganization, ChangeRegion])
    def update_organization(self) -> bool:
        """Start celery task."""
        update_organizations.delay()
        return True
