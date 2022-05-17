<<<<<<< HEAD

from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role
from  flask_migrate import Migrate, MigrateCommand
=======
from app import create_app, db
from flask_script import Manager, Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User
>>>>>>> cbdd7d94a3e6113c55013b9e886dd7e6a60d59fc
from flask_wtf.csrf import CSRFProtect



# Creating app instance
app = create_app('development')
csrf = CSRFProtect(app)
<<<<<<< HEAD
app.config['SECRET_KEY'] = "secretkey"
app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
csrf.init_app(app)

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role=Role )

=======
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
>>>>>>> cbdd7d94a3e6113c55013b9e886dd7e6a60d59fc

if __name__ == '__main__':
    manager.run()
