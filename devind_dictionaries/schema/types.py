"""Describe dictionaries types."""

import datetime
from typing import Optional
import strawberry
from strawberry import auto
from strawberry_django_plus import gql
from devind_dictionaries.models import (
    BudgetClassification,
    Department,
    District,
    Region,
    Organization
)


class BaseTimeStamps:
    """Base of timeStamps class."""
    created_at: datetime.datetime
    updated_at: datetime.datetime


@gql.django.filter(BudgetClassification)
class BudgetClassificationFilter:
    """Filter of Budget classification."""

    id: gql.ID
    code: auto


@gql.django.type(BudgetClassification, filters=BudgetClassificationFilter)
class BudgetClassificationType(BaseTimeStamps, gql.relay.Node):
    """Type of Budget classification."""

    id: gql.ID
    code: auto
    name: auto

    active: auto
    start: auto
    end: auto


@gql.django.type(Department)
class DepartmentType(BaseTimeStamps):
    """Type of Departments."""

    id: gql.ID
    name: auto
    code: auto

    # user: 'UserType'
    # users: list['UserType']
    # minister: 'UserType'

    # @gql.django.field#(only=['users'])
    # def users(self, root: Department) -> 'list[UserType]':
    #     """Resolve function for users in Departments."""
    #     return root.users.all()

    @gql.django.field
    def organizations(self, root: Department) -> 'list[OrganizationType]':
        """Resolve function for organizations in Departments."""
        return root.organizations.all()


@gql.django.filter(District)
class DistrictFilter:
    """Filter of District."""

    name: auto


@gql.django.type(District, filters=DistrictFilter)
class DistrictType(BaseTimeStamps):
    """Type of District."""

    id: gql.ID
    name: auto

    @gql.django.field#(only='region_set')
    def regions(self, root: District) -> 'list[RegionType]':
        """Resolve function for Regions in District."""
        return root.region_set.all()


@gql.django.filter(Region)
class RegionFilter:
    """Type of Region."""

    name: auto
    common_id: auto


@gql.django.type(Region, filters=RegionFilter)
class RegionType(BaseTimeStamps):
    """Type of Region."""

    id: gql.ID
    name: auto
    common_id: auto

    district: DistrictType


@gql.django.filter(Organization)
class OrganizationFilter:
    """Filter of Organization."""

    name: auto
    present_name: auto

    inn: auto
    kpp: auto
    kind: auto

    rubpnubp: auto
    kodbuhg: auto
    okpo: auto

    phone: auto
    site: auto
    mail: auto
    address: auto

    # attributes: auto

    parent: 'OrganizationFilter | None'
    region: RegionFilter | None

    # user: 'UserType'
    # users: list['UserType']


@gql.django.type(Organization, filters=OrganizationFilter)
class OrganizationType(BaseTimeStamps, gql.relay.Node):
    """Type of Organization."""

    id: gql.ID
    name: auto
    present_name: auto

    inn: auto
    kpp: auto
    kind: auto

    rubpnubp: auto
    kodbuhg: auto
    okpo: auto

    phone: auto
    site: auto
    mail: auto
    address: auto

    attributes: strawberry.scalars.JSON

    parent: 'OrganizationType | None'
    region: RegionType | None

    # user: 'UserType'
    # users: list['UserType']



