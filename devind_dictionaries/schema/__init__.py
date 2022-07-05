"""Description for dictionaries schema."""


from .types import RegionType, \
    DistrictType, \
    OrganizationType, \
    DepartmentType, \
    BudgetClassificationType
from .filters import BudgetClassificationFilter
from strawberry_django_plus import gql
from .mutations import UpdateOrganizations


@gql.type
class Query:
    """List of queries for dictionaries."""

    budget_classifications: BudgetClassificationType = gql.django.field(filters=BudgetClassificationFilter)
    active_budget_classifications: BudgetClassificationType = gql.django.field(filters=BudgetClassificationFilter)

    department: DepartmentType = gql.django.field()
    departments: list[DepartmentType] = gql.django.field()

    district: DistrictType = gql.django.field()
    districts: list[DistrictType] = gql.django.field()

    region: RegionType = gql.django.field()
    regions: list[RegionType] = gql.django.field()

    organization: OrganizationType = gql.django.field()
    organizations: list[OrganizationType] = gql.django.field()


@gql.type
class Mutation(UpdateOrganizations):
    """List of mutations for dictionaries."""
    pass

