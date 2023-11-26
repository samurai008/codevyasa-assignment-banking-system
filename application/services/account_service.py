from domain.entities.account import Account
import uuid


class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer):
        account = Account(
            account_id=self._generate_account_id(), customer=customer)
        self.account_repository.save(account)
        return account

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type")
        self.account_repository.save(account)

    def _generate_account_id(self):
        return str(uuid.uuid4())
