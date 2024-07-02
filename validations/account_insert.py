def coerce_decimal(value):
    try:
        return round(float(value), 2)
    except (ValueError, TypeError):
        return value

account_insert_schema = {
    'user_id' : {'type': 'integer', 'required': True, 'empty':False},
    'account_type' : {'type':'string','required': True, 'empty': False, 'allowed': ["Checking", "Savings", "CDs", "Money Market", "Foreign Currency"]},
    'account_number': {'type': 'string', 'required':True, 'empty': False},
    'balance':{'type':'float', 'coerce': coerce_decimal}
}
