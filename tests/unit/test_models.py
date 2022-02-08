from contactsapi.models.contact import Contact, ContactSkill
from contactsapi.models.skill import Skill, SkillLevel

CONTACT = {
    'firstname': 'FirstName',
    'lastname': 'LastName',
    'fullname': 'FullName',
    'address': '190 test Avenue',
    'email': 'test@email.com',
    'phone_number': '0666666666',
}


def test_contact_model():
    contact = Contact(**CONTACT)
    assert {'id': None, **CONTACT} == contact.to_dict()


SKILL = {
    'name': 'skill1',
    'level': SkillLevel.EXPERT,
}


def test_skill_model():
    skill = Skill(**SKILL)
    assert {'id': None, **SKILL} == skill.to_dict()


CONTACT_SKILL = {
    'contact_id': 1,
    'skill_id': 1,
}


def test_contact_skill_model():
    contact_skill = ContactSkill(**CONTACT_SKILL)
    assert {**CONTACT_SKILL} == contact_skill.to_dict()

