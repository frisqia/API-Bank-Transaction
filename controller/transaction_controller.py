from flask import request


from Models.transactions import Transaction
from Models.accounts import Account

from connectors.mysql_connector import connection
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from decimal import Decimal

def test_transaction():
    return 'transaction'

def fetch_transaction():
    list_transaction = select(Transaction)
    Session= sessionmaker(connection)
    s = Session()
    try:
        list = s.execute(list_transaction)
        transaction=[]
        for row in list.scalars():
            transaction.append({
                'ID': row.id,
                'Account ID': row.from_account_id,
                'Update ID': row.to_account_id,
                'Amount': row.amount,
                'Type': row.type,
                'Description': row.description,
                'Transaction Time': row.created_at
            })
        print(f'ID: {row.id} Account ID: {row.from_account_id} Update ID: {row.to_account_id} Amount: {row.amount} Type: {row.type} Descrption: {row.description} Transaction Time: {row.created_at}')
        return{
            'message': 'all data is',
            'data':transaction
        },201
    except Exception as t:
        print(t)
        return {'message': 'fail to fetch Transaction'}, 500
    finally:
        s.close()


def create_transaction():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()
    try:
        from_account_id = request.form['from_account_id']
        to_account_id = request.form['to_account_id']
        amount = Decimal(request.form['amount']) 

        if from_account_id == to_account_id:
            return {'message': 'From and To account cannot be the same'}, 400

        from_account = s.query(Account).filter(Account.id == from_account_id).first()
        to_account = s.query(Account).filter(Account.id == to_account_id).first()

        if not from_account or not to_account:
            return {'message': 'From or To account does not exist'}, 400

        if from_account.balance < amount:
            return {'message': 'Insufficient funds in From account'}, 400

        from_account.balance -= amount
        to_account.balance += amount

        NewTransaction = Transaction(
            from_account_id=from_account_id,
            to_account_id=to_account_id,
            amount=amount,
            type=request.form['type'],
            description=request.form['description'],
        )
        s.add(NewTransaction)

        s.commit()

        NewTransaction = {
            'ID': NewTransaction.id,
            'From Account ID': NewTransaction.from_account_id,
            'To Account ID': NewTransaction.to_account_id,
            'Amount': NewTransaction.amount,
            'Type': NewTransaction.type,
            'Description': NewTransaction.description,
            'Time': NewTransaction.created_at,
        }

        print(f'ID: {NewTransaction['ID']} From Account ID: {NewTransaction['From Account ID']} To Account ID: {NewTransaction['To Account ID']} Amount: {NewTransaction['Amount']} Type: {NewTransaction['Type']} Description: {NewTransaction['Description']} Time: {NewTransaction["Time"]}')
        return {
            'message': 'Transaction success',
            'transaction': NewTransaction
            }, 201
    

    except Exception as t:
        print(t)
        s.rollback()
        return {'message': 'Failed to create transaction'}, 400
    finally:
        s.close()

def search_transaction(id):
    Session = sessionmaker(connection)
    s = Session()
    try:
        details = select(Transaction).where(Transaction.id == id)
        keyword = request.args.get('query')
        if keyword is not None:
            details = details.where(Transaction.type.like(f'%{keyword}%'))
        
        transactions = s.execute(details)
        transaction_list = []
        for row in transactions.scalars():
            transaction_list.append({
                'ID': row.id,
                'From Account ID': row.from_account_id,
                'To Account ID': row.to_account_id,
                'Amount': row.amount,
                'Type': row.type,
                'Description': row.description,
                'Time': row.created_at,
            })
            print(f'ID: {row.id} From Account ID: {row.from_account_id} To Account ID: {row.to_account_id} Amount: {row.amount} Type: {row.type} Description: {row.description} Time: {row.created_at}')
        
        if transaction_list:
            return {
                'detail': transaction_list,
                'message': 'Data found'
            }
        else:
            return {
                'detail': [],
                'message': 'No data found'
            }

    except Exception as a:
        print(a)
        return {'message': 'Fail to Search data'}
    finally:
        s.close()