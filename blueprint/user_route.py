from flask import Blueprint
from controller.user_controller import test_user, register_user, search_user, Update_user

user_bp = Blueprint('user', __name__)

user_bp.route('/user', methods=['GET'])(test_user)
user_bp.route('/users', methods=['POST'])(register_user)
user_bp.route('/users', methods=['GET'])(search_user)
user_bp.route('/users/<id>', methods=['PUT'])(Update_user)


# POST /users: Create a new user account
# GET /users/me: Retrieve the profile of the currently authenticated user.
# PUT /users/me: Update the profile information of thecurrently authenticated user