from .user_routes import apply_users_routes
from .coaster_routes import apply_coaster_routes
from .news_routes import apply_news_routes
def apply_routes(app):
    apply_users_routes(app)
    apply_coaster_routes(app)
    apply_news_routes(app)