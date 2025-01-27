class BankAccount:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


if __name__ == '__main__':
    account = BankAccount('Nabeel', 1000)
    account.deposit(500)
    print(f'Your total balance is {account.get_balance()}')
