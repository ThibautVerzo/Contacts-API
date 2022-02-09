"""Contact controllers."""
# TYPE CHECKING
from typing import Tuple
from sanic.response import HTTPResponse
from sanic.request import Request

from contactsapi.controllers.base_controller import (
    BaseCollectionController,
    BaseResourceController,
    BaseResourceControllerDelete
)
from contactsapi.validators.contact import (
    ContactValidator, ContactSkillValidator
)
from contactsapi.managers.contact import (
    ContactsManager, ContactManager, ContactSkillsManager, ContactSkillManager
)

from sanic_ext import openapi


class ContactsView(BaseCollectionController):
    collection_manager = ContactsManager()
    manager = ContactManager()

    @openapi.definition(
        summary=f"Returns all contacts.",
    )
    async def get(self, request: Request) -> HTTPResponse:
        return await super().get(request)

    @openapi.definition(
        body=ContactValidator,
        summary=f"Creates contact.",
    )
    async def post(self, request: Request) -> HTTPResponse:
        return await super().post(request)


class ContactView(BaseResourceController):
    manager = ContactManager()

    @openapi.definition(
        summary="Returns a contact.",
    )
    async def get(self, request, contact_id: int) -> HTTPResponse:
        return await super().get(request, contact_id)

    @openapi.definition(
        body=ContactValidator,
        summary="Modifies a contact.",
    )
    async def put(self, request, contact_id: int) -> HTTPResponse:
        return await super().put(request, contact_id)

    @openapi.definition(
        summary="Deletes a contact.",
    )
    async def delete(self, request, contact_id: int) -> HTTPResponse:
        return await super().delete(request, contact_id)


class ContactSkillsView(BaseCollectionController):
    collection_manager = ContactSkillsManager()
    manager = ContactSkillManager()

    @openapi.definition(
        summary="Returns the skills of a contact.",
    )
    async def get(self, request, contact_id: int) -> HTTPResponse:
        return await super().get(request, contact_id=contact_id)

    @openapi.definition(
        body=ContactSkillValidator,
        summary=f"Add a skill to a contact.",
    )
    async def post(self, request: Request, contact_id: int) -> HTTPResponse:
        request.json['contact_id'] = contact_id
        return await super().post(request)


class ContactSkillView(BaseResourceControllerDelete):
    manager = ContactSkillManager()

    @openapi.definition(
        summary="Deletes a skill contact.",
    )
    async def delete(
            self, request, contact_id: int, skill_id: int
    ) -> HTTPResponse:
        return await super().delete(
            request, 0, contact_id=contact_id, skill_id=skill_id
        )
