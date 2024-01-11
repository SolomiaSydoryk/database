from my_project.auth.service import specifications_service
from my_project.auth.controller.general_controller import GeneralController


class SpecificationsController(GeneralController):
    """
    Realisation of Specification controller.
    """
    _service = specifications_service

    def find_panel_by_specifications(self, specifications_id):
        return self._service.find_panel_by_specifications(specifications_id)
