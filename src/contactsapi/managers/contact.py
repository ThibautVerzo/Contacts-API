"""Contact managers."""
# TYPE CHECKING
from pip._internal.network.session import PipSession
from typing import List
from contactsapi.models.base_model import BaseModel

from contactsapi.managers.base_manager import (
    BaseCollectionManager, BaseResourceManager
)
from contactsapi.models.contact import Contact, ContactSkill


class ContactsManager(BaseCollectionManager):
    model = Contact


class ContactManager(BaseResourceManager):
    model = Contact


class ContactSkillsManager(BaseCollectionManager):
    model = ContactSkill

    async def get(
            self, session: PipSession, contact_id: int
    ) -> List[BaseModel]:
        return await super().get(
            session, [ContactSkill.contact_id == contact_id]
        )

class ContactSkillManager(BaseResourceManager):
    model = ContactSkill

    async def delete(
            self,
            session: PipSession,
            element_id: int,
            *,
            contact_id: int,
            skill_id: int,
    ) -> None:
        return await super().delete(
            session,
            0,
            [
                ContactSkill.contact_id == contact_id,
                ContactSkill.skill_id == skill_id,
            ]
        )
