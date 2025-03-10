from flask import request

from Models.accounts import Account
from Models.users import User

from connectors.mysql_connector import connection
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker


from cerberus import Validator
from validations.account_insert import account_insert_schema
from flask_login import current_user

from flasgger import swag_from

import os
current_dir = os.path.dirname(os.path.abspath(__file__))


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','account', 'fetch_account.yml'))
def fetch_account():
    Session = sessionmaker(connection)
    s = Session()
    try:
        user_id = current_user.id
        accounts = s.query(Account).filter_by(user_id=user_id).all()

        if not accounts:
            return {"message": "No accounts found"}, 404

        user_account=[]

        for account in accounts:
            user_account.append({
                'ID': account.id,
                'User ID':account.user_id,
                'Type': account.account_type,
                'Number': account.account_number,
                'Balance': account.balance,
                'Register Time': account.created_at,
                'Update register': account.updated_at
            })
            print(f'ID: {account.id} User: {account.user_id} Type: {account.account_type} Number: {account.account_number} Balance: {account.balance} Register Time {account.created_at} Updated Time {account.updated_at}')
        
        return{
            'message': 'all data is',
            'data':user_account
        },200
    except Exception as e:
        print(e)
        return{'message':'Fail to fetch accounts'},400
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','account', 'insert_account.yml'))
def insert_account():

    v = Validator(account_insert_schema)
    request_body = {
        'account_type' : request.form['Type'],
        'account_number' : request.form['Number'],
        'balance' : request.form['Balance']
     }
    
    if not v.validate(request_body):
        return{'error': v.errors}, 489

    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        user_id = current_user.id
        user = s.query(User).filter(User.id == user_id).first()

        if not user:
            raise ValueError("User ID does not exist")
        
        New_Account = Account(
            user_id=user_id,
            account_type=request.form['Type'],
            account_number=request.form['Number'],
            balance=request.form['Balance']
        )
        s.add(New_Account)
        s.commit()

        New_Account = {
            'ID': New_Account.user_id,
            'Type': New_Account.account_type,
            'Number': New_Account.account_number,
            'Balance': New_Account.balance,
            'Register Time': New_Account.created_at,
            'Update Time': New_Account.updated_at
        }
        print(f'ID: {New_Account["ID"]} Type: {New_Account["Type"]} Number: {New_Account["Number"]} Balance: {New_Account["Balance"]} Register Time: {New_Account["Register Time"]} Update Time: {New_Account["Update Time"]}')
        return {
            'message':'succes create account',
            'created':New_Account
            },201
    except Exception as c:
        print(c)
        s.rollback()
        return{'message':'Fail to create account'}, 400
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','account', 'search_account.yml'))
def search_account_by_id(id):
    Session = sessionmaker(connection)
    s = Session()
    try:
        details = select(Account).where(Account.id== id)
        account = s.execute(details).scalar_one_or_none()

        if account:
            if account.user_id != current_user.id:
                return {'message': 'Unauthorized access'}, 403  
                      
            account_detail = {
                'ID': account.id,
                'User ID': account.user_id,
                'Type': account.account_type,
                'Number': account.account_number,
                'Balance': account.balance,
                'Register Time': account.created_at,
                'Update Time': account.updated_at
            }
            print(f'ID: {account.id} User ID: {account.user_id} Type: {account.account_type} Number: {account.account_number} Balance: {account.balance} Register Time: {account.created_at} Updated Time: {account.updated_at}')
            return {
                'detail': account_detail,
                'message': 'Data found'
            }, 200
        else:
            return {
                'detail': None,
                'message': 'No data found for the given user ID '},404

    except Exception as a:
        print(a)
        return{'message': 'Fail to Search data'},400
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','account', 'update_account.yml'))
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
        return{'message':'fail to update'},400
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','account', 'delete_account.yml'))    
def delete_acount(id):
    Session=sessionmaker(connection)
    s= Session()
    s.begin()
    try:
        Data= s.query(Account).filter(Account.id == id).first()
        s.delete(Data)
        s.commit()
        return{'message':'Success to delete'},200
    except Exception as c:
        print(c)
        s.rollback()
        return{'message':'fail to delete'},400
    finally:
        s.close()