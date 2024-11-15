from idlelib.pyparse import trans
from logging import exception

'''1.Определение базового класса BankAccount:'''

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print(f'Депозит увеличен на {amount}')
            else:
                 print(f'недопустимая сумма депозита {amount}')

    def withdraw(self,amount):
        try:
            if -amount > account.__balance:
                raise ValueError('Сумма снятия больше баланса')
            self.__balance += amount
            print(f'Снятие {amount} произошло успешно')
        except ValueError as error:
            print(error)

    def get_balance(self):
        print(f'Баланс владельца {account.owner} = {self.__balance}')


'''Шаг 2: cоздание класса SavingsAccount (наследуется от BankAccount):'''

class SavingsAccount(BankAccount):
    def __init__(self, owner,balance=0):
        super().__init__(owner,balance)

    def apply_interest(self):
        interest_rate = self._BankAccount__balance + (self._BankAccount__balance * 0.05)
        print(f'После начисления процента по счету, Баланс = {interest_rate}')


class CheckingAccount(BankAccount):
    def __init__(self, owner,balance=0):
        super().__init__(owner,balance)

    def withdraw(self,amount):
        self.__balance += amount
        print(f'Снятие {amount} произошло успешно')


account = SavingsAccount('Otis')

transactions = (500,-100)

for transaction in (transactions):
    if transaction > 0:
        account.deposit(transaction)
    else:
        account.withdraw(transaction)


account.get_balance()

account.apply_interest()