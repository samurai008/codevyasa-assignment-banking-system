from application.services.account_statement_service import AccountStatementService
from domain.entities.customer import Customer
from application.services.account_service import AccountService
from infrastructure.persistence.repositories.account_repository import AccountRepository


def main():
    account_repository = AccountRepository()

    account_service = AccountService(account_repository)
    account_statement_service = AccountStatementService(account_repository)

    customer = Customer(customer_id=1, name="Jane Doe",
                        email="jane.doe@foobar.com", phone_number="9998887771")
    customer2 = Customer(customer_id=2, name="John Doe",
                         email="john.doe@foobar.com", phone_number="8889991110")

    new_account = account_service.create_account(customer)
    new_account_2 = account_service.create_account(customer2)

    # Perform some transactions
    account_service.make_transaction(
        account_id=new_account.account_id, amount=1000, transaction_type='deposit')
    account_service.make_transaction(
        account_id=new_account.account_id, amount=200, transaction_type='withdraw')

    account_service.make_transaction(
        account_id=new_account_2.account_id, amount=500, transaction_type='deposit')
    account_service.make_transaction(
        account_id=new_account_2.account_id, amount=100, transaction_type='withdraw')

    # Generate account statements
    print(account_statement_service.generate_account_statement(
        new_account.account_id) + "\n")

    print(account_statement_service.generate_account_statement(
        new_account_2.account_id))


if __name__ == "__main__":
    main()
