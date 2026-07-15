# Week 3 — Functions, Files & Exceptions

## Why this week matters

You cannot build maintainable programs without **functions** to organize code, **file I/O** to persist data, and **exception handling** to gracefully manage errors. By Friday you will write reusable functions with flexible signatures, read and write files safely, and handle errors without crashing your programs.

⚠️ **Week 3 is compressed.** Session 2 covers lambda, file I/O, exceptions, AND custom errors in 90 minutes, then kicks off the final project. Two projects (Cart Engine and Log Analyzer) are both due Wednesday. This is the tightest timeline in the course. Attend office hours if you get stuck—there's no safety net before Week 4's review.

## Objectives — by Friday night you should be able to:

- Write functions with positional, keyword, default parameters, `*args`, and `**kwargs`.
- Explain the LEGB scope rule and predict variable lookup behavior.
- Use lambda expressions with `sorted()`, `filter()`, and `map()`.
- Read and write files using context managers (`with` statement).
- Catch specific exceptions and handle errors gracefully.
- Create custom exception classes for domain-specific errors.

## Sessions

| Session | Date | Covers | Handbook |
|---|---|---|---|
| Session 1 (Thu) | **30-min Review: Contact Book** → Functions | Review anonymized Week 2 bugs, then: function anatomy, arguments (positional, keyword, default, *args, **kwargs), scope (LEGB), docstrings, pure functions | [`session-1-functions/`](./session-1-functions/) |
| Session 2 (Fri) | Lambda, File I/O, Exceptions, Custom Errors | Lambda syntax and use cases, file modes and context managers, try/except/else/finally, exception hierarchy, custom exception classes, **Final Project (IMS) kickoff briefing** | [`session-2-lambda-files-exceptions/`](./session-2-lambda-files-exceptions/) |

## Weekend assessment

Once both sessions are done, work through **[`assessment/README.md`](./assessment/README.md)** — Saturday through Wednesday. It is not graded. It is the *only* material next Thursday's 30-minute review will be built from, so treat it as required, not optional (the optional part is clearly marked separately inside it).

The projects this week are:
- **Project 3: E-Commerce Cart Engine** — uses functions with flexible arguments and lambda for discount logic
- **Project 4: Server Log Analyzer** — uses file I/O and exception handling to parse and report on server logs

Both projects are due **Wednesday night**. This is a compressed timeline by design—start early and use office hours.

## Final Project Kickoff

Session 2 includes a 15-minute briefing on **Project 6: Inventory & Invoice Management System (IMS)**—the final assessment for Week 4. You won't build it until after learning OOP, but reading the requirements now helps you start thinking about data design.

## Further reading

See **[`references.md`](./references.md)** for the official docs that back every concept taught this week.
