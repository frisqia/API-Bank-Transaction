from flask import request
from sqlalchemy import select
from Models.users import User
from connectors.mysql_connector import (connection)
from sqlalchemy.orm import sessionmaker



# from flask_login import logout_user

from flask_jwt_extended import create_access_token, jwt_required, get_jwt


def test_user():
    return 'user'

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
        
        register = {
            'ID' : register.id,
            'Name' : register.username,
            'Email' : register.email,
            'Register Time' : register.created_at,
            'Update Time' : register.updated_at

        }

        return {
            'message': 'Register Success',
            'New User': register
            }, 201
    except Exception as e:
        print(e)
        s.rollback()
        return{'message': 'Fail to Register'}, 500
    finally:
        s.close()

def user_login():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()

    try:
        login = request.form['login']
        password = request.form['password']

        user = s.query(User).filter((User.email == login) | (User.username == login)).first()

        if user is None:
            return {"message": "User not found"}, 403

        if not user.check_password(password):
            return {"message": "Invalid password"}, 403
        
        token = create_access_token(identity=user.id, additional_claims={'Name':user.username, 'User':user.id})

        return {
            "message": "Login successful", 
            "access": token,
            "user": {
            "ID": user.id,
            "Name": user.username,
            "Email": user.email,
            "Register Time": user.created_at,
            "Update Time": user.updated_at
        }}, 200
    
    

    except Exception as e:
        print(e)
        s.rollback()
        return {"message": "Fail to login"}, 500
    finally:
        s.close()
    
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
                'Register Time' : row.created_at,
                'Update Time' : row.updated_at
            })
            print(f'ID: {row.id}, Name: {row.username}, Email: {row.email}, Register Time: {row.created_at}, Updated Time: {row.updated_at}')
        return{
            'users':user
        }
    except Exception as e:
        print(e)
        return{'message': 'Fail to Register'}, 500
    finally:
        s.close()
    
def Update_user(id):
    session= sessionmaker(connection)
    s = session()
    s.begin()
    try:
        update_data = s.query(User).filter(User.id == id).first()

        update_data.username = request.form['username']
        update_data.email = request.form['email']
        update_data.set_password(request.form['password'])
        s.commit()

        New_data = {
            'ID': update_data.id,
            'Username': update_data.username,
            'Email': update_data.email,
            'Register Time': update_data.created_at,
            'Update Time': update_data.updated_at
        }
        return{
            'message':'succes update data',
            'User' : New_data
            },200
    except Exception as c:
        print(c)
        s.rollback()
        return{'message':'fail to update'},500
    finally:
        s.close()
    
# def user_logout():
#     jti = get_jwt()['jti']
#     current_app.blacklist.add(jti)
#     return {"message": "Successfully logged out"}, 200