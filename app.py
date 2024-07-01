from flask import Flask
from connectors.mysql_connector import connection

from blueprint.user_route import user_bp
from blueprint.account_route import account_bp
from blueprint.transaction_route import transaction_bp
import os

# from flask_login import LoginManager
# from flask_jwt_extended import JWTManager

# from Models import users

# from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(user_bp)
app.register_blueprint(account_bp)
app.register_blueprint(transaction_bp)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

# @login_manager.user_loader
# def load_user(user_id):
#     Session = sessionmaker(connection)
#     s = Session()
#     return s.query(users).get(int(user_id))

@app.route('/')
def hello_world():
    return "Hello World"