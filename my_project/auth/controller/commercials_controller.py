from my_project.auth.service import commercials_service
from my_project.auth.controller.general_controller import GeneralController


class CommercialsController(GeneralController):
    """
    Realisation of Commercials controller.
    """
    _service = commercials_service


def get_panel_for_commercials(self, commercials_id: int):
    return self._service.get_panel_for_commercials(commercials_id)


def connect_commercials_and_panel_from_commercials(self, commercials_id: int, panel_id: int):
    return self._service.connect_commercials_and_panel_from_commercials(commercials_id, panel_id)


def add_interactive_advertising_panel_to_commercials(self, interactive_advertising_panel_id: int, commercials_id: int):
    self._service.add_interactive_advertising_panel_to_commercials(interactive_advertising_panel_id, commercials_id)


def remove_interactive_advertising_panel_from_commercials(self, interactive_advertising_panel_id: int,
                                                          commercials_id: int):
    self._service.remove_interactive_advertising_panel_from_commercials(interactive_advertising_panel_id,
                                                                        commercials_id)