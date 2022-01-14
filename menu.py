#Implementing Decorators to print Tic Tac Toe Game Headline/Title
def star (func):    
    def inner():
        print("*" * 35)
        func()
        print("*" * 35)
    return inner

def percent (func):
    def inner():
        print("%" * 35)
        func()
        print("%" * 35)
    return inner

@star
@percent
def splash_printer():
    print ("\tBudget Manager")

#Main Menu
def main_menu(func):
    def inner():
        print("\nSelect\n1. Manage Expenses\n2. Calculate Taxes")
        return func()
    return inner

@main_menu
def menu_selection():
    selected = input("\nPlease Enter:")
    return int(selected)

