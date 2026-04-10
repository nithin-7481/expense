import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# Load expenses
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save expenses
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    date = datetime.now().strftime("%Y-%m-%d")

    expenses.append({
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    })

    save_expenses(expenses)
    print("Expense added!\n")

# View expenses
def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found!\n")
        return

    print("\nYour Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} | ₹{exp['amount']} | {exp['category']} | {exp['date']}")
    print()

# Total spending
def total_expenses(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spending: ₹{total}\n")

# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)
    try:
        index = int(input("Enter number to delete: ")) - 1
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted: {removed['name']}\n")
    except (ValueError, IndexError):
        print("Invalid choice!\n")

# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid option!\n")

if __name__ == "__main__":
    main()