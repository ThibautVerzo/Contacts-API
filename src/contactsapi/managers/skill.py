"""Skill managers."""
from contactsapi.managers.base_manager import (
    BaseCollectionManager, BaseResourceManager
)
from contactsapi.models.skill import Skill


class SkillsManager(BaseCollectionManager):
    model = Skill


class SkillManager(BaseResourceManager):
    model = Skill