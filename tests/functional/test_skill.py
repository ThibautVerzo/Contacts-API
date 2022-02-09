import pytest
from unittest.mock import patch
from sanic_testing.testing import SanicASGITestClient

# TYPE CHECKING
from sanic import Sanic

import json
from contactsapi.models.skill import Skill, SkillLevel
from .helpers import deep_replace_enums


SKILL = {
    'name': 'skill1',
    'level': 'Expert',
}


def test_get_skills(app: Sanic):
    _, response = app.test_client.get('/api/skills')

    assert response.status_code == 200


def test_post_skill(app: Sanic):
    with patch(
        'contactsapi.managers.skill.SkillManager.create',
        return_value=Skill(**SKILL)
    ) as skill_create_mock:
        _, response = app.test_client.post(
            '/api/skills',
            data=SKILL.copy()
        )

        assert response.status_code == 200
        assert response.json == {'id': None, **SKILL}


async def test_skill(app: Sanic):
    client = SanicASGITestClient(app)
    # POST
    _, response = await client.post(
        '/api/skills',
        content=json.dumps(SKILL.copy(), indent=4),
    )
    skill_id = response.json['id']
    assert response.json == {'id': skill_id, **SKILL}

    # GET
    _, response = await client.get(f'/api/skills/{skill_id}')
    assert response.json == {'id': skill_id, **SKILL}

    # UPDATE
    skill_update = SKILL.copy()
    skill_update['name'] = 'skill2'
    _, response = await client.put(
        f'/api/skills/{skill_id}',
        content=json.dumps(skill_update.copy(), indent=4),
    )
    assert response.json == {'id': skill_id, **skill_update}

    # GET
    _, response = await client.get(f'/api/skills/{skill_id}')
    assert response.json == {'id': skill_id, **skill_update}

    # DELETE
    _, response = await client.delete(f'/api/skills/{skill_id}')
    assert response.json == {}

    # GET
    _, response = await client.get(f'/api/skills/{skill_id}')
    assert response.json == {}
