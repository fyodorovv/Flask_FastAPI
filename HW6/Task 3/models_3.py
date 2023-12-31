from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean


# Pydantic
class Status(BaseModel):
    status: bool = False


class TaskIn(Status):
    name: str
    description: str | None = None


class TaskOut(TaskIn):
    id: int


# sqlalchemy
Base = declarative_base()


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text, nullable=True)
    status = Column(Boolean, default=False)
