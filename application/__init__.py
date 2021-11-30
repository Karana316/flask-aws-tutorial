from flask import Flask
from flask_bootstrap import Bootstrap
from application.extensions import db, migrate
from . import models

# create and bootstrap the application
application = Flask(__name__)
application.config.from_object('config')
bootstrap = Bootstrap(application)

# init and create the db
db.init_app(application)
migrate.init_app(application, db)

# comment out the migrate.init_app line above and uncomment the two lines below if you don't want to test
# using flask_migrate. The create_all below will create tables that don't exist (no drops, no changes).
# with application.app_context():
#    db.create_all()

# this has to be relative or it overwrites the Flask application object/variable with the module itself
# it also has to be last because the app has to be created before the decorator in views.py can register the views.
from . import views

