"""Contact managers."""
# TYPE CHECKING
from pip._internal.network.session import PipSession
from typing import List, Optional
from sanic.request import Request

from contactsapi.models.contact import Contact
from contactsapi.exceptions import ContactsAPINotFound
from sqlalchemy import select, delete, update

from sanic.log import logger


class ContactsManager:
    async def get(self, session: PipSession) -> List[Contact]:
        async with session.begin():
            stmt = select(Contact)
            result = await session.execute(stmt)
            contacts = result.all()
        return [_[0] for _ in contacts]


class ContactManager:
    async def create(self, session: PipSession, request: Request) -> Contact:
        async with session.begin():
            contact = Contact(**request.json)
            session.add(contact)
        logger.info(f'Contact with id {contact.id} created.')
        return contact

    async def get(
        self, session: PipSession, contact_id: int
    ) -> Optional[Contact]:
        async with session.begin():
            stmt = select(Contact).where(Contact.id == contact_id)
            result = await session.execute(stmt)
            contact = result.scalar()
            if not contact:
                return None
        return contact

    async def update(
        self, session: PipSession, request: Request, contact_id: int
    ) -> Optional[Contact]:
        contact = await self.get(session, contact_id)
        if not contact:
            return None
        async with session.begin():
            stmt = update(Contact).where(
                Contact.id == contact_id
            ).values(**request.json)
            result = await session.execute(stmt)
        logger.info(f'Contact with id {contact.id} updated.')
        return Contact(id=contact_id, **request.json)

    async def delete(
        self, session: PipSession, contact_id: int
    ) -> None:
        contact = await self.get(session, contact_id)
        if not contact:
            return
        async with session.begin():
            stmt = delete(Contact).where(Contact.id == contact_id)
            result = await session.execute(stmt)
        logger.info(f'Contact with id {contact.id} deleted.')