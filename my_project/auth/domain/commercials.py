from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

interactive_advertising_panel_has_commercials = db.Table(
    'interactive_advertising_panel_has_commercials',
    db.Column('interactive_advertising_panel_id', db.Integer, db.ForeignKey('interactive_advertising_panel.id')),
    db.Column('commercials_id', db.Integer, db.ForeignKey('commercials.id')),
    extend_existing=True
)


class Commercials(db.Model, IDto):
    """
    Model declaration for Commercials.
    """
    __tablename__ = "commercials"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    duration = db.Column(db.String(15), nullable=False)
    manufacturer = db.Column(db.String(30), nullable=False)
    trademark_in_video = db.Column(db.String(30), nullable=False)

    # Relationship M:M with InteractiveAdvertisingPanel
    interactive_advertising_panels = db.relationship("InteractiveAdvertisingPanel",
                                                     secondary="interactive_advertising_panel_has_commercials",
                                                     back_populates="commercials")

    def __repr__(self) -> str:
        return (f"Commercials(id={self.id}, duration={self.duration}, manufacturer={self.manufacturer}, "
                f"trademark_in_video={self.trademark_in_video},)")

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "duration": self.duration,
            "manufacturer": self.manufacturer,
            "trademark_in_video": self.trademark_in_video,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Commercials:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Commercials(
            duration=dto_dict.get("duration"),
            manufacturer=dto_dict.get("manufacturer"),
            trademark_in_video=dto_dict.get("trademark_in_video"),
        )
        return obj
