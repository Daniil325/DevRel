from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import mapped_column
from backend.db.db import Base


class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True, nullable=False)
    name = mapped_column(String)
