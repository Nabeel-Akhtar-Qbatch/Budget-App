from datetime import datetime

class Budget():
    balance = 0
    "Class of maintaining mounthly budget"
    def __init__ (self, amount):
        self.amount += amount
        Budget.balance = amount
    
    def check_fund(self, amount):
        if self.amount < amount: return True
        else: return False
    
    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if self.check(amount) == True:
            self.amount -= amount
            return True
        else: return False
        
        