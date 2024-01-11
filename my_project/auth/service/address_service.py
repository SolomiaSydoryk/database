from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import address_dao


class AddressService(GeneralService):
    _dao = address_dao

    def find_supermarket_by_adress(self, address_id):
        return self._dao.find_supermarket_by_adress(address_id)