from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import interactive_advertising_panel_dao


class InteractiveAdvertisingPanelService(GeneralService):
    _dao = interactive_advertising_panel_dao

    def get_commercials_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        return self._dao.get_commercials_for_interactive_advertising_panel(interactive_advertising_panel_id)

    def get_sections_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        return self._dao.get_sections_for_interactive_advertising_panel(interactive_advertising_panel_id)

    def get_specifications_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        return self._dao.get_specifications_for_interactive_advertising_panel(interactive_advertising_panel_id)

    def connect_commercials_and_panel_from_interactive_advertising_panel(self,
                                                                         commercials_id: int,
                                                                         interactive_advertising_panel_id: int):
        self._dao.connect_commercials_and_panel_from_interactive_advertising_panel(
            commercials_id, interactive_advertising_panel_id)

    def remove_commercials_from_interactive_advertising_panel(self, commercials_id: int,
                                                              interactive_advertising_panel_id: int):
        self._dao.remove_commercials_from_interactive_advertising_panel(commercials_id,
                                                                        interactive_advertising_panel_id)
