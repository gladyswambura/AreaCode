from flask import Flask
from flask_login import LoginManager
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


app=Flask(__name__)
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.login_message_category = "info"

def create_app(config_name):
    app.config.from_object(config_options[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
   

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app