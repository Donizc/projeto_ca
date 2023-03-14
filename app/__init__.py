from flask import Flask


def created_app():
    app = Flask(__name__)
    from .route import sentimental_analysis
    app.register_blueprint(sentimental_analysis)

    return app