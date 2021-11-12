from src.app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

app_env = os.environ.get("APP_SETTINGS")
app = create_app(app_env)

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
