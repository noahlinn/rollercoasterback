from .user_routes import apply_users_routes

def apply_routes(app):
    apply_users_routes(app)