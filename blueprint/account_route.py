from flask import Blueprint
from controller.account_controller import test_account, fetch_account, insert_account, search_account, update_data, delete_acount

account_bp = Blueprint('accounts', __name__)

account_bp.route('/account', methods=['GET'])(test_account)
account_bp.route('/accounts', methods=['GET'])(fetch_account)
account_bp.route('/accounts', methods=['POST'])(insert_account)
account_bp.route('/accounts/<id>', methods=['GET'])(search_account)
account_bp.route('/accounts/<id>', methods=['PUT'])(update_data)
account_bp.route('/accounts/<id>', methods=['DELETE'])(delete_acount)


# GET /accounts: Retrieve a list of all accounts belonging to the currently authenticated user.
# GET /accounts/:id: Retrieve details of a specific account by its ID. (Authorization required for accoynt owner).
# POST /accounts: Create a new account for the currently authenticater user.
# PUT /account/:id: Update details of an existing account. (Authorization required for account owner).
# DELETE /account/:id: Delete an account. (Authorization required for account owner).