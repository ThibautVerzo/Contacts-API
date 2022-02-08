"""File for customs exception."""
from sanic.exceptions import NotFound

class ContactsAPINotFound(NotFound):
    """The requeste object is not found is the ContactsAPI data base."""