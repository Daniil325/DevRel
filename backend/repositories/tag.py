from backend.models.tag import Tag
from backend.utils.repository import SQLAlchemyRepository


class TagRepository(SQLAlchemyRepository):
    model = Tag
