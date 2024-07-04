from flask import request
from sqlalchemy import select
from Models.users import User
from Connectors.mysql_connector import (connection)
from sqlalchemy.orm import sessionmaker

from cerberus import Validator
from validations.user_insert import user_insert_schema

from flask_login import login_user, logout_user,current_user

from flasgger import swag_from
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

@swag_from(os.path.join(current_dir, '..', 'Api_Doc','user', 'test_user.yml'))
def test_user():
    return 'user'


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','user', 'register_user.yml'))
def register_user():


    v = Validator(user_insert_schema)
    request_body = {
        'username': request.form['username'],
        'email' : request.form['email'],
        'password_hash' : request.form['password']
     }
    
    if not v.validate(request_body):
        return{'error': v.errors}, 489

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
        
        print(f'ID: {register["ID"]} Name: {register["Name"]} Email: {register["Email"]} Register Time: {register["Register Time"]} Update Time: {register["Update Time"]}')

        return {
            'message': 'Register Success',
            'New User': register
            }, 201
    except Exception as e:
        print(e)
        s.rollback()
        return{'message': 'Fail to Register'}, 403
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','user', 'login_user.yml'))
def user_login():
    Session = sessionmaker(connection)
    s = Session()
    s.begin()

    try:
        login = request.form['email']
        password = request.form['password']

        user = s.query(User).filter((User.email == login) | (User.username == login)).first()

        if user is None:
            return {"message": "User not found"}, 404

        if not user.check_password(password):
            return {"message": "Invalid password"}, 403

        login_user(user)
        session_id = request.cookies.get('session')  
        
        user_info = {
            "ID": user.id,
            "Name": user.username,
            "Email": user.email,
            "Register Time": user.created_at,
            "Update Time": user.updated_at
        }

        print(f'User ID: {user_info["ID"]} Name: {user_info["Name"]} Email: {user_info["Email"]} Register Time: {user_info["Register Time"]} Update Time: {user_info["Update Time"]}')

        return {
            "message": "Login successful",
            "session_id": session_id, 
            "user": user_info
        }, 200
            
    except Exception as e:
        print(e)
        s.rollback()
        return {"message": "Fail to login"}, 400
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','user', 'profile_user.yml'))
def profile_user():
    Session = sessionmaker(connection)
    s = Session()                                                                              
    try:
        user = current_user

        user_profile = {
            'ID': user.id,
            'Name': user.username,
            'Email': user.email,
            'Register Time': user.created_at,
            'Update Time': user.updated_at
        }
        print(f'ID: {user.id}, Name: {user.username}, Email: {user.email}, Register Time: {user.created_at}, Updated Time: {user.updated_at}')
        return{
            'users':user_profile,
            'message':'Your Profile'
        }, 200
    except Exception as e:
        print(e)
        return{'message': 'Fail to retrieve profile'}, 400
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','user', 'update_user.yml'))   
def Update_user():
    session= sessionmaker(connection)
    s = session()
    s.begin()
    try:
        update_data = s.query(User).filter(User.id == current_user.id).first()
        
        if update_data is None:
            return {'message': 'User not found'}, 404
        if 'username' in request.form:
            update_data.username = request.form['username']

        if 'email' in request.form:
            update_data.email = request.form['email']

        if 'password' in request.form:
            update_data.set_password(request.form['password'])

        s.commit()
        
        updated_user = {
            'ID': update_data.id,
            'Name': update_data.username,
            'Email': update_data.email,
            'Register Time': update_data.created_at,
            'Update Time': update_data.updated_at
        }

        return {
            'message': 'Update successful',
            'Updated User': [updated_user]
        }, 200
    except Exception as c:
        print(c)
        s.rollback()
        return{'message':'fail to update'},400
    finally:
        s.close()


@swag_from(os.path.join(current_dir, '..', 'Api_Doc','user', 'logout_user.yml'))   
def user_logout():
    logout_user()
    return { "message": "Success logout" },200