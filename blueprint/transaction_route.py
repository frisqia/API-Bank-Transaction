from flask import Blueprint
from controller.transaction_controller import test_transaction, fetch_transaction, create_transaction

transaction_bp = Blueprint('transactions', __name__)

transaction_bp.route('/transaction', methods=['GET'])(test_transaction)
transaction_bp.route('/transactions', methods=['GET'])(fetch_transaction)
transaction_bp.route('/transactions', methods=['POST'])(create_transaction)



# GET /transactions: Retrive a list of all transactions for the currently authenticated user's accounts. (Optional: filter by account ID, date range).
# GET /transactions/:id: Retrieve details of a specific transaction by its ID.(Authorization required for related account owner).
# POST /transactions: Initiate a new transaction (deposit, withdrawal, or transfer),(Authorization required for related account owner).