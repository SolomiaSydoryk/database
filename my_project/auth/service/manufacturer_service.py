from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import manufacturer_dao


class ManufacturerService(GeneralService):
    _dao = manufacturer_dao

    def get_supermarkets_for_manufacturer(self, manufacturer_id: int):
        return self._dao.get_supermarkets_for_manufacturer(manufacturer_id)

    def connect_manufacturer_and_supermarket_from_manufacturer(self, manufacturer_id: int, supermarket_id: int):
        return self._dao.connect_manufacturer_and_supermarket_from_manufacturer(manufacturer_id, supermarket_id)

    def insert_in_supermarket_has_manufacturer_by_values(self, manufacturer_name, supermarket_name):
        return self._dao.insert_in_supermarket_has_manufacturer_by_values(manufacturer_name, supermarket_name)

    def remove_supermarket_from_manufacturer(self, manufacturer_id: int, supermarket_id: int):
        return self._dao.remove_supermarket_from_manufacturer(manufacturer_id, supermarket_id)
