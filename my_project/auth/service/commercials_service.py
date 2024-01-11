from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import commercials_dao


class CommercialsService(GeneralService):
    _dao = commercials_dao

    def get_panel_for_commercials(self, commercials_id: int):
        return self._dao.get_panel_for_commercials(commercials_id)
