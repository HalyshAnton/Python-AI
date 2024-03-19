class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        """
        Кладе додаткові кошти на рахунок
        :param amount: (int, float) кількість коштів, які
        додаткова поклали на рахунок
        :return: None
        """
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів на рахунок")


account = BankAccount(100)

print('Початок')
print(account.get_balance())

print('добавили 55 грн')
account.deposit(55)
print(account.get_balance())

print('зняли 60 грн')
account.withdraw(60)
print(account.get_balance())

print('зняли 200 грн')
account.withdraw(200)
print(account.get_balance())

account.__balance