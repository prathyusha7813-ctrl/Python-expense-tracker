"""Expense Tracker
A simple menu-driven program to record expenses, see totals
and find where the most money is going. Data is saved in expenses.json.
"""

import json
import os
from datetime import date

# Save the file next to this script, wherever you run it from
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")


def load_expenses():
    """Read saved expenses from the file. Returns an empty list the first time."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    """Write all expenses to the file."""
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    """Ask the user for details and add one expense."""
    category = input("Category (food, travel, books, ...): ").strip().lower()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount (Rs.): "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if amount <= 0:
        print("Amount must be more than 0.")
        return

    expense = {
        "date": str(date.today()),   # example: 2026-11-16
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added.")


def view_expenses(expenses):
    """Print every expense in a table."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print(f"\n{'No.':<4} {'Date':<12} {'Category':<10} {'Description':<18} {'Amount':>8}")
    for i, e in enumerate(expenses, start=1):
        print(f"{i:<4} {e['date']:<12} {e['category']:<10} {e['description']:<18} {e['amount']:>8.2f}")


def show_summary(expenses):
    """Show the total spent and the total for each category."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    totals = {}   # category -> total amount
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    grand_total = sum(totals.values())
    print("\n--- Summary ---")
    for category, amount in totals.items():
        print(f"{category:<10} Rs. {amount:>8.2f}")
    print(f"{'TOTAL':<10} Rs. {grand_total:>8.2f}")

    top = max(totals, key=totals.get)   # category with the biggest total
    print(f"Highest spending: {top} (Rs. {totals[top]:.2f})")


def monthly_total(expenses):
    """Total spent in a month. Month format: 2026-11"""
    month = input("Enter month (YYYY-MM): ").strip()
    total = 0
    for e in expenses:
        if e["date"].startswith(month):
            total += e["amount"]
    print(f"Total spent in {month}: Rs. {total:.2f}")


def delete_expense(expenses):
    """Delete one expense by its number in the table."""
    view_expenses(expenses)
    if len(expenses) == 0:
        return
    try:
        number = int(input("Enter number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if 1 <= number <= len(expenses):
        removed = expenses.pop(number - 1)
        save_expenses(expenses)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid number.")


def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Summary by category")
        print("4. Monthly total")
        print("5. Delete expense")
        print("6. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            monthly_total(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
