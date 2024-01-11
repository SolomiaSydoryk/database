from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

supermarket_has_section = db.Table(
    'supermarket_has_section',
    db.Column('supermarket_id', db.Integer, db.ForeignKey('supermarket.id'), primary_key=True),
    db.Column('section_id', db.Integer, db.ForeignKey('section.id'), primary_key=True),
    db.UniqueConstraint('supermarket_id', 'section_id', name='uq_supermarket_has_section'),
    extend_existing=True
)


class Section(db.Model, IDto):
    """
    Model declaration for Section.
    """
    __tablename__ = "section"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)

    supermarkets = db.relationship("Supermarket", secondary="supermarket_has_section", back_populates="sections")
    interactive_advertising_panel = db.relationship("InteractiveAdvertisingPanel", backref="sections_")

    def __repr__(self) -> str:
        return f"Section(id={self.id}, '{self.name}',)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Section:
        """
        Creates domain object from DTO        :param dto_dict:  object
        :return: Domain object
        """
        obj = Section(
            name=dto_dict.get("name"),
        )
        return obj
