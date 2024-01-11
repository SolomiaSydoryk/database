from my_project.auth.service import interactive_advertising_panel_service
from my_project.auth.controller.general_controller import GeneralController


class InteractiveAdvertisingPanelController(GeneralController):
    """
    Realisation of Interactive advertising panel controller.
    """
    _service = interactive_advertising_panel_service

    def get_commercials_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        return self._service.get_commercials_for_interactive_advertising_panel(interactive_advertising_panel_id)

    def get_specifications_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        return self._service.get_specifications_for_interactive_advertising_panel(interactive_advertising_panel_id)

    def get_sections_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        return self._service.get_sections_for_interactive_advertising_panel(interactive_advertising_panel_id)

    def connect_commercial_and_panel_from_interactive_advertising_panel(self, commercial_id: int,
                                                                        interactive_advertising_panel_id: int):
        return (self._service.connect_commercial_and_panel_from_interactive_advertising_panel
                (commercial_id, interactive_advertising_panel_id))

    def add_commercials_to_interactive_advertising_panel(self, commercials_id: int,
                                                         interactive_advertising_panel_id: int):
        self._service.add_commercials_to_interactive_advertising_panel(commercials_id, interactive_advertising_panel_id)

    def remove_commercials_from_interactive_advertising_panel(self, commercials_id: int,
                                                              interactive_advertising_panel_id: int):
        self._service.remove_commercials_from_interactive_advertising_panel(commercials_id,
                                                                            interactive_advertising_panel_id)
