from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
from backend.db.db import Base


class SocialMedia(Base):
    __tablename__ = 'social_media'

    id = Column(Integer, primary_key=True)
    name = mapped_column(String)
