from controllers import news_controller
def apply_news_routes(app):
    app.route('/parknews', methods=["GET"])(news_controller.search_park_news)
