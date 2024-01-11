from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Specifications(db.Model, IDto):
    """
    Model declaration for Specifications.
    """
    __tablename__ = "specifications"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_year = db.Column(db.Integer, nullable=True)
    screen_resolution_capacity = db.Column(db.String(25), nullable=True)
    display_type = db.Column(db.String(15), nullable=True)

    interactive_advertising_panel = db.relationship("InteractiveAdvertisingPanel", backref="specifications_")

    def __repr__(self) -> str:
        return (f"Specifications(id={self.id}, model_year={self.model_year}, "
                f"screen_resolution_capacity={self.screen_resolution_capacity}, display_type={self.display_type}, ")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "model_year": self.model_year,
            "screen_resolution_capacity": self.screen_resolution_capacity,
            "display_type": self.display_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Specifications:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Specifications(
            model_year=dto_dict.get("model_year"),
            screen_resolution_capacity=dto_dict.get("screen_resolution_capacity"),
            display_type=dto_dict.get("display_type"),
        )
        return obj
