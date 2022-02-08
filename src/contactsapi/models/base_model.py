"""Base model."""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, INTEGER

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = Column(INTEGER(), primary_key=True)
