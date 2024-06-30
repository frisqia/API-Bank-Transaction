from flask import request
from connectors.mysql_connector import connection
from Models.accounts import Account
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

def test_account():
    return 'account'

def fetch_account():
    account_fetch = select(Account)
    Session = sessionmaker(connection)
    s = Session()
    try:
        result = s.execute(account_fetch)
        accounts=[]
        for row in result.scalars():
            accounts.append({
                'ID': row.id,
                'User ID':row.user_id,
                'Type': row.account_type,
                'Number': row.account_number,
                'Balance': row.balance,
                'Register Time': row.created_at,
                'Update register': row.updated_at
            })
            print(f'ID: {row.id},User: {row.user_id}, Type: {row.account_type}, Number: {row.account_number}, Balance: {row.balance}, Register Time {row.created_at}, Updated Time {row.updated_at}')
        return{
            'data':accounts
        }
    except Exception as e:
        print(e)
        return{'message':'Fail to fetch accounts'},500
    
