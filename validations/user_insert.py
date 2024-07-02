user_insert_schema = {
    'username' : {'type': 'string', 'required': True, 'empty':False, 'minlength':3},
    'email' : {'type':'string','required': True, 'empty': False, 'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
    'password_hash': {'type': 'string', 'required':True, 'empty': False, 'minlength': 6, 'maxlength': 6 }
}