from flask import Blueprint
from controller.user_controller import test_user, register_user, search_user, Update_user

user_bp = Blueprint('user', __name__)

user_bp.route('/user', methods=['GET'])(test_user)
user_bp.route('/register', methods=['POST'])(register_user)
user_bp.route('/users', methods=['GET'])(search_user)
user_bp.route('/users/<id>', methods=['PUT'])(Update_user)