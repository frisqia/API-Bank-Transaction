from Models.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func



class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = mapped_column(String(255), unique=True)
    email = mapped_column(String(255))
    password_hash = mapped_column(String(255))
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_at = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), onupdate=func.now())

# id:(INT,Primary Key) unique identifier for the user
# unsername:(VARCHAR(255),unique) Unsername for login
# email: (VARCHAR(255)) user's email address
# password_hash:(VARCHAR(255)) securely hashed user password
# created_at:(DATETIME) Timestamp of user creation
# updated_at:(DATETIME) Timestamp of user information update