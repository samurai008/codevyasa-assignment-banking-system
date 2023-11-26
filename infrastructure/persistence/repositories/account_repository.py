from application.interfaces.account_repository_interface import AccountRepositoryInterface


class AccountRepository(AccountRepositoryInterface):
    def __init__(self):
        self.accounts = {}

    def save(self, account):
        self.accounts[account.account_id] = account

    def find_by_id(self, account_id):
        return self.accounts.get(account_id, None)

    def find_accounts_by_customer_id(self, customer_id):
        return [account for account in self.accounts.values() if account.customer.customer_id == customer_id]
