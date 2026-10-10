"""
test_expense_tracker.py
-----------------------
Unit tests for src/expense_tracker.py using Python's built-in unittest framework.

Each test method calls reset_expenses() in setUp() to ensure full test isolation.
"""

import sys
import os
import unittest

# Allow test discovery from the project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.expense_tracker import (
    add_expense,
    get_all_expenses,
    calculate_total_expenses,
    filter_expenses_by_category,
    delete_expense,
    reset_expenses,
)


class TestAddExpense(unittest.TestCase):
    """Tests for add_expense()."""

    def setUp(self):
        """Reset state before every test."""
        reset_expenses()

    # ------------------------------------------------------------------
    # Happy-path tests
    # ------------------------------------------------------------------

    def test_add_valid_expense_returns_dict(self):
        """Adding a valid expense should return a dict with correct fields."""
        expense = add_expense("Bus ticket", 50.0, "Transport", "2024-10-01")
        self.assertIsInstance(expense, dict)
        self.assertEqual(expense["description"], "Bus ticket")
        self.assertEqual(expense["amount"], 50.0)
        self.assertEqual(expense["category"], "Transport")
        self.assertEqual(expense["date"], "2024-10-01")
        self.assertEqual(expense["id"], 1)

    def test_add_expense_increments_id(self):
        """Each successive expense should receive an incremented ID."""
        e1 = add_expense("Lunch", 150.0, "Food", "2024-10-01")
        e2 = add_expense("Dinner", 200.0, "Food", "2024-10-01")
        self.assertEqual(e1["id"], 1)
        self.assertEqual(e2["id"], 2)

    def test_add_expense_strips_whitespace(self):
        """Leading/trailing whitespace in description and category should be stripped."""
        expense = add_expense("  Coffee  ", 30.0, "  Food  ", "2024-10-01")
        self.assertEqual(expense["description"], "Coffee")
        self.assertEqual(expense["category"], "Food")

    def test_add_expense_rounds_amount(self):
        """Amount should be rounded to two decimal places."""
        # Use 10.556 to avoid Python's banker's rounding on the 0.005 boundary.
        expense = add_expense("Snack", 10.556, "Food", "2024-10-01")
        self.assertEqual(expense["amount"], 10.56)

    # ------------------------------------------------------------------
    # Validation failure tests
    # ------------------------------------------------------------------

    def test_add_expense_rejects_zero_amount(self):
        """An amount of zero should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Test", 0, "Misc", "2024-10-01")

    def test_add_expense_rejects_negative_amount(self):
        """A negative amount should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Test", -10.0, "Misc", "2024-10-01")

    def test_add_expense_rejects_empty_description(self):
        """An empty description should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("", 100.0, "Food", "2024-10-01")

    def test_add_expense_rejects_whitespace_description(self):
        """A whitespace-only description should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("   ", 100.0, "Food", "2024-10-01")

    def test_add_expense_rejects_empty_category(self):
        """An empty category should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", 100.0, "", "2024-10-01")

    def test_add_expense_rejects_whitespace_category(self):
        """A whitespace-only category should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", 100.0, "   ", "2024-10-01")

    def test_add_expense_rejects_invalid_date_format(self):
        """A date string not in YYYY-MM-DD format should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", 100.0, "Food", "10-10-2024")

    def test_add_expense_rejects_non_numeric_amount(self):
        """A non-numeric amount should raise ValueError."""
        with self.assertRaises(ValueError):
            add_expense("Lunch", "abc", "Food", "2024-10-01")


class TestGetAllExpenses(unittest.TestCase):
    """Tests for get_all_expenses()."""

    def setUp(self):
        reset_expenses()

    def test_get_all_expenses_empty(self):
        """Should return an empty list when no expenses have been added."""
        self.assertEqual(get_all_expenses(), [])

    def test_get_all_expenses_returns_all(self):
        """Should return all added expenses."""
        add_expense("Lunch", 120.0, "Food", "2024-10-01")
        add_expense("Bus", 30.0, "Transport", "2024-10-02")
        expenses = get_all_expenses()
        self.assertEqual(len(expenses), 2)

    def test_get_all_expenses_returns_copy(self):
        """Modifying the returned list should not affect the internal store."""
        add_expense("Lunch", 120.0, "Food", "2024-10-01")
        expenses = get_all_expenses()
        expenses.clear()
        self.assertEqual(len(get_all_expenses()), 1)


class TestCalculateTotalExpenses(unittest.TestCase):
    """Tests for calculate_total_expenses()."""

    def setUp(self):
        reset_expenses()

    def test_total_empty_list(self):
        """Total should be 0.0 when there are no expenses."""
        self.assertEqual(calculate_total_expenses(), 0.0)

    def test_total_single_expense(self):
        """Total should equal the amount of a single expense."""
        add_expense("Lunch", 150.0, "Food", "2024-10-01")
        self.assertEqual(calculate_total_expenses(), 150.0)

    def test_total_multiple_expenses(self):
        """Total should be the sum of all expense amounts."""
        add_expense("Lunch", 150.0, "Food", "2024-10-01")
        add_expense("Bus", 30.0, "Transport", "2024-10-01")
        add_expense("Coffee", 20.0, "Food", "2024-10-01")
        self.assertEqual(calculate_total_expenses(), 200.0)


class TestFilterExpensesByCategory(unittest.TestCase):
    """Tests for filter_expenses_by_category()."""

    def setUp(self):
        reset_expenses()
        add_expense("Lunch", 150.0, "Food", "2024-10-01")
        add_expense("Dinner", 200.0, "Food", "2024-10-02")
        add_expense("Bus ticket", 30.0, "Transport", "2024-10-01")

    def test_filter_returns_matching_expenses(self):
        """Should return only expenses that match the given category."""
        results = filter_expenses_by_category("Food")
        self.assertEqual(len(results), 2)
        for expense in results:
            self.assertEqual(expense["category"], "Food")

    def test_filter_is_case_insensitive(self):
        """Filtering should work regardless of the case of the category string."""
        results = filter_expenses_by_category("food")
        self.assertEqual(len(results), 2)

    def test_filter_nonexistent_category_returns_empty(self):
        """A category with no matching expenses should return an empty list."""
        results = filter_expenses_by_category("Entertainment")
        self.assertEqual(results, [])

    def test_filter_rejects_empty_category(self):
        """An empty category string should raise ValueError."""
        with self.assertRaises(ValueError):
            filter_expenses_by_category("")


class TestDeleteExpense(unittest.TestCase):
    """Tests for delete_expense()."""

    def setUp(self):
        reset_expenses()
        self.expense = add_expense("Lunch", 150.0, "Food", "2024-10-01")

    def test_delete_existing_expense(self):
        """Deleting a valid ID should remove it from the store."""
        deleted = delete_expense(self.expense["id"])
        self.assertEqual(deleted["id"], self.expense["id"])
        self.assertEqual(get_all_expenses(), [])

    def test_delete_returns_correct_expense(self):
        """The returned dict should match the deleted expense."""
        deleted = delete_expense(self.expense["id"])
        self.assertEqual(deleted["description"], "Lunch")
        self.assertEqual(deleted["amount"], 150.0)

    def test_delete_nonexistent_id_raises_error(self):
        """Deleting a non-existent ID should raise ValueError."""
        with self.assertRaises(ValueError):
            delete_expense(999)

    def test_delete_invalid_id_type_raises_error(self):
        """Passing a non-integer ID should raise ValueError."""
        with self.assertRaises(ValueError):
            delete_expense("abc")

    def test_delete_zero_id_raises_error(self):
        """An ID of zero should raise ValueError."""
        with self.assertRaises(ValueError):
            delete_expense(0)

    def test_delete_negative_id_raises_error(self):
        """A negative ID should raise ValueError."""
        with self.assertRaises(ValueError):
            delete_expense(-1)

    def test_delete_reduces_expense_count(self):
        """After deletion the expense list should be shorter by one."""
        add_expense("Bus", 30.0, "Transport", "2024-10-01")
        self.assertEqual(len(get_all_expenses()), 2)
        delete_expense(self.expense["id"])
        self.assertEqual(len(get_all_expenses()), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
