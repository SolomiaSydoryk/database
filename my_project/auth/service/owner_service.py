from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import owner_dao


class OwnerService(GeneralService):
    _dao = owner_dao
