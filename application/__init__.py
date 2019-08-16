from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '1234567890abcdef'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes