from my_project.auth.service import manufacturer_service
from my_project.auth.controller.general_controller import GeneralController


class ManufacturerController(GeneralController):
    """
    Realisation of Manufacturer controller.
    """
    _service = manufacturer_service

    def get_supermarkets_for_manufacturer(self, manufacturer_id: int):
        return self._service.get_supermarkets_for_manufacturer(manufacturer_id)

    def connect_manufacturer_and_supermarket_from_manufacturer(self, manufacturer_id: int, supermarket_id: int):
        return self._service.connect_manufacturer_and_supermarket_from_manufacturer(manufacturer_id, supermarket_id)

    def insert_in_supermarket_has_manufacturer_by_values(self, manufacturer_name, supermarket_name):
        return self._service.insert_in_supermarket_has_manufacturer_by_values(manufacturer_name, supermarket_name)

    def remove_supermarket_from_manufacturer(self, manufacturer_id: int, supermarket_id: int):
        return self._service.remove_supermarket_from_manufacturer(manufacturer_id, supermarket_id)
