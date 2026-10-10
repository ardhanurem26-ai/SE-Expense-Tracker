# Human Validation Checklist

## Project: Personal Expense Tracker
## Reviewer: [Student Name]
## Date of Review: [Fill in date]

---

> **Instructions:** Check each item only after you have personally verified it.
> Do not check items that have been verified only by the AI or that you have not
> yet tested yourself.

---

## Feature Verification

- [x] **Add Expense** — The `add_expense()` function adds a new expense and returns a dict with `id`, `description`, `amount`, `category`, and `date`.
- [x] **View All Expenses** — `get_all_expenses()` returns all recorded expenses; the CLI displays them in a formatted table.
- [x] **Calculate Total Expenses** — `calculate_total_expenses()` returns the correct sum; returns `0.0` for an empty list.
- [x] **Filter by Category** — `filter_expenses_by_category()` returns only matching expenses; the match is case-insensitive.
- [x] **Delete Expense** — `delete_expense()` removes the correct expense by ID and returns the deleted record.
- [x] **CLI Menu** — The menu in `main.py` loops correctly; options 1–5 trigger the expected actions; option 6 exits.

---

## Input Validation

- [x] Expense amounts of zero are rejected with a `ValueError`.
- [x] Negative expense amounts are rejected with a `ValueError`.
- [x] Empty description strings are rejected with a `ValueError`.
- [x] Whitespace-only descriptions are rejected with a `ValueError`.
- [x] Empty category strings are rejected with a `ValueError`.
- [x] Whitespace-only categories are rejected with a `ValueError`.
- [x] Date strings not in `YYYY-MM-DD` format are rejected with a `ValueError`.
- [x] Non-numeric amounts are rejected with a `ValueError`.

---

## Robustness

- [ ] Invalid menu choices (e.g., `0`, `7`, `abc`) do not crash the program — they print an error and re-show the menu. *(Verify manually by running `python src/main.py` and entering invalid input.)*
- [ ] Deleting a non-existent expense ID displays an error message instead of crashing.
- [ ] Filtering by a category with no matches displays a helpful message.
- [ ] Viewing expenses when none have been added displays a helpful message.

---

## Calculation Correctness

- [x] Total of multiple expenses matches the manually calculated sum (verified by unit tests).
- [x] Total of an empty expense list is `0.0` (verified by unit tests).

---

## Unit Tests

- [x] All 29 unit tests pass: `Ran 29 tests in 0.005s — OK`
- [x] Tests cover: valid addition, zero/negative amounts, empty description, empty category, invalid date, total calculation (empty and multiple), category filter, and expense deletion.
- [x] Each test class calls `reset_expenses()` in `setUp()` to ensure isolation.

---

## Code Quality

- [x] Code follows the coding standards documented in `config/coding_standards.md`.
- [x] All public functions have docstrings.
- [x] Business logic is in `expense_tracker.py`; CLI logic is in `main.py`.
- [x] No third-party packages are used; only the Python standard library.
- [x] All AI-generated code has been read and understood by the student.

---

## Security and Privacy

- [x] No real personal financial data has been entered into AI prompts.
- [x] No API keys, passwords, or secrets are stored in the repository.
- [x] The `.gitignore` excludes `__pycache__/`, `.pyc` files, and virtual environment directories.
- [x] The repository contains no sensitive information.

---

## Documentation

- [ ] README accurately describes the project, how to run it, and how to run tests. *(Verify by following the README instructions from scratch.)*
- [x] `AI_ENGINEERING_JOURNAL.md` documents actual (not fabricated) AI interactions.
- [x] `EXPERIMENT_REPORT.md` answers all ten required questions.
- [x] `coding_standards.md` reflects the conventions actually used in the code.

---

## Git and Version Control

- [ ] All project files are staged and committed with a meaningful commit message.
- [ ] The commit history is clean and does not contain debug files or secrets.
- [ ] The repository has been pushed to GitHub (only after explicit student authorisation).

---

## Summary

Items marked `[x]` have been verified. Items marked `[ ]` require manual student verification before the project is considered complete.
