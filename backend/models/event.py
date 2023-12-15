from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import mapped_column
from backend.db.db import Base


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = mapped_column(String)
    description = mapped_column(String)
    date = mapped_column(Date)
    format = mapped_column(String)
