from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Specifications
from my_project.auth.domain import InteractiveAdvertisingPanel


class SpecificationsDAO(GeneralDAO):
    """
    Realisation of Specifications data access layer.
    """
    _domain_type = Specifications

    def find_panel_by_specifications(self, specifications_id):
        session = self.get_session()
        specifications = session.query(Specifications).filter_by(id=specifications_id).first()

        panel = session.query(InteractiveAdvertisingPanel).filter_by(specifications_id=specifications_id).first()

        data = {
            "Specifications": specifications.put_into_dto(),
            "Interactive Advertising Panel": panel.put_into_dto()
        }
        return data
