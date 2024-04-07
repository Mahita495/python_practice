import sys
def info():
    print("Kindly choose an option from below")
    print("1. Add an expense")
    print("2. Remove an expense")
    print("3. Display list of all expenses")
    
category={}

def add_expense(exp):
    for i in range(exp):
        print("Enter the category")
        cat=input()
        print("Enter the amount")
        amt=int(input())
        category[cat]=amt

    print("All expenses added")

def rem_expense(rem_exp):

    if len(category)==0:
        print("No category to remove")
    else:
        for i in range(rem_exp):
            print("Enter the category for expense to be removed")
            rem_cat=input()
            print("Enter amount")
            rem_amt=int(input())
            if rem_cat in category and category[rem_cat]==rem_amt:
                del category[rem_cat]
                print("Expense removed")
            else:
                print("Please enter correct category")
    
    for key,val in category.items():
        print(f"{key}:{val}")

def show_exp():
    if len(category)==0:
        print("No expenses to show")
    else:
        print("Here are the list of expenses:")
        print("------------------------------------")
        c=1
        for key,val in category.items():
            print(f"{c}. {key} : {val}")
            c+=1

def expense_tracker():
    n=int(input())
    if n==1:
        print("No of expenses you want to add")
        exp=int(input())
        add_expense(exp)
        info()
    elif n==2:
        print("Enter no of expenses to be removed")
        rem_exp=int(input())
        rem_expense(rem_exp)
        info()
    elif n==3:
        show_exp()
        info()
    elif n==0:
        sys.exit()
    else:
        info()
    expense_tracker()


        
info()
expense_tracker()

    

    
    





