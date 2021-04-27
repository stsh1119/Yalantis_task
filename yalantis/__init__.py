from flask import Flask
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .models import db
    db.init_app(app)

    from .errors.handlers import errors
    from .courses.routes import courses

    app.register_blueprint(courses)
    app.register_blueprint(errors)

    return app
