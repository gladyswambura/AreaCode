from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from App.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()


mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    
    mail.init_app(app)

    # from App.users.views import users
    from App.posts.views import posts
    # from App.main.views import main
    # app.register_blueprint(users)
    app.register_blueprint(posts)
    # app.register_blueprint(main)


    with app.app_context():
        db.create_all()

    return app