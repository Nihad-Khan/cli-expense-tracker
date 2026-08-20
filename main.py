import sys
import csv
import re

SEPARATOR = "-" * 40

def main():
    print(f"{SEPARATOR}  Expense Trackor  {SEPARATOR}")
    Expenses = load_csv()
    show_menu(Expenses)


def show_menu(expenses):
    options = ["Add Expense","Show Expenses","Total Expenses","Delete Expense","Exit"]
    print(SEPARATOR)

    while True:
        print(f"\n{SEPARATOR}")
        for i,option in enumerate(options,1):
            print(f"{i}. {option}")

        try:
            user = int(input("\nOption :  "))
        except ValueError:
            print("Plz Enter option number only! ")
            continue

        if user == 1:
            add_expense(expenses)
        elif user == 2:
            show_expenses(expenses)
        elif user == 3:
            total_expenses(expenses)
        elif user == 4:
            delete_expense(expenses)
        elif user == 5:
            sys.exit("Good Bye !")
        else:
            print("Plz enter option from (1-5)")



def add_expense(expenses):
    title = input("Enter expense Title :  ").strip().title()
    category = input("Enter expense Catogary : ").strip().title()
    while True:
        try : 
            cost = float(input("Enter Expense Cost : "))
            break

        except ValueError:
            print("Plz Enter Expense cost in numbers ! ")
            continue



    while True:
        date = input("Enter expense Date i.e : (2026-08-20) : ").strip()
        date_pattern =  r"^(19\d{2}|20[0-2][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
        if not re.match(date_pattern,date):
            print("Put date like this i.e : (2026-08-20)")
            continue
        break
    expense = {"Title" : title,"Category" : category,"Cost" : cost,"Date" : date}
    expenses.append(expense)
    print("Expense Added Successfully !")
    save_to_csv(expenses)


def show_expenses(expenses):
    if not expenses:
        print("No expenses here !")
        return False
    
    for i,expense in enumerate(expenses,1):
        print(f"\nExpense No : {i}")
        for key,value in expense.items():
            if key == "Cost":
                print(f"{key} : Rs.{value}")
            else:
                print(f"{key} : {value}")
    
    return True

def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["Cost"]
    print(f"Total Expenses =Rs. {total}")

        
def delete_expense(expenses):
    if show_expenses(expenses):
        try :
            user = int(input('\nEnter expense Number You want to delete or 0 to back : '))
            if user == 0:
                return
            elif user < 1 :
                raise IndexError
            del expenses[user-1]

            print("Expense deleted !")
            save_to_csv(expenses)


        except ValueError:
            print("Plz only put Numbers : ")
        except IndexError :
            print("Expense number not in range ")
   

def save_to_csv(expenses):
    headers= ["Title","Category","Cost","Date"]
    with open("expenses.csv","w",newline="") as file:
        writer = csv.DictWriter(file,fieldnames=headers)

        writer.writeheader()
        writer.writerows(expenses)


def load_csv():
    expenses = []

    try:
        with open("expenses.csv","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["Cost"] = float(row['Cost'])
                expenses.append(row)
    except FileNotFoundError:
        return []
    return expenses

            


if __name__ == "__main__":
    main()