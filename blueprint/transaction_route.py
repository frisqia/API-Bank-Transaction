from flask import Blueprint
from controller.transaction_controller import test_transaction, fetch_transaction, create_transaction, search_transaction

from flask_login import login_required

def login_required_blueprint(bp):
    original_add_url_rule = bp.add_url_rule

    def new_add_url_rule(rule, endpoint=None, view_func=None, **options):
        view_func = login_required(view_func)
        return original_add_url_rule(rule, endpoint, view_func, **options)

    bp.add_url_rule = new_add_url_rule
    return bp

transaction_bp = Blueprint('transactions', __name__)
transaction_bp = login_required_blueprint(transaction_bp)

transaction_bp.route('/transaction', methods=['GET'])(test_transaction)
transaction_bp.route('/transactions', methods=['GET'])(fetch_transaction)
transaction_bp.route('/transactions', methods=['POST'])(create_transaction)
transaction_bp.route('/transactions/<id>', methods=['GET'])(search_transaction)



# GET /transactions: Retrive a list of all transactions for the currently authenticated user's accounts. (Optional: filter by account ID, date range).
# GET /transactions/:id: Retrieve details of a specific transaction by its ID.(Authorization required for related account owner).
# POST /transactions: Initiate a new transaction (deposit, withdrawal, or transfer),(Authorization required for related account owner).