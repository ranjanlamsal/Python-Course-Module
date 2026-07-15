# Session 1 — Functions

**Duration:** 90 minutes (30 min review + 60 min new content)

## Overview

Functions are the foundation of code organization. They let you name a block of logic, reuse it, test it in isolation, and compose larger programs from smaller, understandable pieces.

This session covers:
- **30-minute review:** Anonymized bugs from Week 2's Contact Book project
- **Function anatomy:** `def`, parameters, `return`, calling
- **Flexible signatures:** default params, `*args`, `**kwargs`
- **Scope:** LEGB rule, `global` keyword (and why to avoid it)
- **Best practices:** docstrings, pure functions, `return` vs `print`

## Handbooks

Read these in order:

1. **[01-function-anatomy-and-arguments.md](./01-function-anatomy-and-arguments.md)**
   - Function definition syntax
   - Positional, keyword, and default arguments
   - `*args` and `**kwargs` for flexible APIs

2. **[02-scope-and-best-practices.md](./02-scope-and-best-practices.md)**
   - LEGB scope resolution
   - When (not) to use `global`
   - Pure functions, side effects, docstrings

## Code Demos

All demo files are runnable. Type them out yourself, experiment with modifications:

- **[`demo_function_basics.py`](./code/demo_function_basics.py)** — Simple functions, parameters, return values
- **[`demo_args_kwargs.py`](./code/demo_args_kwargs.py)** — `*args` and `**kwargs` in action
- **[`demo_scope.py`](./code/demo_scope.py)** — LEGB rule and variable shadowing
- **[`demo_pet_function.py`](./code/demo_pet_function.py)** — The live-coded example from class: combines default params, `*args`, `**kwargs`

## Key Takeaways

- **Functions organize code.** Your Contact Book likely has duplicate logic—functions fix that.
- **Flexible signatures matter.** Default params, `*args`, and `**kwargs` make APIs that grow without breaking.
- **Scope is predictable.** LEGB rule: Local → Enclosing → Global → Built-in. If a variable lookup confuses you, trace LEGB.
- **Return, don't print.** Functions that `print` their result can't compose. Functions that `return` can be tested, chained, reused.

## What's Next

Session 2 covers lambda expressions (anonymous functions), file I/O, and exception handling—the tools you need for Project 4 (Log Analyzer).
