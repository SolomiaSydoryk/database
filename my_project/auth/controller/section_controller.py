from my_project.auth.service import section_service
from my_project.auth.controller.general_controller import GeneralController


class SectionController(GeneralController):
    """
    Realisation of Section controller.
    """
    _service = section_service

    def find_panel_by_section(self, section_id):
        return self._service.find_panel_by_section(section_id)
