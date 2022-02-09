"""Skill model."""
from sqlalchemy import Column, String, Enum as db_Enum
from .base_model import BaseModel
from enum import Enum

class SkillLevel(Enum):
    NOVICE = 'Novice'
    ADVANCED_BEGINNER = 'Advanced Biginner'
    COMPETENT = 'Competent'
    PROFICIENT = 'Proficient'
    EXPERT = 'Expert'

class Skill(BaseModel):
    __tablename__ = 'skill'

    name = Column(String(), nullable=False)
    level = Column(db_Enum(SkillLevel), nullable=False)

    def to_dict(self) -> dict:
        level = self.level if isinstance(self.level, str) else self.level.value
        return {
            'id': self.id,
            'name': self.name,
            'level': level,
        }
