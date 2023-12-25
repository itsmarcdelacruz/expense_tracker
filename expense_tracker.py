from expense import Expense
import csv

def main():
    print(f"Running Expense Tracking!")
    
    # Get user to input expenses
    expense = get_expense()
    print(expense)
    # Write expense into file
    save_expense_to_file(expense)
    # Read file and display and summarize expenses
    summarize_expense()

def get_expense():
    print(f"Getting Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: ") )
    print(f"You've entered {expense_name} for {expense_amount}")
    selected_category = get_category()
    
    print(f"You selected: {selected_category}")
    
    return Expense(expense_name, selected_category, expense_amount)
    
def get_category():
    categories = ['🍔 Food', '🚗 Transport', '💼 Work', '🏠 Rent/Utilities', '🎥 Entertainment', '⭐ Misc',]
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Select a category (1-6): "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return categories[choice - 1]

def save_expense_to_file(expense: Expense):
    print(f"Save Expense")
    filename = "expenses.csv"
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Check if the file is empty to write headers
        if file.tell() == 0:
            writer.writerow(["Name", "Category", "Amount"])
        
        writer.writerow([expense.name, expense.category, expense.amount])
        print(f"Expense saved to {filename}")

def summarize_expense():
    print(f"Print Expense")
    pass
    


if __name__ == "__main__":
    main()