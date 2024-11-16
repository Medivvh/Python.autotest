from unittest import removeResult

from task2 import SavingsAccount, transactions, transaction

account = SavingsAccount('Tom')



def test_add():
    transactions = (800, -800, 0, 600, -6000)
    for transaction in (transactions):
        if transaction > 0:
            account.deposit(transaction)
            assert account._BankAccount__balance > 0, ValueError
        elif transaction < 0:
            account.withdraw(transaction)
            assert account._BankAccount__balance >= 0, ValueError

        else:
            print(f'Баланс не изменился, сумма транзакции = {transaction}')


account.apply_interest()
account.get_balance()
