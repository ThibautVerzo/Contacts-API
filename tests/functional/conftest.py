import pytest
from contactsapi import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def test_app(loop, app, test_client):
    return loop.run_until_complete(test_client(app))

