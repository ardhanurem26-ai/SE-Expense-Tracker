# Experiment Report

## AI-Augmented Software Development Environment Using a Personal Expense Tracker

**Institution:** Veermata Jijabai Technological Institute (VJTI)
**Subject:** Software Engineering Practical
**Student:** [Aditya Dhanure]
**Date:** October 2024

---

## 1. Experiment Title

AI-Augmented Software Development Environment Using a Personal Expense Tracker

---

## 2. Aim

To demonstrate how an AI coding assistant (Antigravity AI) can support the
complete software development lifecycle — including code generation, code
explanation, test generation, debugging, refactoring, and documentation — while
a human developer reviews, validates, and takes ownership of the final
deliverable.

---

## 3. Objectives

1. Implement a backend-only Personal Expense Tracker in Python using basic
   data structures and standard-library modules.
2. Use an AI coding assistant at each stage of development and document the
   interaction.
3. Generate and run a comprehensive unit test suite using `unittest`.
4. Apply PEP 8 coding standards and document them.
5. Maintain a Git repository with a clean commit history.
6. Practise human review and validation of AI-generated code.

---

## 4. Problem Statement

Manual expense tracking is tedious and error-prone. A simple command-line
application can help a user record, view, and analyse personal expenses during a
session. The challenge is to implement this application using an AI assistant as
a development aid — not as a replacement for human understanding — and to show
that the human developer can validate, debug, and improve AI-generated code.

---

## 5. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python 3 | Programming language |
| `unittest` (standard library) | Automated unit testing |
| Git | Version control |
| GitHub | Remote repository hosting |
| Antigravity AI (IDE assistant) | Code generation, explanation, debugging |
| VS Code | Code editor |
| PEP 8 | Coding style guide |

No third-party Python packages were used. The application runs entirely on the
Python standard library.

---

## 6. Project Structure

```
expense_tracker/
├── src/
│   ├── __init__.py
│   ├── expense_tracker.py   # Business logic, validation, in-memory storage
│   └── main.py              # Command-line interface (menu loop)
├── tests/
│   ├── __init__.py
│   └── test_expense_tracker.py   # 29 unit tests
├── docs/
│   ├── AI_ENGINEERING_JOURNAL.md
│   ├── HUMAN_VALIDATION.md
│   └── EXPERIMENT_REPORT.md      # this file
├── config/
│   └── coding_standards.md
├── .github/
│   └── copilot-instructions.md
├── .gitignore
└── README.md
```

---

## 7. Implementation Methodology

### In-Memory Data Model

Expenses are stored in a module-level Python list:

```python
_expenses: list[dict] = []
```

Each expense is a dictionary:

```python
{
    "id": int,           # auto-incremented
    "description": str,
    "amount": float,     # positive, rounded to 2 d.p.
    "category": str,
    "date": str,         # YYYY-MM-DD
}
```

### Layered Design

| Layer | File | Responsibility |
|---|---|---|
| Business Logic | `expense_tracker.py` | Validation, CRUD, totals, filtering |
| CLI | `main.py` | User input, output formatting, menu loop |
| Tests | `test_expense_tracker.py` | Automated verification of logic layer |

This separation ensures that unit tests can exercise the logic layer without
simulating terminal input.

### Validation Strategy

All inputs are validated in `add_expense()` and `filter_expenses_by_category()`:
- Descriptions and categories must be non-empty after stripping whitespace.
- Amounts must be convertible to `float` and strictly positive.
- Dates must match `YYYY-MM-DD` using `datetime.strptime()`.
- Invalid IDs in `delete_expense()` raise `ValueError` with a descriptive message.

---

## 8. AI-Assisted Development Activities

The following activities were performed with AI assistance. Full details are in
`docs/AI_ENGINEERING_JOURNAL.md`.

1. **Requirements Analysis** — AI helped scope the project and design the data model.
2. **Code Generation** — AI generated the initial `expense_tracker.py` and `main.py`.
3. **Code Explanation** — AI explained the purpose of `reset_expenses()` and the
   importance of test isolation.
4. **Test Generation** — AI generated 29 unit tests covering happy-path, edge-case,
   and error scenarios.
5. **Debugging** — AI identified a floating-point rounding bug in the test suite
   (banker's rounding in Python's `round()`) and provided the correct fix.
6. **Refactoring Review** — AI reviewed the code for readability; no additional
   changes were required.
7. **Documentation** — AI generated README, coding standards, copilot instructions,
   and this report.

---

## 9. Unit Testing and Results

### Test Suite Structure

| Test Class | Tests | Focus |
|---|---|---|
| `TestAddExpense` | 12 | Valid addition, all validation failures |
| `TestGetAllExpenses` | 3 | Empty list, count, copy independence |
| `TestCalculateTotalExpenses` | 3 | Empty, single, multiple |
| `TestFilterExpensesByCategory` | 4 | Match, case-insensitivity, no-match, empty input |
| `TestDeleteExpense` | 7 | Valid delete, non-existent, invalid types |
| **Total** | **29** | |

### Test Results

```
Ran 29 tests in 0.005s

OK
```

**All 29 tests passed.** One test failure was identified and corrected during
development (floating-point rounding; see Activity 5 in the journal).

---

## 10. Human Validation and Review

After AI-generated code was produced, the student performed the following
manual validation steps:

- Read every line of `expense_tracker.py` and confirmed that validation logic
  is correct.
- Read every line of `main.py` and confirmed that no business logic is present
  in the CLI layer.
- Ran the test suite and verified the output manually.
- Identified the rounding test failure and understood the root cause before
  applying the fix.
- Reviewed documentation for accuracy.

Details are in `docs/HUMAN_VALIDATION.md`.

---

## 11. Git and Version-Control Workflow

### Repository

- Remote: `https://github.com/ardhanurem26-ai/SE-Expense-Tracker.git`
- Branch: `main`
- Initial commit: `fb2e28f First Commit`

### Recommended Commands for the Student

```bash
# Stage all new and modified files
git add .

# Commit with a descriptive message
git commit -m "feat: implement Personal Expense Tracker with tests and docs"

# Push to GitHub (run only when ready)
git push origin main
```

### What Was NOT Done
- Force push was not used.
- Remote URL was not changed.
- Existing commit history was preserved.
- Changes were not pushed to GitHub without explicit student authorisation.

---

## 12. Security, Privacy, and Responsible AI Considerations

- **No real financial data** was entered into AI prompts. All example amounts
  used in tests and documentation are fictitious.
- **No secrets** (API keys, passwords, tokens) are stored in the repository.
- AI-generated code was **reviewed by a human** before being committed.
- The `.gitignore` prevents `__pycache__` and `.pyc` files from being tracked.
- The AI assistant was used as a **tool**, not as an authority. Every suggestion
  was evaluated before acceptance.

---

## 13. Conclusion

This experiment demonstrates that an AI coding assistant can significantly
accelerate the development of a Python application by generating boilerplate
code, validation logic, unit tests, and documentation. However, AI assistance
does not eliminate the need for human review. In this project, a test failure
caused by Python's floating-point rounding behaviour was only detected because
the test suite was actually run — the AI-generated test assertion was
technically wrong. This reinforces the principle that **AI-generated code must
always be reviewed and tested by a human**.

The Personal Expense Tracker meets all stated requirements: add, view, total,
filter, and delete expenses through a command-line menu, with validated input,
isolated unit tests, and clean separation between business logic and the CLI.

---

## 14. Answers to the Ten Questions

### Q1. What is an AI-augmented software development environment?

An AI-augmented software development environment is a development setup in which
AI tools — such as code assistants, code generators, and documentation helpers —
are integrated into the developer's workflow to increase productivity. The AI
assists with repetitive or boilerplate tasks (writing tests, generating
docstrings, spotting bugs), while the human developer retains responsibility for
design decisions, correctness validation, and understanding the code.

In this project, Antigravity AI was used inside VS Code to generate the initial
implementation, write unit tests, and explain Python behaviour such as banker's
rounding.

---

### Q2. Why is Git or version control important in software development?

Version control allows developers to track every change made to a codebase over
time. It provides:
- A complete history of who changed what and when.
- The ability to revert to a previous working state if a change introduces a bug.
- Safe experimentation through branches.
- Collaboration support for teams working on the same codebase.

In this project, Git is used to record the progression from an empty repository
to a complete expense tracker, with meaningful commit messages that explain each
change.

---

### Q3. What is an AI coding assistant?

An AI coding assistant is a software tool, typically integrated into a code
editor, that uses a large language model (LLM) to help developers write code
faster and more accurately. It can complete code, generate entire functions,
explain existing code, suggest fixes for bugs, and write tests.

Examples include GitHub Copilot, Cursor, and the Antigravity AI assistant used
in this experiment. The key distinction is that the AI suggests code — the human
reviews and decides whether to accept, modify, or reject the suggestion.

---

### Q4. What is repository context, and why is it useful?

Repository context refers to the files, folder structure, coding conventions,
and existing code in a project that an AI assistant can read to understand the
codebase before generating new suggestions. When an AI has repository context,
its output is more consistent with the project's existing style, naming
conventions, and architecture.

In this project, the `.github/copilot-instructions.md` file provides explicit
repository context: it describes the project structure, the data model, which
functions exist, and what the AI should not suggest (databases, GUI, third-party
packages).

---

### Q5. What is an AI engineering journal?

An AI engineering journal is a structured log that records every interaction
between a developer and an AI coding assistant during a project. Each entry
documents the activity performed, the prompt or instruction given to the AI, the
output the AI produced, and the human's validation decision.

The journal serves as evidence that the developer understood and reviewed the
AI's contributions, and it provides a record of what was human-authored vs.
AI-assisted. In this project, `docs/AI_ENGINEERING_JOURNAL.md` is the journal.

---

### Q6. Why should developers review AI-generated code?

AI models generate statistically likely code, not provably correct code. They
can:
- Produce subtle logic errors (as seen in the rounding test in this project).
- Suggest deprecated or insecure practices.
- Miss project-specific constraints that were not in the prompt.
- Generate code that looks correct but fails on edge cases.

In this project, the AI-generated test `round(10.555, 2) == 10.56` was wrong due
to Python's floating-point representation. Running the tests caught the failure;
the developer then understood the root cause and applied the correct fix.

---

### Q7. How can coding standards be enforced in a project?

Coding standards can be enforced in multiple ways:
- **Documentation:** Write a `coding_standards.md` file that all contributors
  must follow (as done in this project).
- **Linting tools:** Tools like `ruff` automatically check for PEP 8 violations.
- **Formatters:** `black` automatically reformats code to a consistent style.
- **Code review:** Peer or mentor review of pull requests before merging.
- **CI/CD pipelines:** Automated checks that run linters on every commit.

In this project, standards are documented in `config/coding_standards.md` and
the AI was instructed to follow them via `copilot-instructions.md`.

---

### Q8. Why is unit testing important?

Unit tests automatically verify that individual functions behave correctly.
They:
- Catch bugs introduced by new changes (regression testing).
- Document the expected behaviour of functions (tests as specification).
- Allow safe refactoring — if tests still pass, behaviour is unchanged.
- Provide confidence to developers when extending or modifying code.

In this project, the 29 unit tests catch the rounding bug and confirm that every
validation rule (empty descriptions, negative amounts, invalid dates, etc.) works
as specified.

---

### Q9. What information should never be shared with an AI coding assistant?

Developers should never share:
- **Real personal financial data** (actual transactions, account numbers).
- **Passwords, API keys, or authentication tokens**.
- **Proprietary source code** that the organisation has not authorised to share.
- **Personally identifiable information (PII)** about themselves or others.
- **Database connection strings** or internal server addresses.

In this experiment, all amounts and descriptions in prompts and test data are
fictitious (e.g., "Lunch", 150.0). No real financial information was disclosed.

---

### Q10. How does repository context improve AI-generated code?

When an AI assistant has access to repository context — the project's folder
structure, existing code, naming conventions, and a dedicated instructions file
— its suggestions align much more closely with the project's actual requirements.

Without context, an AI might suggest a Flask API or a SQLite database for an
expense tracker. With the `copilot-instructions.md` file in this project
explicitly stating "backend-only, no database, no third-party packages," the AI
correctly generated simple in-memory Python functions that matched the
assignment's constraints. Context also helps the AI use the same naming
conventions (`snake_case`, `_expenses`, `_next_id`) and follow the same
validation patterns as the rest of the codebase.
