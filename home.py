from budget import Budget
class Home(Budget):
    def __init__(self, amnt, balance):
        self.home_exp = amnt
        if Budget.balance == 0:
            Budget.balance = balance
        print (f"{self.home_exp},{Budget.balance}")
    
    def home_budget(self, amnt):
        if self.home_exp != 0:
            return (int(self.home_exp) / int(amnt)) * 100
        else:
            print("No food expenses this month")

