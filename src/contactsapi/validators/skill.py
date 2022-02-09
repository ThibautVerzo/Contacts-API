"""Skill validator."""
from dataclasses import dataclass
from contactsapi.models.skill import SkillLevel


@dataclass
class SkillValidator:
    name: str
    level: str
