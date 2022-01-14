from budget import Budget

class Food(Budget):
    def __init__(self, amnt, balance):
        self.food_exp = amnt
        if Budget.balance == 0:
            Budget.balance = balance
        
    def food_budget(self, amnt):
        if self.food_exp != 0:
            return (int(self.food_exp) / int(amnt)) * 100
        else:
            print("No food expenses this month")

