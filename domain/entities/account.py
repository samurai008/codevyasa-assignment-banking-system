import datetime
from domain.value_objects.transaction import Transaction


class Account:
    def __init__(self, account_id, customer, balance=0):
        self.account_id = account_id
        self.customer = customer
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self._record_transaction(amount, "Deposit", datetime.datetime.now())

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record_transaction(amount, "Withdrawal", datetime.datetime.now())

    def _record_transaction(self, amount, transaction_type, timestamp):
        transaction = Transaction(
            self.account_id, amount, transaction_type, timestamp)
        self.transactions.append(transaction)

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transactions
