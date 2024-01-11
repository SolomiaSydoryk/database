from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import section_dao


class SectionService(GeneralService):
    _dao = section_dao

    def find_panel_by_section(self, section_id):
        return self._dao.find_panel_by_section(section_id)
