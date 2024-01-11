from sqlalchemy.orm import joinedload

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Commercials
from my_project.auth.domain.interactive_advertising_panel import InteractiveAdvertisingPanel
from my_project.auth.domain.interactive_advertising_panel import interactive_advertising_panel_has_commercials


class CommercialsDAO(GeneralDAO):
    """
    Realisation of Commercials data access layer.
    """
    _domain_type = Commercials

    def get_panel_for_commercials(self, commercials_id: int):
        session = self.get_session()
        commercials = session.query(Commercials).filter_by(id=commercials_id).first()
        panel_ids = (
            session.query(interactive_advertising_panel_has_commercials.c.panel_id)
            .filter(interactive_advertising_panel_has_commercials.c.commercials_id == commercials_id).all()
        )
        panel_ids = [panel_id for (panel_id,) in panel_ids]
        panels = session.query(InteractiveAdvertisingPanel).filter(InteractiveAdvertisingPanel
                                                                     .id.in_(panel_ids)).all()
        data = {
            "Interactive Advertising Panel": [panel.put_into_dto() for panel in panels],
            "Commercials": commercials.put_into_dto()
        }
        return data

    def add_interactive_advertising_panel_to_commercial(self, commercial_id: int,
                                                        interactive_advertising_panel_id: int):
        session = self.get_session()

        association = interactive_advertising_panel_has_commercials.insert().values(
            commercials_id=commercial_id,
            interactive_advertising_panel_id=interactive_advertising_panel_id
        )

        session.execute(association)

        session.commit()

    def remove_interactive_advertising_panel_from_commercial(self, commercial_id: int,
                                                             interactive_advertising_panel_id: int):
        session = self.get_session()

        session.execute(
            interactive_advertising_panel_has_commercials.delete()
            .where(interactive_advertising_panel_has_commercials.c.commercial_id == commercial_id)
            .where(
                interactive_advertising_panel_has_commercials.c.interactive_advertising_panel_id == interactive_advertising_panel_id)
        )

        session.commit()
