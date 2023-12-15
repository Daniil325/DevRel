from backend.db.db import User
from backend.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
