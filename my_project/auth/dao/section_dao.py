from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Section, InteractiveAdvertisingPanel


class SectionDAO(GeneralDAO):
    """
    Realisation of Section data access layer.
    """
    _domain_type = Section

    def find_panel_by_section(self, section_id):
        session = self.get_session()
        panel = session.query(InteractiveAdvertisingPanel).filter_by(section_id=section_id).first()
        section = session.query(Section).filter_by(id=section_id).first()
        data = {"Section": section.put_into_dto(),
                "Interactive Advertising Panel": panel.put_into_dto()}
        return data

