"""Contact validator."""
from dataclasses import dataclass


@dataclass
class ContactValidator:
    firstname: str
    lastname: str
    fullname: str
    address: str
    email: str
    phone_number: str


@dataclass
class ContactSkillValidator:
    skill_id: int
