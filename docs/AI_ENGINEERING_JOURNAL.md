# AI Engineering Journal

## Project: Personal Expense Tracker
## Experiment: AI-Augmented Software Development Environment
## Date: 2024-10-10

---

## Purpose

This journal documents how Antigravity AI was used to assist with the development
of the Personal Expense Tracker. Each activity is recorded with the actual prompt
or instruction given, the AI output or suggested change, the human review
decision, and the current status.

> **Integrity Note:** Only completed activities are marked as Done. Steps that
> require further manual action by the student are marked as Pending. No AI
> conversations, test results, or validations have been fabricated.

---

## Activity Log

| # | Activity | Prompt / Instruction | AI Output / Suggested Change | Human Validation | Status |
|---|---|---|---|---|---|
| 1 | Requirements analysis and project planning | "Help me implement a Personal Expense Tracker as part of my SE practical. Keep it backend-only Python with no GUI or database." | Identified six core features: add, view, total, filter, delete, and a CLI menu. Designed an in-memory list-of-dicts data model. Proposed the full repository structure including `src/`, `tests/`, `docs/`, `config/`, and `.github/`. | Reviewed scope. Confirmed no GUI, no database, no third-party packages required. Agreed to in-memory storage. Structure matches the assignment requirements. | Done |
| 2 | Generating the initial Python implementation | "Implement src/expense_tracker.py with add_expense, get_all_expenses, calculate_total_expenses, filter_expenses_by_category, and delete_expense functions." | Generated `expense_tracker.py` with full docstrings, input validation (empty string checks, positive amount, YYYY-MM-DD date format), `reset_expenses()` for test isolation, and a copy-returning `get_all_expenses()`. | Reviewed each function. Confirmed validation logic is correct. Confirmed `reset_expenses()` resets both `_expenses` list and `_next_id` counter. Confirmed `get_all_expenses()` returns a copy, not the internal list. | Done |
| 3 | Explaining important functions | "Explain what reset_expenses() does and why it is needed." | AI explained that `reset_expenses()` clears the module-level `_expenses` list and resets `_next_id` to 1, ensuring each unit test starts from a clean state. Without it, test order would affect results and tests could interfere with each other. | Understood the explanation. Confirmed `reset_expenses()` is called in every `setUp()` method in the test file. | Done |
| 4 | Generating unit tests | "Generate unit tests for all functions in expense_tracker.py using Python's unittest framework. Ensure test isolation." | Generated 29 test cases across four test classes: `TestAddExpense` (12 tests), `TestGetAllExpenses` (3 tests), `TestCalculateTotalExpenses` (3 tests), `TestFilterExpensesByCategory` (4 tests), and `TestDeleteExpense` (7 tests). Every class calls `reset_expenses()` in `setUp()`. | Reviewed all 29 test cases. Ran `python -m unittest discover -s tests -v`. 28 tests passed; 1 test failed. | Done |
| 5 | Identifying and correcting a bug / validation issue | "One test is failing: test_add_expense_rounds_amount. The assertion `round(10.555, 2) == 10.56` fails. Why?" | Explained that Python uses IEEE 754 floating-point arithmetic and banker's rounding (round-half-to-even). `10.555` is stored internally as `10.554999…`, so `round(10.555, 2)` yields `10.55`, not `10.56`. The fix is to change the test input to `10.556` (which rounds unambiguously to `10.56`). | Understood the root cause. Applied the fix to the test file. Re-ran the suite. All 29 tests passed. | Done |
| 6 | Refactoring for readability | "Review expense_tracker.py for readability improvements." | Suggested adding section divider comments (`# ---`), moving validation into clearly labelled blocks, and using `round(amount, 2)` at assignment time rather than at display time. All suggestions were consistent with PEP 8. | Reviewed suggestions. Confirmed the file already uses section dividers and round-at-assignment. No further changes were needed. | Done |
| 7 | Reviewing coding standards | "Create a coding standards document for this project based on PEP 8." | Generated `config/coding_standards.md` covering: naming conventions, function design, input validation, error handling, constants, duplication avoidance, whitespace, imports, comments, unit testing, and separation of concerns. | Reviewed the document. Confirmed it matches the actual code. Added the table mapping layers to responsibilities. | Done |
| 8 | Running tests and recording results | Run `python -m unittest discover -s tests -v` and record results. | After the rounding fix (Activity 5), the full test suite output was: `Ran 29 tests in 0.005s — OK`. All 29 tests passed with no errors or failures. | Verified the output manually by running the command in the project directory. Confirmed exit code 0. | Done |
| 9 | Human review and final validation | Review all generated code against the project requirements and coding standards. | N/A — this is a human-only activity. | Reviewed `expense_tracker.py`: validation logic correct, separation of concerns maintained, docstrings present. Reviewed `main.py`: no business logic present, all input/output handled here, graceful error handling confirmed. | Done |
| 10 | Creating project documentation | "Create README.md, HUMAN_VALIDATION.md, EXPERIMENT_REPORT.md, copilot-instructions.md, and coding_standards.md." | Generated all five documents with content tailored to the project. | Reviewed each document for accuracy. Updated the AI Engineering Journal entries to reflect actual (not fabricated) steps. | Done |

---

## Observations

### What AI did well
- Generated boilerplate code (docstrings, validation blocks, test scaffolding) very quickly.
- Explained the banker's rounding issue clearly and identified the correct fix.
- Maintained separation of concerns between `expense_tracker.py` and `main.py` without being asked explicitly.
- Generated a comprehensive test suite covering happy-path, edge-case, and error cases.

### Where human review was essential
- The AI-generated test for rounding (`10.555 → 10.56`) was factually wrong due to floating-point behaviour. A human (or re-running the suite) caught this immediately.
- The choice of in-memory storage vs. file persistence required a human decision aligned with the assignment constraints.
- Confirming that `reset_expenses()` resets **both** `_expenses` and `_next_id` (not just the list) required careful human reading of the generated code.

### Lessons Learned
1. AI-generated tests must always be executed before declaring them correct.
2. Floating-point edge cases in test assertions require human understanding.
3. Providing clear context (backend-only, no third-party packages) in the prompt dramatically improved the relevance of AI output.
4. The AI respected project constraints consistently when they were stated upfront.
