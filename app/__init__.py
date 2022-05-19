from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet, IMAGES, configure_uploads

from config import config_options

photos = UploadSet('photos', IMAGES)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    configure_uploads(app,photos)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Registering the blueprint
    # register home blueprint
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from app.posts.views import posts
    app.register_blueprint(posts)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
