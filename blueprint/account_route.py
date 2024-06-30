from flask import Blueprint
from controller.account_controller import test_account

account_bp = Blueprint('account', __name__)

account_bp.route('/account', methods=['GET'])(test_account)