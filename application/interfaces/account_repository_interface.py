from abc import ABC, abstractmethod


class AccountRepositoryInterface(ABC):
    @abstractmethod
    def save(self, account):
        pass

    @abstractmethod
    def find_by_id(self, account_id):
        pass

    @abstractmethod
    def find_accounts_by_customer_id(self, customer_id):
        pass
