# Copilot / AI Assistant Instructions

## Project: Personal Expense Tracker

This file gives AI coding assistants the context they need to generate useful,
project-consistent code suggestions.

---

## Overview

This is a **beginner-level Python backend project** built as a Software
Engineering practical exercise. It demonstrates an AI-augmented development
workflow.

**There is no frontend, GUI, database, API, or web server.** Keep all
suggestions simple and limited to Python standard-library only.

---

## Repository Structure

```
expense_tracker/
├── src/
│   ├── __init__.py
│   ├── expense_tracker.py   ← ALL business logic lives here
│   └── main.py              ← CLI menu only; no business logic
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
│   └── copilot-instructions.md   ← this file
├── .gitignore
└── README.md
```

---

## Coding Conventions

- Language: **Python 3** (standard library only)
- Style guide: **PEP 8**
- Function naming: `snake_case`
- Constants: `UPPER_SNAKE_CASE`
- Docstrings: required on all public functions
- Validation: raise `ValueError` with descriptive messages
- Separation: business logic in `expense_tracker.py`, I/O in `main.py`

---

## Data Model

Each expense is a plain Python dictionary:

```python
{
    "id": int,           # auto-incremented, starts at 1
    "description": str,  # non-empty, stripped
    "amount": float,     # positive, rounded to 2 decimal places
    "category": str,     # non-empty, stripped
    "date": str,         # YYYY-MM-DD format
}
```

Expenses are stored in a module-level list (`_expenses`) in `expense_tracker.py`.

---

## Running the Application

```bash
python src/main.py
```

## Running the Tests

```bash
python -m unittest discover -s tests -v
```

---

## What NOT to Suggest

- Databases (SQLite, PostgreSQL, etc.)
- Web frameworks (Flask, FastAPI, Django)
- Third-party packages (pandas, rich, click, etc.)
- File persistence (JSON/CSV read-write on disk)
- GUIs or web frontends
- Authentication, multi-user support, budgets, analytics

---

## Test Isolation Rule

Every test class must call `reset_expenses()` in `setUp()` to clear the
in-memory store before each test. This is mandatory for test independence.
