from flask import Flask
from config import config_options



def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    
    # register home blueprint
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    
    return app