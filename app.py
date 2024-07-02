from flask import Flask
from connectors.mysql_connector import connection

from blueprint.user_route import user_bp
from blueprint.account_route import account_bp
from blueprint.transaction_route import transaction_bp
import os

from flask_login import LoginManager

from Models.users import User

from sqlalchemy.orm import sessionmaker
from datetime import timedelta

from dotenv import load_dotenv

from flasgger import Swagger

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)


swagger = Swagger(app)

app.register_blueprint(user_bp)
app.register_blueprint(account_bp)
app.register_blueprint(transaction_bp)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(users_id):
     Session = sessionmaker(connection)
     s = Session()
     return s.query(User).get(int(users_id))



@app.route('/')
def hello_world():
    return "Hello World"