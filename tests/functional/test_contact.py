import pytest
import json
from unittest.mock import patch
from sanic_testing.testing import SanicASGITestClient

# TYPE CHECKING
from sanic import Sanic

from contactsapi.models.contact import Contact
from .test_skill import SKILL


CONTACT = {
    'firstname': 'FirstName',
    'lastname': 'LastName',
    'fullname': 'FullName',
    'address': '190 test Avenue',
    'email': 'test@email.com',
    'phone_number': '0666666666',
}


def test_get_contacts(app: Sanic):
    _, response = app.test_client.get('/api/contacts')

    assert response.status_code == 200


def test_post_contact(app: Sanic):
    with patch(
        'contactsapi.managers.contact.ContactManager.create',
        return_value=Contact(**CONTACT)
    ) as contact_create_mock:
        _, response = app.test_client.post('/api/contacts', data=CONTACT)

        assert response.status_code == 200
        assert response.json == {'id': None, **CONTACT}


async def test_contact(app: Sanic):
    client = SanicASGITestClient(app)
    # POST
    _, response = await client.post(
        '/api/contacts', content=json.dumps(CONTACT, indent=4),
    )
    contact_id = response.json['id']
    assert response.json == {'id': contact_id, **CONTACT}

    # GET
    _, response = await client.get(f'/api/contacts/{contact_id}')
    assert response.json == {'id': contact_id, **CONTACT}

    # UPDATE
    contact_update = CONTACT.copy()
    contact_update['firstname'] = 'Firstname Updated'
    _, response = await client.put(
        f'/api/contacts/{contact_id}',
        content=json.dumps(contact_update, indent=4),
    )
    assert response.json == {'id': contact_id, **contact_update}

    # GET
    _, response = await client.get(f'/api/contacts/{contact_id}')
    assert response.json == {'id': contact_id, **contact_update}

    # DELETE
    _, response = await client.delete(f'/api/contacts/{contact_id}')
    assert response.json == {}

    # GET
    _, response = await client.get(f'/api/contacts/{contact_id}')
    assert response.json == {}


async def test_contact_skill(app: Sanic):
    client = SanicASGITestClient(app)

    # POST CONTACT
    _, response = await client.post(
        '/api/contacts', content=json.dumps(CONTACT, indent=4),
    )
    contact_id = response.json['id']
    assert response.json == {'id': contact_id, **CONTACT}

    # POST SKILL
    _, response = await client.post(
        '/api/skills',
        content=json.dumps(SKILL.copy(), indent=4),
    )
    skill_id = response.json['id']
    assert response.json == {'id': skill_id, **SKILL}

    # ADD SKILL TO CONTACT
    _, response = await client.post(
        f'/api/contacts/{contact_id}/skills',
        content=json.dumps({'skill_id': skill_id}, indent=4),
    )

    # GET CONTACT SKILLS
    _, response = await client.get(f'/api/contacts/{contact_id}/skills')
    assert response.json == {
        'count': 1,
        'values': [{'contact_id': contact_id, 'skill_id': skill_id}]
    }

    # DELETE CONTACT SKILL
    _, response = await client.delete(
        f'/api/contacts/{contact_id}/skills/{skill_id}'
    )
    assert response.json == {}

    # GET CONTACT SKILLS
    _, response = await client.get(f'/api/contacts/{contact_id}/skills')
    assert response.json == {'count': 0, 'values': []}

    # DELETE CONTACT
    _, response = await client.delete(f'/api/contacts/{contact_id}')
    assert response.json == {}

    # GET CONTACT
    _, response = await client.get(f'/api/contacts/{contact_id}')
    assert response.json == {}

    # DELETE
    _, response = await client.delete(f'/api/skills/{skill_id}')
    assert response.json == {}

    # GET
    _, response = await client.get(f'/api/skills/{skill_id}')
    assert response.json == {}