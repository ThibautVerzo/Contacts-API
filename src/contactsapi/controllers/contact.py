"""Contact controllers."""
from sanic.response import json, text
from sanic.views import HTTPMethodView
from sanic_ext import openapi

# TYPE CHECKING
from typing import Tuple
from sanic.response import HTTPResponse
from sanic.request import Request

from contactsapi.validators.contact import ContactValidator
from contactsapi.managers.contact import ContactsManager, ContactManager
from contactsapi.helpers import json_list_response


class ContactsView(HTTPMethodView):
    @openapi.definition(
        summary="Returns all contacts.",
    )
    async def get(self, request: Request) -> HTTPResponse:
        session = request.ctx.session
        contacts_manager = ContactsManager()
        contacts = await contacts_manager.get(session)
        return json_list_response([_.to_dict() for _ in contacts])


    @openapi.definition(
        body=ContactValidator,
        summary="Creates contact.",
    )
    async def post(self, request: Request) -> HTTPResponse:
        session = request.ctx.session
        contact_manager = ContactManager()
        contact = await contact_manager.create(session, request)
        return json(contact.to_dict())


class ContactView(HTTPMethodView):
    @openapi.definition(
        summary="Returns a contact.",
    )
    async def get(self, request, contact_id: int) -> HTTPResponse:
        session = request.ctx.session
        contact_manager = ContactManager()
        contact = await contact_manager.get(session, contact_id)
        if not contact:
            return json({})
        return json(contact.to_dict())

    @openapi.definition(
        body=ContactValidator,
        summary="Modifies a contact.",
    )
    async def put(self, request, contact_id: int) -> HTTPResponse:
        session = request.ctx.session
        contact_manager = ContactManager()
        contact = await contact_manager.update(session, request, contact_id)
        if not contact:
            return json({})
        return json(contact.to_dict())

    @openapi.definition(
        summary="Deletes a contact.",
    )
    async def delete(self, request, contact_id: int) -> HTTPResponse:
        session = request.ctx.session
        contact_manager = ContactManager()
        contact = await contact_manager.delete(session, contact_id)
        return json({})
