"""File for customs exception."""
from sanic.exceptions import NotFound, SanicException

class ContactsAPINotFound(NotFound):
    """The requeste object is not found is the ContactsAPI data base."""


class ContactsAPIVaidationError(SanicException):
    """An object field is not under the right schema."""