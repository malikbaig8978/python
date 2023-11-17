import csv
import os
from datetime import datetime

# Function to add an expense
def add_expense(date, category, amount, description):
    with open('expenses.csv', 'a', newline='') as csvfile:
        fieldnames = ['Date', 'Category', 'Amount', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is empty
        if os.path.getsize('expenses.csv') == 0:
            writer.writeheader()

        # Write the expense data
        writer.writerow({'Date': date, 'Category': category, 'Amount': amount, 'Description': description})
    print("Expense added successfully!")

# Function to generate monthly report
def generate_monthly_report(month, year):
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        total_expense = 0

        # Print the header
        print(f"\nMonthly Report for {month} {year}")
        print("{:<15} {:<15} {:<15} {:<15}".format("Date", "Category", "Amount", "Description"))
        print("-" * 60)

        # Print expenses for the specified month and year
        for row in reader:
            expense_date = datetime.strptime(row['Date'], '%Y-%m-%d')
            if expense_date.month == month and expense_date.year == year:
                total_expense += float(row['Amount'])
                print("{:<15} {:<15} {:<15} {:<15}".format(row['Date'], row['Category'], row['Amount'], row['Description']))

        # Print total expense for the month
        print("\nTotal Expense for the Month: ${:.2f}\n".format(total_expense))

# Main menu
while True:
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. Generate Monthly Report")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        amount = input("Enter the amount: ")
        description = input("Enter a description: ")
        add_expense(date, category, amount, description)
    elif choice == '2':
        month = int(input("Enter the month (1-12): "))
        year = int(input("Enter the year: "))
        generate_monthly_report(month, year)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
