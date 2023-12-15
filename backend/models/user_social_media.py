from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from backend.db.db import Base, User
from backend.models.social_media import SocialMedia


class UserSocialMedia(Base):
    __tablename__ = 'user_social_media'

    id = Column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey(User.id))
    social_media_id = mapped_column(ForeignKey(SocialMedia.id))

    user = relationship(
        User, foreign_keys=[user_id], lazy='joined'
    )
    social_media = relationship(
        SocialMedia, foreign_keys=[social_media_id], lazy='joined'
    )
