from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Manufacturer, Supermarket
from my_project.auth.domain.manufacturer import supermarket_has_manufacturer


class ManufacturerDAO(GeneralDAO):
    """
    Realisation of Manufacturer data access layer.
    """
    _domain_type = Manufacturer

    def get_supermarkets_for_manufacturer(self, manufacturer_id: int):
        session = self.get_session()
        manufacturer = session.query(Manufacturer).filter_by(id=manufacturer_id).first()
        supermarkets_ids = (
            session.query(supermarket_has_manufacturer.c.supermarket_id)
            .filter(supermarket_has_manufacturer.c.manufacturer_id == manufacturer_id).all()
        )
        supermarkets_ids = [supermarkets_id for (supermarkets_id,) in supermarkets_ids]
        supermarkets = session.query(Supermarket).filter(Supermarket.id.in_(supermarkets_ids)).all()
        data = {
            "Manufacturer": manufacturer.put_into_dto(),
            "Supermarkets": [supermarket.put_into_dto() for supermarket in supermarkets]
        }
        return data

    def connect_manufacturer_and_supermarket_from_manufacturer(self, manufacturer_id: int, supermarket_id: int):
        session = self.get_session()
        session.execute(supermarket_has_manufacturer.insert().values(manufacturer_id=manufacturer_id,
                                                                     supermarket_id=supermarket_id))
        session.commit()

    def insert_in_supermarket_has_manufacturer_by_values(self, manufacturer_name: str, supermarket_name: str):
        session = self.get_session()
        manufacturer_id = session.query(Manufacturer).filter_by(name=manufacturer_name).first().id
        supermarket_id = session.query(Supermarket).filter_by(supermarket_name=supermarket_name).first().id
        session.execute(supermarket_has_manufacturer.insert().values(manufacturer_id=manufacturer_id,
                                                                     supermarket_id=supermarket_id))
        session.commit()

    def remove_supermarket_from_manufacturer(self, manufacturer_id: int, supermarket_id: int):
        session = self.get_session()
        session.execute(supermarket_has_manufacturer.delete().
                        where(supermarket_has_manufacturer.c.supermarket_id == supermarket_id).
                        where(supermarket_has_manufacturer.c.manufacturer_id == manufacturer_id))
        session.commit()
