from backend.repositories.tag import TagRepository
from backend.services.tag import TagService
from backend.repositories.event import EventRepository
from backend.services.event import EventService
from backend.repositories.user import UserRepository
from backend.services.user import AuthService
from backend.repositories.event_tag import EventTagRepository
from backend.services.event_tag import EventTagService
from backend.repositories.social_media import SocialMediaRepository
from backend.services.social_media import SocialMediaService
from backend.repositories.status import StatusRepository
from backend.services.status import StatusService
from backend.repositories.user_social_media import UserSocialMediaRepository
from backend.services.user_social_media import UserSocialMediaService
from backend.repositories.review import ReviewRepository
from backend.services.review import ReviewService
from backend.repositories.user_event import UserEventRepository
from backend.services.user_event import UserEventService


def review_service():
    return ReviewService(ReviewRepository)


def user_event_service():
    return UserEventService(UserEventRepository)


def user_social_media_service():
    return UserSocialMediaService(UserSocialMediaRepository)


def status_service():
    return StatusService(StatusRepository)


def tag_service():
    return TagService(TagRepository)


def event_service():
    return EventService(EventRepository, EventTagRepository)


def user_service():
    return AuthService(UserRepository)


def event_tag_service():
    return EventTagService(EventTagRepository)


def social_media_service():
    return SocialMediaService(SocialMediaRepository)
