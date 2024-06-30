from flask import Blueprint
from controller.user_controller import test_user

user_bp = Blueprint('user', __name__)

user_bp.route('/user', methods=['GET'])(test_user)