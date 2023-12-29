from expense import Expense
import csv
from datetime import datetime

def main():
    print(f"Running Expense Tracking!")
    
    # Get user to input expenses
    expense = get_expense()
    print(expense)
    
    # Write expense into file
    save_expense_to_file(expense)
    
    # Read file and display and summarize expenses
    summarize_expense()

    #Summarize specfic category expenses

    #Add dates to expenses

def get_expense():
    print(f"Getting Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: ") )
    print(f"You've entered {expense_name} for {expense_amount}")
    selected_category = get_category()
    
    print(f"You selected: {selected_category}")
    
    expense_date = input("Enter date of expense (YYYY-MM-DD): ")
    
        # Validate and format the date
    try:
        expense_date = datetime.strptime(expense_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Using today's date.")
        expense_date = datetime.today().date()
    
    return Expense(expense_date, expense_name, selected_category, expense_amount,)
    
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
            writer.writerow(["Date", "Name", "Category", "Amount"])
        
        writer.writerow([expense.date, expense.name, expense.category, expense.amount])
        print(f"Expense saved to {filename}")

def summarize_expense():
    print(f"Print Expense")
    filename = "expenses.csv"
    total_amount = 0.0
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            print("Expenses Summary:")
            print(f"{'Date':10} {'Name':20} {'Category':20} {'Amount':>10}")
            for row in reader:
                date, name, category, amount = row
                print(f"{date:10} {name:20} {category:20} {amount:>10}")
                total_amount += float(amount)
        print(f"\nTotal Amount Spent: ${total_amount:.2f}")
    except FileNotFoundError:
        print(f"No records found. '{filename}' does not exist.")
    


if __name__ == "__main__":
    main()