from flask import Flask

from blueprint.user_route import user_bp
from blueprint.account_route import account_bp
from blueprint.transaction_route import transaction__bp
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(user_bp)
app.register_blueprint(account_bp)
app.register_blueprint(transaction__bp)

@app.route('/')
def hello_world():
    return "Hello World"