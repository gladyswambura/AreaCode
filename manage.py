from app import create_app, db
from flask_script import Manager, Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User
from flask_wtf.csrf import CSRFProtect



# Creating app instance
app = create_app('development')
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = "glado123"
app.config['WTF_CSRF_SECRET_KEY'] = "glado123"
csrf.init_app(app)

manager=Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.shell
def makeshell():
    return dict(app=app,db=db, User=User)

if __name__ == '__main__':
    manager.run()
