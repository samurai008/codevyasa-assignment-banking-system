class AccountStatementService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_by_id(account_id)
        if not account:
            return "Account not found"

        statement = f"Account Statement for {account_id}\n"
        statement += f"Customer: {account.customer.name}\n"
        statement += "Transactions:\n"
        for transaction in account.get_transaction_history():
            statement += f"  - {transaction}\n"
        statement += f"Current Balance: INR {account.get_balance()}"

        return statement
