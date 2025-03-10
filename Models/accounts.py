from Models.base import Base
from sqlalchemy.orm import mapped_column,relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.sql import func

class Account(Base):
    __tablename__ = 'accounts'

    id = mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id=mapped_column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    account_type=mapped_column(String(255))
    account_number=mapped_column(String(255), unique=True)
    balance=mapped_column(DECIMAL(10,2))
    created_at=mapped_column(DateTime(timezone=True), server_default=func.now())
    # updated_at=mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at=mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship('User', back_populates='accounts')
    transactions_from = relationship('Transaction', foreign_keys='Transaction.from_account_id', back_populates='from_account', cascade='all, delete-orphan')
    transactions_to = relationship('Transaction', foreign_keys='Transaction.to_account_id', back_populates='to_account',cascade='all, delete-orphan')

# id:(INT,Primary Key)Unique identifier for the account.
# user_id:(INT,Foreign Key references Users.id) User associated with the account
# account_type:(VARCHAR(255)) Type of account(e.g., checking, savings).
# account_number:(VARCHAR(255),Unique) Unique account number.
# balance:(DECIMAL(10,2)) Current balance of the account.
# created_at:(DATETIME) Timestamp of account creation.
# update_at:(DATETIME) Timestamp of account information update.