from backend.models.social_media import SocialMedia
from backend.utils.repository import SQLAlchemyRepository


class SocialMediaRepository(SQLAlchemyRepository):
    model = SocialMedia
