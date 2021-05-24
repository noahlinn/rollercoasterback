from controllers import coaster_controller 

def apply_coaster_routes(app):
    app.route('/coasters', methods=["POST"])(coaster_controller.create_coaster)