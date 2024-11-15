from task2 import SavingsAccount

acc_primer = SavingsAccount('Tom')

def test_add():
    transactions = (-600,-900)
    for transaction in (transactions):
        if transaction > 0:
            acc_primer.deposit(transaction)
        else:
            acc_primer.withdraw(transaction)

acc_primer.get_balance()

acc_primer.apply_interest()