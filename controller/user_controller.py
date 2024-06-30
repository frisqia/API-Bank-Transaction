from flask import request
from sqlalchemy import select
from Models.users import User
from connectors.mysql_connector import (connection)
from sqlalchemy.orm import sessionmaker

def test_user():
    return 'user'

# register
def register_user():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()                                                                                
    try:
        register = User(
            email = request.form ['email'],
            username = request.form ['username']
      )
        register.set_password(request.form['password'])
        s.add(register)
        s.commit()
        return {'message': 'Register Success'}, 201
    except Exception as e:
        print(e)
        s.rollback()
        return{'message': 'Fail to Register'}, 500
    

def search_user():
    Session = sessionmaker(connection)
    s = Session()                                                                              
    try:
        User_me = select(User)
        keyword = request.args.get('query')
        if keyword !=None:
            User_me = User_me.where(User.username.like(f'%{keyword}%'))
        user_result = s.execute(User_me)
        user=[]
        for row in user_result.scalars():
            user.append({
                'ID' : row.id,
                'Name' : row.username,
                'Email' : row.email,
                'Register Time' : row.created_at
            })
            print(f'ID: {row.id}, Name: {row.username}, Email: {row.email}, Register Time: {row.created_at}')
        return{
            'users':user
        }
    except Exception as e:
        print(e)
        return{'message': 'Fail to Register'}, 500
    
def Update_user():
    try
        
    except