from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Shell
from app import app, db
from models import Person



manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

