from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from review.filters import show_stars, naturaltime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf09ag0w4ngq0n4g000q43y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///db.sqlite3'
app.jinja_env.filters['show_stars'] = show_stars
app.jinja_env.filters['naturaltime'] = naturaltime
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
import views
