from flask import Blueprint
from controller.user_controller import register_user, user_login, profile_user, Update_user, user_logout

from flask_login import login_required

user_bp = Blueprint('user', __name__)

user_bp.route('/users', methods=['POST'])(register_user)
user_bp.route('/users/login', methods=['POST'])(user_login)
user_bp.route('/users/me', methods=['GET'])((profile_user))
user_bp.route('/users/me', methods=['PUT'])((Update_user))
user_bp.route('/users/logout', methods=['POST'])(login_required(user_logout))

# POST /users: Create a new user account
# GET /users/me: Retrieve the profile of the currently authenticated user.
# PUT /users/me: Update the profile information of thecurrently authenticated user