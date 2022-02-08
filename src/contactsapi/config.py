"""ContactsAPI config file."""
from sanic.config import Config


class MyConfig(Config):
    DB = {
        'name': 'contactsapi_db',
        'user': 'root',
        'password': 'password',
        'host': 'localhost',
        'port': '3306'
    }
