from distutils.command.build_scripts import build_scripts
from budget import Budget
from food import Food
from home import Home
from menu import menu_selection, splash_printer
from saving import Saving
from tax_calculator import tax
from print_percentage import printProgressBar
from travel import Travel

def main():
    splash_printer()
    sel = menu_selection()
    if sel == 1:
        income = int(input("Enter your Monthly income: "))
        if income <= 0:
            print("Not Valid Amount to enter")
            main()
        else:
            foodexp = int(input("Enter Food Expense: "))
            food = Food(foodexp, income)
            homeexp = int(input("Enter Home Expense: "))
            home = Home(homeexp, income)
            travexp = int(input("Enter Travel Expenses: "))
            travel = Travel(travexp, income)

            pertravel = float(travel.travel_budget(income))
            perhome = float(home.home_budget(income))
            perfood = float(food.food_budget(income))
            saved = float((foodexp + homeexp + travexp) - income)
            if saved < 0: saved = saved * -1
            save = Saving(saved, income)
            persave = int(save.savings(income))
            print("\nPercentages of Different expenses from total income\n")
            printProgressBar(perfood, "Food Expenses", foodexp)
            printProgressBar(perhome, "Home Expenses", homeexp)
            printProgressBar(pertravel, "Travel Expenses", travexp)
            printProgressBar(persave, "Saved Amount", saved)
            
    if sel == 2:
        income = int(input("Enter your monthly salary: "))
        tax_amnt = tax(income)
        more_sel = input("\n**Show more detail**\nEnter (y/n) ")
        if more_sel == 'y' or more_sel == 'Y':
            tax_amnt_final = f"\n**** Tax Detail ****\nMonthly Salary: {income}\nMonthly Tax: {tax_amnt / 12}\nMonthly Salary After tax: {income - (tax_amnt / 12)}\nYearly Salary: {income * 12}\nYearly Tax: {tax_amnt}\nYearly Salary after tax: {(income * 12) - tax_amnt}" 
            print(tax_amnt_final)
        elif more_sel == 'n' or more_sel == 'N':
            main()

if __name__ == "__main__":
    main()
