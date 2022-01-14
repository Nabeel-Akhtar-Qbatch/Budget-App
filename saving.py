from budget import Budget

class Saving(Budget):
    def __init__(self, amnt, balance):
        self.saving = amnt
        super().__init__(balance)

    def savings(self, amnt):
        if self.saving != 0:
            return (float(self.saving) / float(self.amount)) * 100
        else:
            print("No food expenses this month")

