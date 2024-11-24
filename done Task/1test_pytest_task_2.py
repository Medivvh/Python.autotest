import random
import pytest
from task2 import SavingsAccount

def test_add_positive():
    account = SavingsAccount('Andrey', 0)
    account.deposit(random.randint(1, 1000))
    assert account._BankAccount__balance > 0

def test_add_negative():
    account = SavingsAccount('Andrey', 0)
    with pytest.raises(ValueError):
        price = random.randint(1, 1000)
        account.withdraw(price)
        raise ValueError


def test_add_negative_zero():
    account = SavingsAccount('Andrey', 0)
    with pytest.raises(ValueError):
        account.withdraw(0)
        raise ValueError