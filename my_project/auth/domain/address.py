from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Address(db.Model, IDto):
    """
    Model declaration for Address.
    """
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street_name = db.Column(db.String(45), nullable=False)
    number_of_building = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(45), nullable=False)
    region = db.Column(db.String(45), nullable=False)

    # 1:1
    supermarket = db.relationship("Supermarket", uselist=False, back_populates='address')

    def __repr__(self) -> str:
        return (f"Address(id={self.id}, '{self.city}', '{self.region}', '{self.street_name}', "
                f"'{self.number_of_building}')")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "city": self.city,
            "region": self.region,
            "street_name": self.street_name,
            "number_of_building": self.number_of_building,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Address:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Address(
            city=dto_dict.get("city"),
            region=dto_dict.get("region"),
            street_name=dto_dict.get("street_name"),
            number_of_building=dto_dict.get("number_of_building"),
        )
        return obj
