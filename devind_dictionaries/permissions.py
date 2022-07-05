"""Module define permission in dictionaries."""

from strawberry_django_plus.permissions import HasPerm


ChangeDistrict = HasPerm('devind_dictionaries.change_district')
ChangeRegion = HasPerm('devind_dictionaries.change_region')
ChangeOrganization = HasPerm('devind_dictionaries.change_organization')

# from devind_helpers.permissions import ModelPermission
#
#
# ChangeDistrict = ModelPermission('devind_dictionaries.change_district')
# ChangeRegion = ModelPermission('devind_dictionaries.change_region')
# ChangeOrganization = ModelPermission('devind_dictionaries.change_organization')
