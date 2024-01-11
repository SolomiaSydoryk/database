from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import specifications_dao


class SpecificationsService(GeneralService):
    _dao = specifications_dao

    def find_panel_by_specifications(self, specifications_id):
        return self._dao.find_panel_by_specifications(specifications_id)
