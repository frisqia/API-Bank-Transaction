from Models.base import Base
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func

from flask_login import UserMixin

import bcrypt


class User(Base,UserMixin):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = mapped_column(String(255), nullable=False, unique=True)
    email = mapped_column(String(255),nullable=False,unique=True)
    password = mapped_column(String(255), nullable=True)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    accounts = relationship('Account', cascade='all, delete-orphan')

    # password yang sudah di encript
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # check hashingnya/ membandingkan password yang sudah di input dengan password yang atersimpan
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

# id:(INT,Primary Key) unique identifier for the user
# unsername:(VARCHAR(255),unique) Unsername for login
# email: (VARCHAR(255)) user's email address
# password_hash:(VARCHAR(255)) securely hashed user password
# created_at:(DATETIME) Timestamp of user creation
# updated_at:(DATETIME) Timestamp of user information update