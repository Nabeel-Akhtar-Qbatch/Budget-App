from budget import Budget

class Home(Budget):
    def __init__(self, amnt, balance):
        self.home_exp = amnt
        super().__init__(balance)
    
    def home_budget(self, amnt):
        if self.home_exp != 0:
            return (float(self.home_exp) / float(self.amount)) * 100
        else:
            print("No food expenses this month")

