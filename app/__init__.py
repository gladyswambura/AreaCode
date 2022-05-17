from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    
    #initialize imports
    db.init_app(app)
    bootstrap.init_app(app)
    
    # register home blueprint
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    
    return app