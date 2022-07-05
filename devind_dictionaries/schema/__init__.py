"""Description for dictionaries schema."""


from .types import RegionType, \
    DistrictType, \
    OrganizationType, \
    DepartmentType, \
    BudgetClassificationType, \
    BudgetClassificationFilter
from typing import List, Optional
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

    # @staticmethod
    # def resolve_active_budget_classifications(
    #         root: Any,
    #         info: ResolveInfo,
    #         *args,
    #         **kwargs
    # ) -> Iterable[BudgetClassification]:
    #     """Resolve active budget classification for now."""
    #     return BudgetClassification.objects.active_now()
    #
    # @staticmethod
    # def resolve_department(root: Any, info: ResolveInfo, department_id: int) -> Department:
    #     """Resolve function for get department entity."""
    #
    # @staticmethod
    # def resolve_district(root: Any, info: ResolveInfo, district_id: int) -> District:
    #     """Resolve function for get district entity."""
    #     return get_object_or_404(District, pk=district_id)
    #
    # @staticmethod
    # def resolve_region(root: Any, info: ResolveInfo, region_id: int) -> Region:
    #     """Resolve function for get region entity."""
    #     return get_object_or_404(Region, pk=region_id)
    #
    # @staticmethod
    # def resolve_organization(root: Any, info: ResolveInfo, organization_id: int) -> Organization:
    #     """Resolve function for get organizations entity."""
    #     return get_object_or_404(Organization, pk=organization_id)


@gql.type
class Mutation(UpdateOrganizations):
    """List of mutations for dictionaries."""
    pass

