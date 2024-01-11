from my_project.auth.service import address_service
from my_project.auth.controller.general_controller import GeneralController


class AddressController(GeneralController):
    """
    Realisation of Address controller.
    """
    _service = address_service

    def find_supermarket_by_adress(self, address_id):
        return self._service.find_supermarket_by_adress(address_id)
