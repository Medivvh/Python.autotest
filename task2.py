from logging import exception

'''1.Определение базового класса BankAccount:'''

class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Депозит на сумму {amount}, произошёл успешно')
        else:
             print(f'недопустимая сумма депозита {amount}')

    def withdraw(self,amount):
        try:
            if -amount > account.__balance:
                raise ValueError('Сумма снятия больше баланса')
            self.__balance += amount
            print(f'Снятие {amount} произошло успешно')
        except ValueError as error:
            return (error)

    def get_balance(self):
        print(f'Баланс владельца {account.owner} = {self.__balance}')


'''2. Cоздание класса SavingsAccount (наследуется от BankAccount):'''

class SavingsAccount(BankAccount):
    def __init__(self, owner,balance = 0):
        super().__init__(owner,balance)
        self._BankAccount__balance = 0 #узнать поподробнее о строке

    def apply_interest(self):
        self._BankAccount__balance += self._BankAccount__balance * 0.05
        print(f'После начисления процента по счету, Баланс = {self._BankAccount__balance}')


'''3. Cоздание класса CheckingAccount'''

class CheckingAccount(BankAccount):
    def __init__(self, owner,balance = 0):
        super().__init__(owner,balance)

    def withdraw(self,amount):
        self.__balance += amount
        print(f'Снятие {amount} произошло успешно')


account = SavingsAccount('Otis')


transactions = (500,-100, 700, 800, 1300)

for transaction in (transactions):
    if transaction > 0:
        account.deposit(transaction)
    else:
        account.withdraw(transaction)

account.apply_interest()
account.get_balance()