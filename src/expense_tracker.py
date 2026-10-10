"""
expense_tracker.py
------------------
Core backend logic for the Personal Expense Tracker.
Stores expenses in an in-memory list of dictionaries.
No database or file persistence is used.

Each expense dictionary contains:
    id          (int)  : auto-incremented unique identifier
    description (str)  : brief label for the expense
    amount      (float): positive monetary value
    category    (str)  : grouping label (e.g. "Food", "Transport")
    date        (str)  : date in YYYY-MM-DD format
"""

import re
from datetime import datetime

# ---------------------------------------------------------------------------
# In-memory storage
# ---------------------------------------------------------------------------

_expenses: list[dict] = []
_next_id: int = 1

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

DATE_FORMAT = "%Y-%m-%d"


# ---------------------------------------------------------------------------
# Helper / validation utilities
# ---------------------------------------------------------------------------

def _validate_date(date_str: str) -> bool:
    """Return True if date_str matches YYYY-MM-DD format, False otherwise."""
    try:
        datetime.strptime(date_str, DATE_FORMAT)
        return True
    except ValueError:
        return False


def reset_expenses() -> None:
    """
    Clear all stored expenses and reset the ID counter.
    Intended for use in unit tests to ensure test isolation.
    """
    global _expenses, _next_id
    _expenses = []
    _next_id = 1


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def add_expense(description: str, amount: float, category: str, date: str) -> dict:
    """
    Add a new expense to the in-memory store.

    Parameters
    ----------
    description : str
        A non-empty label for the expense (e.g. "Lunch at cafe").
    amount : float
        A positive monetary value (e.g. 250.00).
    category : str
        A non-empty category label (e.g. "Food").
    date : str
        Date in YYYY-MM-DD format (e.g. "2024-10-10").

    Returns
    -------
    dict
        The newly created expense record.

    Raises
    ------
    ValueError
        If any validation check fails.
    """
    global _next_id

    # Validate description
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Description must be a non-empty string.")

    # Validate amount
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        raise ValueError("Amount must be a numeric value.")
    if amount <= 0:
        raise ValueError("Amount must be a positive number greater than zero.")

    # Validate category
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category must be a non-empty string.")

    # Validate date
    if not _validate_date(date):
        raise ValueError(f"Date must be in YYYY-MM-DD format. Got: '{date}'")

    expense = {
        "id": _next_id,
        "description": description.strip(),
        "amount": round(amount, 2),
        "category": category.strip(),
        "date": date,
    }
    _expenses.append(expense)
    _next_id += 1
    return expense


def get_all_expenses() -> list[dict]:
    """
    Return a copy of all recorded expenses.

    Returns
    -------
    list[dict]
        List of expense dictionaries (may be empty).
    """
    return list(_expenses)


def calculate_total_expenses() -> float:
    """
    Calculate the sum of all recorded expense amounts.

    Returns
    -------
    float
        Total amount. Returns 0.0 if there are no expenses.
    """
    return round(sum(e["amount"] for e in _expenses), 2)


def filter_expenses_by_category(category: str) -> list[dict]:
    """
    Return all expenses whose category matches the given string (case-insensitive).

    Parameters
    ----------
    category : str
        The category to filter by.

    Returns
    -------
    list[dict]
        Matching expenses. Empty list if no match is found.

    Raises
    ------
    ValueError
        If category is empty.
    """
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Category filter must be a non-empty string.")

    search = category.strip().lower()
    return [e for e in _expenses if e["category"].lower() == search]


def delete_expense(expense_id: int) -> dict:
    """
    Remove the expense with the given ID from the store.

    Parameters
    ----------
    expense_id : int
        The ID of the expense to delete.

    Returns
    -------
    dict
        The deleted expense record.

    Raises
    ------
    ValueError
        If expense_id is not a positive integer or is not found.
    """
    if not isinstance(expense_id, int) or expense_id <= 0:
        raise ValueError("Expense ID must be a positive integer.")

    for index, expense in enumerate(_expenses):
        if expense["id"] == expense_id:
            return _expenses.pop(index)

    raise ValueError(f"No expense found with ID {expense_id}.")
