from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import InteractiveAdvertisingPanel

from my_project.auth.domain.interactive_advertising_panel import interactive_advertising_panel_has_commercials
from my_project.auth.domain.commercials import Commercials

from my_project.auth.domain.interactive_advertising_panel import supermarket_has_interactive_advertising_panel
from my_project.auth.domain.supermarket import Supermarket
from my_project.auth.domain.section import Section
from my_project.auth.domain.specifications import Specifications

from sqlalchemy.orm import joinedload


class InteractiveAdvertisingPanelDAO(GeneralDAO):
    """
    Realisation of InteractiveAdvertisingPanel data access layer.
    """
    _domain_type = InteractiveAdvertisingPanel

    def get_commercials_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        session = self.get_session()

        interactive_advertising_panel = session.query(InteractiveAdvertisingPanel).filter_by(
            id=interactive_advertising_panel_id).first()
        commercials_ids = (
            session.query(interactive_advertising_panel_has_commercials.c.commercials_id)
            .filter(
                interactive_advertising_panel_has_commercials.c.interactive_advertising_panel_id ==
                interactive_advertising_panel_id).all()
        )
        commercials_ids = [commercials_id for (commercials_id,) in commercials_ids]
        commercials = session.query(Commercials).filter(Commercials.id.in_(commercials_ids)).all()
        data = {
            "Interactive Advertising Panel": interactive_advertising_panel.put_into_dto(),
            "Commercials": [commercial.put_into_dto() for commercial in commercials]
        }
        return data

    def get_specification_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        session = self.get_session()
        specification_id = (session.query(InteractiveAdvertisingPanel).filter_by(id=interactive_advertising_panel_id)
                            .first().specification_id)
        specification = session.query(Specifications).filter_by(id=specification_id).first()
        interactive_advertising_panel = (session.query(InteractiveAdvertisingPanel)
                                         .filter_by(id=interactive_advertising_panel_id).first())
        return {"Interactive Advertising Panel": interactive_advertising_panel.put_into_dto(),
                "Specification": specification.put_into_dto()}

    def get_sections_for_interactive_advertising_panel(self, interactive_advertising_panel_id: int):
        session = self.get_session()

        interactive_advertising_panel = session.query(InteractiveAdvertisingPanel).filter_by(
            id=interactive_advertising_panel_id).first()
        sections_ids = (
            session.query(interactive_advertising_panel_has_commercials.c.sections_id)
            .filter(
                interactive_advertising_panel_has_commercials.c.interactive_advertising_panel_id ==
                interactive_advertising_panel_id).all()
        )
        sections_ids = [sections_id for (sections_id,) in sections_ids]
        sections = session.query(Section).filter(Section.id.in_(sections_ids)).all()
        data = {
            "Interactive Advertising Panel": interactive_advertising_panel.put_into_dto(),
            "Section": [section.put_into_dto() for section in sections]
        }
        return data

