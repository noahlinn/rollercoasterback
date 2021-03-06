from controllers import users_controller

def apply_users_routes(app):
    app.route('/users', methods=["POST"])(users_controller.create_user)
    app.route('/users/login', methods=["POST"])(users_controller.login)
    app.route('/users/verify', methods=["GET"])(users_controller.verify)
    app.route('/users/<int:id>', methods=["GET"])(users_controller.one_user)
    app.route('/users/credits/<int:id>', methods=["PUT", "GET", "DELETE"])(users_controller.credits)
    app.route('/users/bucketlist/<int:id>', methods=["PUT", "GET", "DELETE"])(users_controller.add_to_bucketlist)
    app.route('/users/search/name', methods=["POST"])(users_controller.search_by_name)
    app.route('/users/search/location', methods=["POST"])(users_controller.search_by_location)
    app.route('/users/created/<int:id>', methods=["GET"])(users_controller.get_users_created_coasters)


    