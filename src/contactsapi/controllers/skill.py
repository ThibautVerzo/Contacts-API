"""Skill controllers."""
# TYPE CHECKING
from typing import Tuple
from sanic.response import HTTPResponse
from sanic.request import Request

from contactsapi.controllers.base_controller import (
    BaseCollectionController, BaseResourceController
)
from contactsapi.validators.skill import SkillValidator
from contactsapi.managers.skill import SkillsManager, SkillManager

from sanic_ext import openapi


class SkillsView(BaseCollectionController):
    collection_manager = SkillsManager()
    manager = SkillManager()

    @openapi.definition(
        summary=f"Returns all skills.",
    )
    async def get(self, request: Request) -> HTTPResponse:
        return await super().get(request)

    @openapi.definition(
        body=SkillValidator,
        summary=f"Creates skill.",
    )
    async def post(self, request: Request) -> HTTPResponse:
        return await super().post(request)


class SkillView(BaseResourceController):
    manager = SkillManager()

    @openapi.definition(
        summary="Returns a skill.",
    )
    async def get(self, request, skill_id: int) -> HTTPResponse:
        return await super().get(request, skill_id)

    @openapi.definition(
        body=SkillValidator,
        summary="Modifies a skill.",
    )
    async def put(self, request, skill_id: int) -> HTTPResponse:
        return await super().put(request, skill_id)

    @openapi.definition(
        summary="Deletes a skill.",
    )
    async def delete(self, request, skill_id: int) -> HTTPResponse:
        return await super().delete(request, skill_id)