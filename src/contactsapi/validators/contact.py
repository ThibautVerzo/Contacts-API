"""Contact validator."""
from dataclasses import dataclass


@dataclass
class ContactValidator:
    firstname: str = 'Firstname'
    lastname: str = 'Lastname'
    fullname: str = 'Fullname'
    address: str = '190 address street'
    email: str = 'email@email.com'
    phone_number: str = '0666666666'


@dataclass
class ContactResponse:
    id: int = 1
    firstname: str = 'Firstname'
    lastname: str = 'Lastname'
    fullname: str = 'Fullname'
    address: str = '190 address street'
    email: str = 'email@email.com'
    phone_number: str = '0666666666'



@dataclass
class ContactSkillValidator:
    skill_id: int
