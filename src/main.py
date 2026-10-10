"""
main.py
-------
Command-line interface for the Personal Expense Tracker.
Presents a text menu and delegates all business logic to expense_tracker.py.
"""

import sys
import os

# Allow running from project root: python src/main.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src import expense_tracker as et  # noqa: E402

# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

SEPARATOR = "-" * 55


def print_header(title: str) -> None:
    """Print a simple section header."""
    print(f"\n{SEPARATOR}")
    print(f"  {title}")
    print(SEPARATOR)


def print_expense_row(expense: dict) -> None:
    """Print a single expense in a formatted row."""
    print(
        f"  ID: {expense['id']:>3}  |  "
        f"{expense['date']}  |  "
        f"Rs {expense['amount']:>10.2f}  |  "
        f"{expense['category']:<15}  |  "
        f"{expense['description']}"
    )


# ---------------------------------------------------------------------------
# Menu actions
# ---------------------------------------------------------------------------

def action_add_expense() -> None:
    """Prompt the user for expense details and add the expense."""
    print_header("Add New Expense")
    description = input("  Description : ").strip()
    category = input("  Category    : ").strip()
    date_str = input("  Date (YYYY-MM-DD) : ").strip()
    amount_str = input("  Amount      : ").strip()

    try:
        amount = float(amount_str)
        expense = et.add_expense(description, amount, category, date_str)
        print(f"\n  Expense added successfully with ID {expense['id']}.")
    except ValueError as err:
        print(f"\n  Error: {err}")


def action_view_expenses() -> None:
    """Display all recorded expenses."""
    print_header("All Expenses")
    expenses = et.get_all_expenses()
    if not expenses:
        print("  No expenses recorded yet.")
        return
    print(
        f"  {'ID':>3}  |  {'Date':<10}  |  {'Amount':>12}  |  "
        f"{'Category':<15}  |  Description"
    )
    print("  " + "-" * 75)
    for expense in expenses:
        print_expense_row(expense)


def action_total_expenses() -> None:
    """Display the total of all recorded expenses."""
    print_header("Total Expenses")
    total = et.calculate_total_expenses()
    print(f"  Total: Rs {total:.2f}")


def action_filter_by_category() -> None:
    """Filter and display expenses by category."""
    print_header("Filter by Category")
    category = input("  Enter category to filter: ").strip()
    try:
        results = et.filter_expenses_by_category(category)
    except ValueError as err:
        print(f"\n  Error: {err}")
        return

    if not results:
        print(f"  No expenses found in category '{category}'.")
        return
    print(f"\n  Expenses in category '{category}':")
    for expense in results:
        print_expense_row(expense)


def action_delete_expense() -> None:
    """Delete an expense by its ID."""
    print_header("Delete Expense")
    id_str = input("  Enter Expense ID to delete: ").strip()
    try:
        expense_id = int(id_str)
        deleted = et.delete_expense(expense_id)
        print(f"\n  Deleted expense: [{deleted['id']}] {deleted['description']}")
    except ValueError as err:
        print(f"\n  Error: {err}")


# ---------------------------------------------------------------------------
# Main menu loop
# ---------------------------------------------------------------------------

MENU = """
+------------------------------------------+
|       Personal Expense Tracker           |
+------------------------------------------+
|  1. Add Expense                          |
|  2. View All Expenses                    |
|  3. Calculate Total Expenses             |
|  4. Filter Expenses by Category          |
|  5. Delete Expense                       |
|  6. Exit                                 |
+------------------------------------------+
"""


def main() -> None:
    """Entry point: display menu and handle user choices in a loop."""
    print("\nWelcome to the Personal Expense Tracker!")

    actions = {
        "1": action_add_expense,
        "2": action_view_expenses,
        "3": action_total_expenses,
        "4": action_filter_by_category,
        "5": action_delete_expense,
    }

    while True:
        print(MENU)
        choice = input("  Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\n  Goodbye! All expense data has been cleared.\n")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("\n  Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
