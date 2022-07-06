"""Describe dictionaries types."""

from __future__ import annotations

import datetime
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

from .filters import BudgetClassificationFilter
from .filters import DistrictFilter, RegionFilter, OrganizationFilter
from ..settings import dictionaries_settings


class BaseTimeStamps:
    """Base of timeStamps class."""
    created_at: datetime.datetime
    updated_at: datetime.datetime


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

    # user: dictionaries_settings.USER_TYPE | None
    # minister: dictionaries_settings.USER_TYPE | None
    #
    # @gql.django.field  # (only=['users'])
    # def users(self, root: Department) -> 'list[dictionaries_settings.USER_TYPE]':
    #     """Resolve function for users in Departments."""
    #     return root.users.all()

    @gql.django.field
    def organizations(self, root: Department) -> 'list[OrganizationType]':
        """Resolve function for organizations in Departments."""
        return root.organizations.all()


@gql.django.type(District, filters=DistrictFilter)
class DistrictType(BaseTimeStamps):
    """Type of District."""

    id: gql.ID
    name: auto

    @gql.django.field   # (only='region_set')
    def regions(self, root: District) -> 'list[RegionType]':
        """Resolve function for Regions in District."""
        return root.region_set.all()


@gql.django.type(Region, filters=RegionFilter)
class RegionType(BaseTimeStamps):
    """Type of Region."""

    id: gql.ID
    name: auto
    common_id: auto

    district: DistrictType | None


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

    # user: dictionaries_settings.USER_TYPE
    #
    # @gql.django.field  # (only=['users'])
    # def users(self, root: Organization) -> 'list[dictionaries_settings.USER_TYPE]':
    #     """Resolve function for users in Departments."""
    #     return root.users.all()


