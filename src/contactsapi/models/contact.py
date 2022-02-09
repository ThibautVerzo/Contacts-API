"""Contact model."""
from sqlalchemy import Column, String, ForeignKey
from .base_model import BaseModel, Base

class Contact(BaseModel):
    __tablename__ = 'contact'

    firstname = Column(String(), nullable=False)
    lastname = Column(String(), nullable=False)
    fullname = Column(String(), nullable=False)
    address = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    phone_number = Column(String(), nullable=False)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'fullname': self.fullname,
            'address': self.address,
            'email': self.email,
            'phone_number': self.phone_number,
        }

class ContactSkill(BaseModel):
    __tablename__ = 'contact_skill'

    contact_id = Column(ForeignKey('contact.id'), primary_key=True)
    skill_id = Column(ForeignKey('skill.id'), primary_key=True)

    def to_dict(self) -> dict:
        return {
            'contact_id': self.contact_id,
            'skill_id': self.skill_id,
        }
