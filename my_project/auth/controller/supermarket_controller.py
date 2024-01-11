from my_project.auth.service import supermarket_service
from my_project.auth.controller.general_controller import GeneralController


class SupermarketController(GeneralController):
    """
    Realisation of Supermarket controller.
    """
    _service = supermarket_service

    def get_address_for_supermarket(self, supermarket_id: int):
        return self._service.get_address_for_supermarket(supermarket_id)

    def get_manufacturers_for_supermarket(self, supermarket_id: int):
        return self._service.get_manufacturers_for_supermarket(supermarket_id)

    def connect_manufacturer_and_supermarket_from_supermarket(self, manufacturer_id: int, supermarket_id: int):
        return self._service.connect_manufacturer_and_supermarket_from_supermarket(manufacturer_id, supermarket_id)

    def insert_in_supermarket_has_manufacturer_by_values(self, manufacturer_name, supermarket_name):
        return self._service.insert_in_supermarket_has_manufacturer_by_values(manufacturer_name, supermarket_name)

    def remove_manufacturer_from_supermarket(self, manufacturer_id: int, supermarket_id: int):
        return self._service.remove_manufacturer_from_supermarket(manufacturer_id, supermarket_id)
