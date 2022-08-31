from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)

from models import *


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

admin = Admin(app)

admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))

# Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
Security = Security(app, user_datastore)
