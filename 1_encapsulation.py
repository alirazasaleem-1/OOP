# Task 1: ENCAPSULATION

class BankAccount:

    def __init__(self, owner_name= None, balance = 0):
        self.owner_name = owner_name
        self.__balance = balance 
    
    def deposit(self, amount):
        self.__balance += amount 
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount 
        else:
            print("Insufficient Balance")
    
    def get_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount("Ali", 2000)
account.deposit(1000)