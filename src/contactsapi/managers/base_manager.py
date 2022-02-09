"""Base managers."""
# TYPE CHECKING
from pip._internal.network.session import PipSession
from typing import List, Optional
from sanic.request import Request
from contactsapi.models.base_model import BaseModel

from contactsapi.exceptions import ContactsAPINotFound
from sqlalchemy import select, delete, update

from sanic.log import logger

class BaseCollectionManager:
    model: BaseModel = ...

    async def get(
        self, session: PipSession, constraints: Optional[list] = None
    ) -> List[BaseModel]:
        async with session.begin():
            if not constraints:
                stmt = select(self.model)
            else:
                stmt = select(self.model).where(*constraints)
            result = await session.execute(stmt)
            elements = result.all()
        return [_[0] for _ in elements]

class BaseResourceManager:
    model: BaseModel = ...

    async def create(self, session: PipSession, request: Request) -> BaseModel:
        async with session.begin():
            element = self.model(**request.json)
            session.add(element)
        logger.info(f'{self.model.__name__} with id {element.id} created.')
        return element

    async def get(
            self,
            session: PipSession,
            element_id: int,
            constraints: Optional[list] = None
    ) -> Optional[BaseModel]:
        async with session.begin():
            if not constraints:
                stmt = select(self.model).where(self.model.id == element_id)
            else:
                stmt = select(self.model).where(*constraints)
            result = await session.execute(stmt)
            element = result.scalar()
            if not element:
                return None
        return element

    async def update(
            self, session: PipSession,
            request: Request, element_id: int,
            constraints: Optional[list] = None
    ) -> Optional[BaseModel]:
        element = await self.get(session, element_id)
        if not element:
            return None
        async with session.begin():
            stmt = update(self.model).where(
                self.model.id == element_id
            ).values(**request.json)
            result = await session.execute(stmt)
        logger.info(f'{self.model.__name__} with id {element.id} updated.')
        return self.model(id=element_id, **request.json)

    async def delete(
            self,
            session: PipSession,
            element_id: int,
            constraints: Optional[list] = None
    ) -> None:
        element = await self.get(session, element_id, constraints)
        if not element:
            return
        async with session.begin():
            if not constraints:
                stmt = delete(self.model).where(self.model.id == element_id)
            else:
                stmt = delete(self.model).where(*constraints)
            result = await session.execute(stmt)
        logger.info(f'{self.model.__name__} with id {element.id} deleted.')