#Dictionary for tax slab (Pakistan Tax 2020-2021)
tax_slab = {'slab1' : '600000', 'slab2' : '1200000', 'slab3' : '1800000', 
            'slab4' : '2500000', 'slab5' : '3500000', 'slab6' : '5000000', 
            'slab7' : '8000000', 'slab8' : '12000000', 'slab9' : '30000000', 
            'slab10' : '50000000', 'slab11' : '75000000'}
anm_amnt = 0

#Formula for calulating Tax
def tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt):
    tax_on = anm_amnt - tax_slab_amnt
    tax_amnt = (tax_on * tax_rate) + add_amnt
    return tax_amnt

#Decorator to Pre check the Applicable percentage of Tax on Annual Incone
def taxable_check(func):
    def inner(amnt):
        anm_amnt = amnt * 12
        print("\n****** Tax Calculation ******\nMonthly Income: ",amnt)
        print("\nCalculating Total Tax, As per Federal Budget 2019-2020 presented by Government of Pakistan\n")
        if anm_amnt < int(tax_slab['slab1']):                                           #Slab 1
            tax_rate = 0
            add_amnt = 0
            tax_slab_amnt =int(tax_slab['slab1'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            if tax_amnt == 0: print("\nIncome is not Taxable\n")
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab1']) and anm_amnt < int(tax_slab['slab2']):   #Slab 2
            tax_rate = 0.05
            add_amnt = 0
            tax_slab_amnt =int(tax_slab['slab1'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab2']) and anm_amnt < int(tax_slab['slab3']):   #Slab 3
            tax_rate = 0.1
            add_amnt = 30000
            tax_slab_amnt =int(tax_slab['slab2'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab3']) and anm_amnt < int(tax_slab['slab4']):   #Slab 4
            tax_rate = 0.15
            add_amnt = 90000
            tax_slab_amnt =int(tax_slab['slab3'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab4']) and anm_amnt < int(tax_slab['slab5']):   #Slab 5
            tax_rate = 0.175
            add_amnt = 195000
            tax_slab_amnt =int(tax_slab['slab4'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab5']) and anm_amnt < int(tax_slab['slab6']):   #Slab 6
            tax_rate = 0.2
            add_amnt = 370000
            tax_slab_amnt =int(tax_slab['slab5'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab6']) and anm_amnt < int(tax_slab['slab7']):   #Slab 7
            tax_rate = 0.225
            add_amnt = 670000
            tax_slab_amnt =int(tax_slab['slab6'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab7']) and anm_amnt < int(tax_slab['slab8']):   #Slab 8
            tax_rate = 0.25
            add_amnt = 1345000
            tax_slab_amnt =int(tax_slab['slab7'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab8']) and anm_amnt < int(tax_slab['slab9']):   #Slab 9
            tax_rate = 0.275
            add_amnt = 2345000
            tax_slab_amnt =int(tax_slab['slab8'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab9']) and anm_amnt < int(tax_slab['slab10']):  #Slab 10
            tax_rate = 0.3
            add_amnt = 7295000
            tax_slab_amnt =int(tax_slab['slab9'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab10']) and anm_amnt < int(tax_slab['slab11']): #Slab 11
            tax_rate = 0.325
            add_amnt = 13295000
            tax_slab_amnt =int(tax_slab['slab10'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
        elif anm_amnt > int(tax_slab['slab11']):                                    #Slab 12
            tax_rate = 0.35
            add_amnt = 21420000
            tax_slab_amnt =int(tax_slab['slab11'])
            tax_amnt = tax_formula(anm_amnt, tax_slab_amnt, tax_rate, add_amnt)
            return func(tax_amnt)
    return inner

@taxable_check
def tax(amnt):
    tax_amnt_final = f"**** Total Tax ****\nYearly Tax: {amnt}\nMonthly Tax: {amnt/12}\n"
    print(tax_amnt_final)
    return amnt
