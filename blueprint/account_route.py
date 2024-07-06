from flask import Blueprint
from controller.account_controller import  fetch_account, insert_account, search_account_by_id, update_data, delete_acount



from flask_login import login_required

def login_required_blueprint(bp):
    original_add_url_rule = bp.add_url_rule

    def new_add_url_rule(rule, endpoint=None, view_func=None, **options):
        view_func = login_required(view_func)
        return original_add_url_rule(rule, endpoint, view_func, **options)

    bp.add_url_rule = new_add_url_rule
    return bp

account_bp = Blueprint('accounts', __name__)
account_bp = login_required_blueprint(account_bp)


account_bp.route('/accounts', methods=['GET'])((fetch_account))
account_bp.route('/accounts', methods=['POST'])(insert_account)
account_bp.route('/accounts/<id>', methods=['GET'])((search_account_by_id))
account_bp.route('/accounts/<id>', methods=['PUT'])(update_data)
account_bp.route('/accounts/<id>', methods=['DELETE'])(delete_acount)


# GET /accounts: Retrieve a list of all accounts belonging to the currently authenticated user.
# GET /accounts/:id: Retrieve details of a specific account by its ID. (Authorization required for accoynt owner).
# POST /accounts: Create a new account for the currently authenticater user.
# PUT /account/:id: Update details of an existing account. (Authorization required for account owner).
# DELETE /account/:id: Delete an account. (Authorization required for account owner).