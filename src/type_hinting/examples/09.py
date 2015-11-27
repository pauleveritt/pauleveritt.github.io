from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    Text
)

Base = declarative_base()
Session = sessionmaker()
session = Session()


# start-here
class ToDo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    title = Column(Text)

    @classmethod
    def list(cls) -> List[ToDo]:
        return session.query(cls).order_by(cls.title)
