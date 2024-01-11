from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Owner


class OwnerDAO(GeneralDAO):
    """
    Realisation of Owner data access layer.
    """
    _domain_type = Owner
