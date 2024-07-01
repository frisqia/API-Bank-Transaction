from flask import request

from Models.accounts import Account
from Models.users import User

from connectors.mysql_connector import connection
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
            print(f'ID: {row.id} User: {row.user_id} Type: {row.account_type} Number: {row.account_number} Balance: {row.balance} Register Time {row.created_at} Updated Time {row.updated_at}')
        return{
            'message': 'all data is',
            'data':accounts
        },201
    except Exception as e:
        print(e)
        return{'message':'Fail to fetch accounts'},404
    finally:
        s.close()
    
def insert_account():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        user_id = request.form['user_id']
        user = s.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("User ID does not exist")
        
        NewAccount = Account(
            user_id=user_id,
            account_type=request.form['account_type'],
            account_number=request.form['account_number'],
            balance=request.form['balance']
        )
        s.add(NewAccount)
        s.commit()

        NewAccount = {
            'ID': NewAccount.user_id,
            'Type': NewAccount.account_type,
            'Number': NewAccount.account_number,
            'Balance': NewAccount.balance,
            'Register Time': NewAccount.created_at,
            'Update Time': NewAccount.updated_at
        }
        print(f'ID: {NewAccount["ID"]} Type: {NewAccount["Type"]} Number: {NewAccount["Number"]} Balance: {NewAccount["Balance"]} Register Time: {NewAccount["Register Time"]} Update Time: {NewAccount["Update Time"]}')
        return {
            'message':'succes cresate account',
            'created':NewAccount
            },201
    except Exception as c:
        print(c)
        s.rollback()
        return{'message':'Fail to create account'}, 404
    finally:
        s.close()


def search_account(id):
    Session = sessionmaker(connection)
    s = Session()
    try:
        details = select(Account).where(Account.id == id)
        keyword = request.args.get('query')
        if keyword != None:
            details= details.where(Account.account_type.like(f'%{keyword}%'))
        account = s.execute(details)
        accounts=[]
        for row in account.scalars():
            accounts.append({
                'ID':row.id,
                'User ID': row.user_id,
                'Type': row.account_type,
                'Number':row.account_number,
                'balance':row.balance,
                'Register Time':row.created_at,
                'Update Time':row.updated_at
            })
            print(f'ID: {row.user_id} Type: {row.account_type} Number: {row.account_number} Balance: {row.balance} Register Time: {row.created_at} Updated Time: {row.updated_at}')
        
        if accounts:
            return {
                'detail': accounts,
                'message': 'Data found'
                }
        else:
            return {
                'detail': [],
                'message': 'No data found for the given user ID or query'}

    except Exception as a:
        print(a)
        return{'message': 'Fail to Search data'}
    finally:
        s.close()

def update_data(id):
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        update = s.query(Account).filter(Account.id == id).first()
        
        update.account_type = request.form['Type']
        update.account_number = request.form['Number']
        update.balance= request.form['Balance']

        if not update:
             return {'message': 'Account not found'}, 404

        s.commit()
        
        updated_account = {
            'ID': update.user_id,
            'Type': update.account_type,
            'Number': update.account_number,
            'Balance': update.balance,
            'Register Time': update.created_at,
            'Update Time': update.updated_at
        }
        print(f'ID: {updated_account["ID"]} Type: {updated_account["Type"]} Number: {updated_account["Number"]} Balance: {updated_account["Balance"]} Register Time: {updated_account["Register Time"]} Update Time: {updated_account["Update Time"]}')

        
        return {
            'message': 'Account updated successfully',
            'account': updated_account}, 201

    except Exception as c:
        print(c)
        return{'message':'fail to update'},404
    finally:
        s.close()
    
def delete_acount(id):
    Session=sessionmaker(connection)
    s= Session()
    s.begin()
    try:
        Data= s.query(Account).filter(Account.id == id).first()

        if not Data:
            return {'message': 'Account not found'}, 404

        user_id = Data.user_id        
        s.delete(Data)
        s.commit()

        remaining_accounts = s.query(Account).filter(Account.user_id == user_id).all()

        if not remaining_accounts:
            user = s.query(User).filter(User.id == user_id).first()
            if user:
                s.delete(user)
                s.commit()

        return{'message':'Success to delete'},201
    except Exception as c:
        print(c)
        s.rollback()
        return{'message':'fail to delete'},404
    finally:
        s.close()