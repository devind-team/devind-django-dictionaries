"""Describe dictionaries types."""

import datetime
from typing import Optional
import strawberry
from strawberry import auto
import strawberry_django
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


@strawberry_django.type(BudgetClassification)
class BudgetClassificationType(BaseTimeStamps):
    """Type of Budget classification."""

    id: auto
    code: str
    name: str

    active: bool
    start: datetime.datetime
    end: datetime.datetime


@strawberry_django.type(District)
class DistrictType(BaseTimeStamps):
    """Type of District."""

    id: auto
    name: str


@strawberry_django.type(Region)
class RegionType(BaseTimeStamps):
    """Type of Region."""

    id: auto
    name: str
    common_id: int

    district: DistrictType


@strawberry_django.type(Organization)
class OrganizationType(BaseTimeStamps):
    """Type of Organization."""

    id: auto
    name: str
    present_name: str

    inn: Optional[str]
    kpp: Optional[str]
    kind: Optional[str]

    rubpnubp: Optional[str]
    kodbuhg: Optional[str]
    okpo: Optional[str]

    phone: Optional[str]
    site: Optional[str]
    mail: Optional[str]
    address: Optional[str]

    attributes: strawberry.scalars.JSON

    parent: Optional['OrganizationType']
    region: Optional[RegionType]

    # user: 'UserType'
    # users: list['UserType']


@strawberry_django.type(Department)
class DepartmentType(BaseTimeStamps):
    """Type of Departments."""

    id: auto
    name: str
    code: int

    # user: 'UserType'
    # users: list['UserType']
    # minister: 'UserType'
    organizations: list['OrganizationType']
