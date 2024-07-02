def coerce_decimal(value):
    try:
        return round(float(value), 2)
    except (ValueError, TypeError):
        return value

transaction_insert_schema = {
    'from_account_id' : {'type': 'integer', 'required': True, 'empty':False},
    'to_account_id' : {'type':'integer','required': True, 'empty': False},
    'amount': {'type':'float', 'coerce': coerce_decimal, 'required':True, 'empty': False},
    'type':{'type': 'string', 'required': True,'empty':False, 'allowed': ['Deposits','Withdrawals','Transfers','Loans and Credits','Bill Payments','Foreign Exchange Transactions','Fees and Service Charges','Interest Payments']},
    'description':{'type': 'string'}
}

