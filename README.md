# Expense Tracker (Python)

A simple menu-driven console program to record daily expenses and see where your money goes. Expenses are saved in a JSON file, so they are still there the next time you run it.

## Features
- Add an expense (category, description, amount); today's date is added automatically
- View all expenses in a table
- Summary: total per category, grand total and the highest-spending category
- Monthly total (for example `2026-11`)
- Delete an expense
- Input validation for amounts and menu choices

## Concepts used
Functions, lists, dictionaries, loops, file handling (`json`), exception handling (`try/except`), f-string formatting, `datetime`

## How to run
Needs only Python 3 (no extra libraries).
```bash
python expense_tracker.py
```

## Sample output
```
--- Expense Tracker ---
Choice: 1
Category (food, travel, books, ...): food
Description: Lunch
Amount (Rs.): 120
Expense added.

--- Summary ---
food       Rs.   120.00
travel     Rs.    60.00
TOTAL      Rs.   180.00
Highest spending: food (Rs. 120.00)
```

## Future improvements
- Set a monthly budget and warn when it is crossed
- Export expenses to a CSV file
- Draw a bar chart of spending by category using matplotlib
