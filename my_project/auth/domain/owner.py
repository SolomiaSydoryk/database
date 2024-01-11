from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

owner_has_supermarket = db.Table(
    'owner_has_supermarket',
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'), primary_key=True),
    db.Column('owner_id', db.Integer, db.ForeignKey('owner.id'), primary_key=True),
    db.UniqueConstraint('supermarket_id', 'owner_id', name='uq_owner_has_supermarket'),
    extend_existing=True
)


class Owner(db.Model, IDto):
    """
    Model declaration for Owner.
    """
    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    email = db.Column(db.String(45), nullable=False)


    def __repr__(self) -> str:
        return (f"Owner(id={self.id}, '{self.name}', '{self.surname},' "
                f"'{self.phone},' '{self.email}')")

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
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Owner:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Owner(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            phone=dto_dict.get("phone"),
            email=dto_dict.get("email"),
        )
        return obj
