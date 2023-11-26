class Transaction:
    def __init__(self, account, amount, transaction_type, timestamp):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: INR {self.amount}"
