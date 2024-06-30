# from Models import base
# from sqlalchemy.orm import mapped_column
# from sqlalchemy import Integer, String, DateTime, ForeignKey, DECIMAL
# from sqlalchemy.sql import func

# class Account(base):
#     __tablename__ = 'accounts'

#     id = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
#     user_id=mapped_column(Integer, ForeignKey('users.id',ondelete="CASCADE"))
#     account_type=mapped_column(String(255))
#     account_number=mapped_column(String(255))
#     balance=mapped_column(DECIMAL(255))
#     created_at=mapped_column(DateTime(timezone=True), server_default=func.now())
#     update_at=mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())



# id:(INT,Primary Key)Unique identifier for the account.
# user_id:(INT,Foreign Key references Users.id) User associated with the account
# account_type:(VARCHAR(255)) Type of account(e.g., checking, savings).
# account_number:(VARCHAR(255),Unique) Unique account number.
# balance:(DECIMAL(10,2)) Current balance of the account.
# created_at:(DATETIME) Timestamp of account creation.
# update_at:(DATETIME) Timestamp of account information update.

