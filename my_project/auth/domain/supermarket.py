from __future__ import annotations
from typing import Dict, Any

from sqlalchemy import Index

from my_project import db
from my_project.auth.domain.i_dto import IDto

supermarket_has_interactive_advertising_panel = db.Table(
    'supermarket_has_interactive_advertising_panel',
    db.Column('interactive_advertising_panel_id', db.Integer, db.ForeignKey('interactive_advertising_panel.id'),
              primary_key=True),
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'), primary_key=True),
    db.UniqueConstraint('interactive_advertising_panel_id', 'supermarket_id',
                        name='uq_supermarket_has_interactive_advertising_panel'),
    extend_existing=True
)

supermarket_has_section = db.Table(
    'supermarket_has_section',
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'), primary_key=True),
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.UniqueConstraint('supermarket_id', 'section_id', name='uq_supermarket_has_section2'),
    extend_existing=True
)

owner_has_supermarket = db.Table(
    'owner_has_supermarket',
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'), primary_key=True),
    db.Column('owner_id', db.Integer, db.ForeignKey('owner.id'), primary_key=True),
    db.UniqueConstraint('supermarket_id', 'owner_id', name='uq_owner_has_supermarket2'),
    extend_existing=True
)

supermarket_has_manufacturer = db.Table(
    'supermarket_has_manufacturer',
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id')),
    db.Column('manufacturer_id', db.Integer, db.ForeignKey('manufacturer.id')),
    extend_existing=True
)


class Supermarket(db.Model, IDto):
    """
    Model declaration for Supermarket.
    """
    __tablename__ = "supermarket"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    supermarket_name = db.Column(db.String(40), nullable=False)
    description_of_supermarket = db.Column(db.String(60), nullable=True)
    area = db.Column(db.Float, nullable=True)
    trade_network = db.Column(db.String(45), nullable=False)
    business_hours = db.Column(db.String(15), nullable=True)
    average_number_of_visitors = db.Column(db.Integer, nullable=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)

    # 1:1
    address = db.relationship("Address", back_populates="supermarket")

    # M:M
    manufacturers = db.relationship("Manufacturer", secondary="supermarket_has_manufacturer",
                                    back_populates="supermarkets")

    interactive_advertising_panels = db.relationship("InteractiveAdvertisingPanel",
                                                     secondary="supermarket_has_interactive_advertising_panel",
                                                     back_populates="supermarkets")
    sections = db.relationship("Section", secondary="supermarket_has_section", back_populates="supermarkets")

    employee = db.relationship("Employee", backref="supermarket_employee")

    def __repr__(self) -> str:
        return (f"Supermarket(id={self.id}, '{self.supermarket_name}', '{self.description_of_supermarket},' "
                f"'{self.area}', trade_network={self.trade_network}, '{self.business_hours}',"
                f"average_number_of_visitors={self.average_number_of_visitors}, address_id={self.address_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "supermarket_name": self.supermarket_name,
            "description_of_supermarket": self.description_of_supermarket,
            "area": self.area,
            "trade_network": self.trade_network,
            "business_hours": self.business_hours,
            "average_number_of_visitors": self.average_number_of_visitors,
            "address_id": self.address_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Supermarket:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Supermarket(
            supermarket_name=dto_dict.get("supermarket_name"),
            description_of_supermarket=dto_dict.get("description_of_supermarket"),
            area=dto_dict.get("area"),
            trade_network=dto_dict.get("trade_network"),
            business_hours=dto_dict.get("business_hours"),
            average_number_of_visitors=dto_dict.get("average_number_of_visitors"),
            address_id=dto_dict.get("address_id"),

        )
        return obj
