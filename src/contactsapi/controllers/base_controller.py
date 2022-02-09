"""Base controllers."""
# TYPE CHECKING
from typing import Tuple
from sanic.response import HTTPResponse
from sanic.request import Request
from contactsapi.managers.base_manager import (
    BaseResourceManager, BaseCollectionManager
)

from contactsapi.helpers import json_list_response

from sanic.response import json, text
from sanic.views import HTTPMethodView


class BaseCollectionController(HTTPMethodView):
    collection_manager: BaseCollectionManager = ...
    manager: BaseResourceManager = ...

    async def get(self, request: Request, **kwargs) -> HTTPResponse:
        session = request.ctx.session
        elements = await self.collection_manager.get(session, **kwargs)
        return json_list_response([_.to_dict() for _ in elements])

    async def post(self, request: Request) -> HTTPResponse:
        session = request.ctx.session
        element = await self.manager.create(session, request)
        return json(element.to_dict())


class BaseResourceController(HTTPMethodView):
    manager: BaseResourceManager = ...

    async def get(self, request, element_id: int) -> HTTPResponse:
        session = request.ctx.session
        element = await self.manager.get(session, element_id)
        if not element:
            return json({})
        return json(element.to_dict())

    async def put(self, request, element_id: int) -> HTTPResponse:
        session = request.ctx.session
        element = await self.manager.update(session, request, element_id)
        if not element:
            return json({})
        return json(element.to_dict())

    async def delete(self, request, element_id: int) -> HTTPResponse:
        session = request.ctx.session
        element = await self.manager.delete(session, element_id)
        return json({})


class BaseResourceControllerDelete(HTTPMethodView):
    manager: BaseResourceManager = ...

    async def delete(self, request, element_id: int, **kwargs) -> HTTPResponse:
        session = request.ctx.session
        element = await self.manager.delete(session, element_id, **kwargs)
        return json({})
