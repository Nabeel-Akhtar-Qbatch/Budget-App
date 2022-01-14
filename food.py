from budget import Budget

class Food(Budget):
    def __init__(self, amnt, balance):
        self.food_exp = amnt
        super().__init__(balance)

    def food_budget(self, amnt):
        if self.food_exp != 0:
            return (float(self.food_exp) / float(self.amount)) * 100
        else:
            print("No food expenses this month")

