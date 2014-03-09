from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdf09ag0w4ngq0n4g000q43y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///db.sqlite3'
login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
import views
