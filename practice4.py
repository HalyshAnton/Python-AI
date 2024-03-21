class Bank:
    count = 0
    exchange_rate_usd_uah = 38

    def __init__(self):
        Bank.count += 1
        self.balance = 10

    @staticmethod
    def uah_to_usd(value_uah):
        print(Bank.exchange_rate_usd_uah)
        return value_uah / 38

    @classmethod
    def uah_to_usd2(cls, value_uah):
        return value_uah / cls.exchange_rate_usd_uah

    def set_balance(self, balance):
        self.balance = balance

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_exchange_rate(cls):
        return cls.exchange_rate_usd_uah


object1 = Bank()
#print(object1.uah_to_usd(1000))
#print(Bank.uah_to_usd(1000))
#print(Bank.get_exchange_rate())

#2

class Calculator:
    @staticmethod
    def add_numbers(num1, num2):
        return num1 + num2

    @classmethod
    def add_numbers_with_round(cls, num1, num2):
        num1 = round(num1)
        num2 = round(num2)
        return cls.add_numbers(num1, num2)


print(Calculator.add_numbers(1, 2))
print(Calculator.add_numbers_with_round(1.3, 5.075))
