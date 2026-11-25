# LAB EXERCISE 14: Bank Account System Using OOP

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Amount withdrawn")

    def show_balance(self):
        print("Balance:", self.__balance)


a = BankAccount("Nivin", 5000)
a.deposit(1000)
a.withdraw(2000)
a.show_balance()
