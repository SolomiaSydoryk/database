from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy import UniqueConstraint


class Employee(db.Model, IDto):
    """
    Model declaration for Employee.
    """
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    position = db.Column(db.String(30), nullable=False)
    supermarket_id = db.Column(db.Integer, db.ForeignKey('supermarket.id'), nullable=False)

    supermarket = db.relationship("Supermarket", backref="employee_")

    def __repr__(self) -> str:
        return (f"Employee(id={self.id}, '{self.name}', '{self.surname},' "
                f"'{self.phone},' '{self.position}', supermarket_id={self.supermarket_id}, "
                f"supermarket_address_id={self.supermarket_address_id})")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "phone": self.phone,
            "position": self.position,
            "supermarket_id": self.supermarket_id,
            "supermarket_address_id": self.supermarket_address_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Employee(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            phone=dto_dict.get("phone"),
            position=dto_dict.get("position"),
            supermarket_id=dto_dict.get("supermarket_id"),
            supermarket_address_id=dto_dict.get("supermarket_address_id"),
        )
        return obj
