from backend.models.user_social_media import UserSocialMedia
from backend.utils.repository import SQLAlchemyRepository


class UserSocialMediaRepository(SQLAlchemyRepository):
    model = UserSocialMedia
