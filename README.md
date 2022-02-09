# Contacts-API

In root directory:

###Setup:

pip install -r requirements.txt

alembic upgrade

(In case of alembic error use init.sql file in MySQL folder.)

###Run:
contactsapi run

###Test:
pytest tests/

###Test coverage:
pytest --cov=src/ tests

###Documentation:
http://127.0.0.1:8000/docs/swagger