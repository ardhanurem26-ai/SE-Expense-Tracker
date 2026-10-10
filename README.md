# Personal Expense Tracker

A simple, beginner-friendly command-line expense tracking application built in
Python as part of a Software Engineering practical experiment on AI-augmented
development.

---

## Project Description

The Personal Expense Tracker allows you to record, view, and manage personal
expenses during a single session. All data is stored in memory and is cleared
when the program exits. No database, file, or internet connection is required.

---

## Aim and Objectives

**Aim:** Demonstrate how an AI coding assistant supports the software development
lifecycle while the human developer validates and owns the final code.

**Objectives:**
- Implement core expense management features using Python standard-library only.
- Apply PEP 8 coding standards.
- Generate and pass a unit test suite.
- Document the AI-assisted workflow.

---

## Features

| Feature | Description |
|---|---|
| Add Expense | Record a description, amount, category, and date |
| View All Expenses | Display all expenses in a formatted table |
| Calculate Total | Sum all recorded expense amounts |
| Filter by Category | Show only expenses in a specified category |
| Delete Expense | Remove an expense by its ID |
| Input Validation | Reject empty text, non-positive amounts, and invalid dates |

---

## Technologies Used

- **Python 3** — core language
- **`unittest`** — standard library test framework
- **Git + GitHub** — version control
- **Antigravity AI** — AI coding assistant
- **VS Code** — editor

No third-party packages are required.

---

## Repository Structure

```
expense_tracker/
├── src/
│   ├── __init__.py
│   ├── expense_tracker.py   # Business logic
│   └── main.py              # Command-line interface
├── tests/
│   ├── __init__.py
│   └── test_expense_tracker.py
├── docs/
│   ├── AI_ENGINEERING_JOURNAL.md
│   ├── HUMAN_VALIDATION.md
│   └── EXPERIMENT_REPORT.md
├── config/
│   └── coding_standards.md
├── .github/
│   └── copilot-instructions.md
├── .gitignore
└── README.md
```

---

## Requirements

- Python 3.8 or later
- No additional packages to install

Verify your Python version:

```bash
python --version
```

---

## Running the Application

From the project root directory:

```bash
python src/main.py
```

---

## Running the Tests

```bash
python -m unittest discover -s tests -v
```

Expected output:

```
Ran 29 tests in 0.005s

OK
```

---

## Example Menu Interaction

```
Welcome to the Personal Expense Tracker!

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

  Enter your choice (1-6): 1

-------------------------------------------------------
  Add New Expense
-------------------------------------------------------
  Description : Lunch at canteen
  Category    : Food
  Date (YYYY-MM-DD) : 2024-10-10
  Amount      : 120

  Expense added successfully with ID 1.

  Enter your choice (1-6): 3

-------------------------------------------------------
  Total Expenses
-------------------------------------------------------
  Total: Rs 120.00

  Enter your choice (1-6): 6

  Goodbye! All expense data has been cleared.
```

---

## Limitations

- **In-memory storage only:** All expense data is lost when the program exits.
  There is no file or database persistence.
- **Single session:** The application does not retain data between runs.
- **No multi-user support:** Only one user can use the tracker at a time.
- **No currency conversion:** Amounts are treated as plain numbers.
- **No export:** There is no way to save expenses to a file.

---

## AI Assistance and Validation

This project was built with the assistance of the **Antigravity AI** coding
assistant. The AI helped with:

- Generating the initial Python implementation
- Writing unit tests
- Explaining Python floating-point rounding behaviour
- Creating documentation

**Every piece of AI-generated code was reviewed, run, and validated by the
student developer.** One AI-generated test assertion was incorrect (due to
Python's banker's rounding) and was corrected after running the test suite.
The AI engineering journal (`docs/AI_ENGINEERING_JOURNAL.md`) documents each
interaction accurately.

---

## License

This project is submitted for academic purposes as part of a Software Engineering
practical at VJTI. No commercial use intended.
