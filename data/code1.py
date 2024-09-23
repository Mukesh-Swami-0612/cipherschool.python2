# Personal Expense Tracker

# Dictionary to store expenses
expenses = []

# Function to add expense
def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category (e.g., Food, Transport, etc.): ")
    description = input("Enter a description for the expense: ")
    
    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses to show.")
        return
    
    total = 0
    print("\nAll Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['category']} - ${expense['amount']}: {expense['description']}")
        total += expense['amount']
    
    print(f"\nTotal spending: ${total}\n")

# Function to save expenses to a file
def save_expenses():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']} - ${expense['amount']}: {expense['description']}\n")
    
    print("Expenses saved to file successfully!\n")

# Main menu
def menu():
    while True:
        print("Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Save Expenses to File")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            save_expenses()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the app
menu()
