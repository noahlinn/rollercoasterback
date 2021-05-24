from controllers import coaster_controller 

def apply_coaster_routes(app):
    app.route('/coasters', methods=["POST"])(coaster_controller.create_coaster)
    app.route('/coasters/search', methods=["POST"])(coaster_controller.search_coasters_by_name)
    app.route('/seed', methods=["POST"])(coaster_controller.seeding)
    app.route('/coasters/<int:id>', methods=["GET"])(coaster_controller.get_one_coaster)