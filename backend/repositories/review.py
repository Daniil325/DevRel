from backend.models.review import Review
from backend.utils.repository import SQLAlchemyRepository


class ReviewRepository(SQLAlchemyRepository):
    model = Review
