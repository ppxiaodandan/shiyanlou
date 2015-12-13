from flask.ext.sqlalchemy import sqlAlchemy
db = sqlAlchemy()

from flask.ext.cache import Cache
cache=Cache()

from flask.ext.login import LoginManager
login_manager= LoginManager()
