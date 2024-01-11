from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import supermarket_dao


class SupermarketService(GeneralService):
    _dao = supermarket_dao

    def get_address_for_supermarket(self, supermarket_id: int):
        return self._dao.get_address_for_supermarket(supermarket_id)

    def get_manufacturers_for_supermarket(self, supermarket_id: int):
        return self._dao.get_manufacturers_for_supermarket(supermarket_id)

    def connect_manufacturer_and_supermarket_from_supermarket(self, manufacturer_id: int, supermarket_id: int):
        return self._dao.connect_manufacturer_and_supermarket_from_supermarket(manufacturer_id, supermarket_id)

    def insert_in_supermarket_has_manufacturer_by_values(self, manufacturer_name, supermarket_name):
        return self._dao.insert_in_supermarket_has_manufacturer_by_values(manufacturer_name, supermarket_name)

    def remove_manufacturer_from_supermarket(self, manufacturer_id: int, supermarket_id: int):
        return self._dao.remove_manufacturer_from_supermarket(manufacturer_id, supermarket_id)
