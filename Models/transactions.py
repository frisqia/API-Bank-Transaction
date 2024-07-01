from Models.base import Base
from sqlalchemy.orm import mapped_column,relationship
from sqlalchemy import Integer,ForeignKey, String, DateTime, DECIMAL
from sqlalchemy.sql import func

class Transaction(Base):
    __tablename__ = 'transactions'


    id= mapped_column(Integer, primary_key=True, autoincrement=True, unique=True)
    from_account_id=mapped_column(Integer, ForeignKey('accounts.id', ondelete="CASCADE"))
    to_account_id=mapped_column(Integer, ForeignKey('accounts.id',ondelete="CASCADE"))
    amount=mapped_column(DECIMAL(10,2))
    type=mapped_column(String(255))
    description=mapped_column(String(255))
    created_at=mapped_column(DateTime(timezone=True), server_default=func.now())

account = relationship('Account', back_populates='transactions')

# id:(INT,Primary Key)Unique identifier for the account.
# from_account_id:(INT, ForeignKey references Account.id) Account initiating the transaction(optional fro transfers)
# to_account_id:(INT, ForeignKey reference Account.id) Account receiving the transaction(optional for transfers)
# amount:(DECIMAL(10,2)) Transaction amount.
# type:(VARCHAR(255)) Type of transaction (e.g., deposit, withdrawal, transfer).
# description:(VARCHAR(255)) Optional description of the transaction.
# created_at:(DATETIME) Timestamp of transaction creation.