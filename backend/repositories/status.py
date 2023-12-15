from backend.models.status import Status
from backend.utils.repository import SQLAlchemyRepository


class StatusRepository(SQLAlchemyRepository):
    model = Status
