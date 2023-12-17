from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import mapped_column
from backend.db.db import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    from_user_id = mapped_column(Integer)
    to_user_id = mapped_column(Integer)
    text = mapped_column(String)
    date = mapped_column(DateTime)
