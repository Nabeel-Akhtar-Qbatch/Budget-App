from budget import Budget

class Travel(Budget):
    def __init__(self, amnt, balance):
        self.trav_exp = amnt
        super().__init__(balance)
    
    def travel_budget(self, amnt):
        if self.trav_exp != 0:
            return (float(self.trav_exp) / float(self.amount)) * 100
        else:
            print("No Travel expenses this month")

