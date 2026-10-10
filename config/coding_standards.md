# Coding Standards

## Project: Personal Expense Tracker

These standards are based on PEP 8 and apply to all Python files in this project.

---

## 1. Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Functions | `snake_case` | `add_expense()` |
| Variables | `snake_case` | `expense_id` |
| Constants | `UPPER_SNAKE_CASE` | `DATE_FORMAT` |
| Modules | `snake_case` | `expense_tracker.py` |
| Classes | `PascalCase` (if used) | `ExpenseTracker` |

---

## 2. Function Design

- Each function must have **one clear responsibility**.
- Keep functions short — typically under 20 lines of executable code.
- Business logic must **not** mix with command-line input/output.
- All public functions must have a **docstring** explaining what they do, their parameters, return values, and any exceptions they raise.

```python
# Good
def calculate_total_expenses() -> float:
    """Calculate and return the total of all recorded expenses."""
    return round(sum(e["amount"] for e in _expenses), 2)

# Bad
def do_stuff():
    amount_str = input("Amount: ")
    total = sum(...)
    print(total)
```

---

## 3. Input Validation

- Validate all inputs at the boundary of public functions.
- Raise `ValueError` with a clear, human-readable message for invalid input.
- Never assume user input is well-formed.

```python
if not description.strip():
    raise ValueError("Description must be a non-empty string.")
```

---

## 4. Error Handling

- Use specific exceptions (`ValueError`, `TypeError`) rather than bare `except`.
- Catch exceptions at the CLI layer; let the backend raise them cleanly.
- Never silently swallow exceptions.

```python
# Good
try:
    expense = add_expense(description, amount, category, date)
except ValueError as err:
    print(f"Error: {err}")
```

---

## 5. Constants

- Define magic strings and format strings as module-level constants.
- Do not repeat literal strings across the codebase.

```python
DATE_FORMAT = "%Y-%m-%d"  # defined once, reused everywhere
```

---

## 6. Code Duplication

- Extract repeated logic into a helper function.
- Do not copy-paste validation blocks; share a validation utility.

---

## 7. Whitespace and Formatting

- Use **4 spaces** per indentation level (no tabs).
- Limit lines to **79 characters** where practical.
- Two blank lines between top-level function definitions.
- One blank line between logically distinct blocks inside a function.

---

## 8. Imports

- Standard library imports only (no third-party packages required).
- Group imports: standard library first, then local modules.
- One import per line.

---

## 9. Comments

- Write comments to explain *why*, not *what*.
- Keep comments up to date when code changes.
- Use section dividers (`# ---`) sparingly to group related functions.

---

## 10. Unit Tests

- Every public function must have at least one unit test.
- Tests must be isolated: call `reset_expenses()` in `setUp()`.
- Test names must describe the expected behaviour: `test_add_expense_rejects_negative_amount`.
- Run the full suite before committing:
  ```
  python -m unittest discover -s tests -v
  ```

---

## 11. Separation of Concerns

| Layer | Responsibility |
|---|---|
| `src/expense_tracker.py` | Business logic, validation, data storage |
| `src/main.py` | User input, output formatting, menu loop |
| `tests/` | Automated verification of backend logic |

The CLI layer (`main.py`) must **never** perform validation or data mutation directly; it delegates entirely to `expense_tracker.py`.
