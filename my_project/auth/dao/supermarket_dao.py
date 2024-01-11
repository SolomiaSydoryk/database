from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Supermarket, Address, Manufacturer
from my_project.auth.domain.supermarket import supermarket_has_manufacturer
from my_project.auth.domain.interactive_advertising_panel import supermarket_has_interactive_advertising_panel
from my_project.auth.domain.interactive_advertising_panel import InteractiveAdvertisingPanel

from flask import jsonify


class SupermarketDAO(GeneralDAO):
    """
    Realisation of Supermarket data access layer.
    """
    _domain_type = Supermarket

    def get_address_for_supermarket(self, supermarket_id: int):
        session = self.get_session()
        address_id = session.query(Supermarket).filter_by(id=supermarket_id).first().address_id
        address = session.query(Address).filter_by(id=address_id).first()
        supermarket = session.query(Supermarket).filter_by(id=supermarket_id).first()
        return {"Supermarket": supermarket.put_into_dto(),
                "Address": address.put_into_dto()}

    def get_manufacturers_for_supermarket(self, supermarket_id: int):
        session = self.get_session()
        supermarket = session.query(Supermarket).filter_by(id=supermarket_id).first()
        manufacturers_ids = (
            session.query(supermarket_has_manufacturer.c.manufacturer_id)
            .filter(supermarket_has_manufacturer.c.supermarket_id == supermarket_id).all()
        )
        manufacturers_ids = [manufacturers_id for (manufacturers_id,) in manufacturers_ids]
        manufacturers = session.query(Manufacturer).filter(Manufacturer.id.in_(manufacturers_ids)).all()
        data = {
            "Supermarket": supermarket.put_into_dto(),
            "Manufacturers": [manufacturer.put_into_dto() for manufacturer in manufacturers]
        }
        return data

    def connect_manufacturer_and_supermarket_from_supermarket(self, manufacturer_id: int, supermarket_id: int):
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

    def remove_manufacturer_from_supermarket(self, manufacturer_id: int, supermarket_id: int):
        session = self.get_session()
        session.execute(supermarket_has_manufacturer.delete().
                        where(supermarket_has_manufacturer.c.supermarket_id == supermarket_id).
                        where(supermarket_has_manufacturer.c.manufacturer_id == manufacturer_id))
        session.commit()
