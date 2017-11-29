"""
This app helps to control your own finances, your wallet.
    It contains accounts, period of the your money spends,
    transactions with date, value and categories of spends.
    Also it contains functions with count your spends on average.
    App connects to database and makes a manipulation with data, after that returns the data to db.

"""

from datetime import datetime
import ast
from decimal import *

class Account(object):
    # var name always is string, var value is number
    def __init__(self, name, value):
        self.account_name = name
        self.account_value = value

class Transaction(object):
    # var name always is string, var value is number, account is object of Account class
    def __init__(self, value, account,category):
        self.transaction_name = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self.transaction_value = value
        self.transaction_account = account
        self.category = category

class Wallet(object):
    transaction_list = {}
    account_list = {}
    category_list = {}

    def add_account(self,account):
        self.account_list[account.account_name] = str(account.account_value)

    def add_transaction(self, transaction):
        tr_cell = self.transaction_list[transaction.transaction_name] = {}
        tr_cell["value"]  = str(transaction.transaction_value)
        tr_cell["category"] = transaction.category
        tr_cell['account'] = transaction.transaction_account

    def spend(self,account,transaction):
        decimal_account = Decimal(account).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        decimal_transaction = Decimal(transaction).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        return  str(decimal_account-decimal_transaction)

    

wallet = Wallet()


