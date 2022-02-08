import pytest
from unittest.mock import patch
from sanic_testing.testing import SanicASGITestClient

# TYPE CHECKING
from sanic import Sanic

import json
from contactsapi.models.contact import Contact


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
