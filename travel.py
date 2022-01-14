from budget import Budget
class Travel(Budget):
    def __init__(self, amnt, balance):
        self.trav_exp = amnt
        if Budget.balance == 0:
            Budget.balance = balance
        print (f"{self.trav_exp},{Budget.balance}")
    
    def travel_budget(self, amnt):
        if self.trav_exp != 0:
            return (int(self.trav_exp) / int(amnt)) * 100
        else:
            print("No Travel expenses this month")

