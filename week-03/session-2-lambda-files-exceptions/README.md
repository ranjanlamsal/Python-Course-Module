# Session 2 — Lambda, File I/O, Exceptions

**Duration:** 90 minutes (very compressed!)

## Overview

This is the most packed session in the course. In 90 minutes you'll learn:
- **Lambda expressions:** anonymous functions for inline transformations
- **File I/O:** reading and writing files safely with context managers
- **Exceptions:** handling errors gracefully with try/except
- **Custom errors:** creating domain-specific exception classes
- **Final Project kickoff:** 15-minute IMS briefing (not built until Week 4)

⚠️ **This session is the highest-risk in the course.** Two major topics (files + exceptions) that beginners find conceptually new, plus lambda, plus the final project intro—all in 90 minutes. Start the projects early and use office hours.

## Handbooks

Read these in order:

1. **[01-lambda-expressions.md](./01-lambda-expressions.md)**
   - Syntax: `lambda args: expression`
   - When (and when NOT) to use lambda
   - Common use cases: `sorted()`, `filter()`, `map()`

2. **[02-file-io.md](./02-file-io.md)**
   - File modes: 'r', 'w', 'a'
   - Context managers: `with open(...)` 
   - Reading and writing methods
   - Why `with` prevents resource leaks

3. **[03-exceptions-and-custom-errors.md](./03-exceptions-and-custom-errors.md)**
   - Exception hierarchy
   - try/except/else/finally structure
   - Catching specific exceptions
   - Creating custom exception classes
   - Why bare `except:` is dangerous

## Code Demos

All demo files are runnable:

- **[`demo_lambda_basics.py`](./code/demo_lambda_basics.py)** — Lambda syntax and simple examples
- **[`demo_lambda_with_filter_sorted.py`](./code/demo_lambda_with_filter_sorted.py)** — The exact examples from class: `sorted()` and `filter()` with lambda
- **[`demo_file_reading.py`](./code/demo_file_reading.py)** — Reading files line-by-line with context managers
- **[`demo_file_writing.py`](./code/demo_file_writing.py)** — Writing to files safely
- **[`demo_exceptions.py`](./code/demo_exceptions.py)** — try/except for ValueError and FileNotFoundError
- **[`demo_custom_errors.py`](./code/demo_custom_errors.py)** — The TooShortError example from class
- **[`sample_data.txt`](./code/sample_data.txt)** — Sample file for file I/O demos

## Key Takeaways

- **Lambda:** Use for simple inline transformations (`sorted(key=...)`, `filter()`, `map()`). For complex logic, use a named function.
- **File I/O:** Always use `with open(...)` to ensure files close, even if an exception occurs.
- **Exceptions:** Catch *specific* exceptions (`ValueError`, `FileNotFoundError`), not bare `except:`. Handle what you expect, let the rest propagate.
- **Custom errors:** Create domain-specific exceptions (`class OutOfStockError(Exception)`) for clarity.

## Final Project Kickoff (15 min)

The **Inventory & Invoice Management System (IMS)** is the Week 4 final assessment. It combines:
- Functions (this week)
- File I/O (this week)
- Exceptions (this week)
- OOP: Classes, Inheritance, Polymorphism (next week)

You won't build it until Week 4, but reading the requirements now helps you start thinking about data design. **Don't start coding it yet**—just read the spec and sketch ideas.

## What's Next

Session 2 immediately launches into two projects:
- **Project 3: Cart Engine** — uses functions and lambda
- **Project 4: Log Analyzer** — uses file I/O and exceptions

Both are due Wednesday night. Start Saturday morning, not Sunday night.
