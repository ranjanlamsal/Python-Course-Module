# 4-Week Master Schedule — Intensive Python Bootcamp

**Format:** 8 sessions × 90 min = 12 hours. Thu/Fri live, Sat–Wed self-study/build.
**Model:** class time = concept-building only; projects are built entirely outside class.

## Summary Table

| Week | Session 1 (Thu) | Session 2 (Fri) | Self-Study / Project |
|---|---|---|---|
| **1** | Env setup (venv), variables, core types, casting, arithmetic | Conditionals, loops, break/continue | **Project 1: Smart ATM Simulator** |
| **2** | *(30 min) Review: ATM* → Lists, Tuples | Dictionaries, Sets | **Project 2: Contact Book Manager** |
| **3** | *(30 min) Review: Contact Book* → Functions (anatomy, args, scope) | Lambda expressions → File I/O, Exceptions, Custom Errors → **Final Project kickoff briefing** | **Project 3: E-Commerce Cart Engine** + **Project 4: Server Log Analyzer** |
| **4** | *(30 min) Review: Cart Engine + Log Analyzer* → Classes, Instances, Attributes, Encapsulation, Inheritance | Polymorphism, Abstraction, Magic Methods → assign Final Project (full spec) + optional Project 5 | **Final Project 6: Inventory & Invoice Management System (IMS)** — mandatory, no in-class review. **Project 5: RPG Arena** — optional, ungraded extra OOP reps. |

Note: Project 3 and Project 4 are assigned together after Week 3 (both phases are compressed into that week — see risk assessment). Project 6 (IMS) is introduced in Week 3 but not built until Week 4's OOP content lands; it has no in-class review since there is no Week 5 — it is the terminal assessment.

---

## Session-by-Session Breakdown

### Week 1, Session 1 — Environment, Variables, Types, Arithmetic
- **Live-coded snippet (~8 lines):** A Celsius→Fahrenheit converter: `input()`, explicit `int()`/`float()` casting, one arithmetic expression, an f-string print.
- **Maps to Project 1 without being it:** ATM needs to read user input and cast it to numbers, and do arithmetic on a balance — this isolates that mechanic in a domain with no accounts, PINs, or menus.
- **Independent reading:** venv creation/activation, PEP 8 basics, int/float/str/bool reference, operator precedence table.

### Week 1, Session 2 — Conditionals, Loops
- **Live-coded snippet (~10 lines):** A "guess a hardcoded number 1–10" loop: `while` with an attempt counter capped at 3, `break` on success, an `else` on the loop for "out of attempts."
- **Maps to Project 1 without being it:** This is the exact shape of the ATM's 3-attempt PIN check and its `while True` menu-with-`break`, but in a domain (number guessing) that shares no vocabulary with banking — it can't be copy-pasted into the ATM.
- **Independent reading:** `for` vs `while` use cases, `continue` vs `break` vs `pass`, truthy/falsy values, nested conditionals.

### Week 2, Session 1 — Review (30 min) + Lists, Tuples
- **Review targets (anonymized ATM bugs):** PIN compared as `int` vs `str`, balance going negative from wrong validation order, infinite loops missing a `break`, `elif` chains that accidentally fire multiple branches.
- **Live-coded snippet (~10 lines):** A plain number list — `append`, `pop`, `sort`, slicing — plus a tuple `point = (3, 4)` unpacked into `x, y`.
- **Maps to Project 2 without being it:** Contact Book needs a mutable, sortable collection and needs to understand tuple immutability vs. mutable structures — shown on numbers/coordinates, not contacts.
- **Independent reading:** list methods reference, list comprehensions (intro only), why tuples for fixed data.

### Week 2, Session 2 — Dictionaries, Sets
- **Live-coded snippet (~12 lines):** A `fruit → color` dict — `.get()`, `.items()` iteration, updating a value — plus a set deduplicating a list of numbers and one `union()` example.
- **Maps to Project 2 without being it:** Contact Book's nested-dict-per-entry structure and case-insensitive lookup pattern, and using a set-style dedup check for duplicate entries — demonstrated on fruit/colors and raw numbers instead.
- **Independent reading:** nested dictionaries, dict vs list tradeoffs, set algebra (union/intersection/difference).

### Week 3, Session 1 — Review (30 min) + Functions (anatomy, arguments, scope)
- **Review targets (anonymized Contact Book bugs):** search not using `.lower()` (case-sensitivity bugs), mutating a "global" dict inside a helper instead of passing/returning it, one giant unstructured script with no functions yet.
- **Live-coded snippet (~14 lines):** `def describe_pet(name, species="dog", *tricks, **extra_info):` — default params, `*args`, `**kwargs`, and a local-vs-global scope demo using the `global` keyword on a counter.
- **Maps to Project 3 without being it:** This is the exact signature shape of `calculate_total(cart_items, discount_coupon=None)` with `**kwargs` for fees — shown on pets/tricks, not carts.
- **Independent reading:** docstrings, `return` vs `print`, LEGB scope rule, what makes a function "pure."

### Week 3, Session 2 — Lambda → File I/O, Exceptions, Custom Errors → Final Project Kickoff
- **Live-coded snippet A, lambda (~8 lines):** `sorted(word_pairs, key=lambda pair: pair[1])` on a list of `(word, length)` tuples, plus one `filter(lambda n: n % 2 == 0, numbers)`.
  - **Maps to Project 3:** the inline lambda-inside-`filter()` pattern the Cart Engine needs for discount scaling — shown on words/numbers, not prices.
- **Live-coded snippet B, files/exceptions (~15 lines):** `with open(...)` reading a small text file line by line, `try/except` catching `ValueError` (bad `int()` cast) and `FileNotFoundError`, then a custom `class TooShortError(Exception): pass` raised from a length-check function.
  - **Maps to Project 4:** the exact file-opening/`FileNotFoundError` and malformed-line handling the Log Analyzer needs — shown on generic notes, not log tags.
- **Independent reading:** file modes (r/w/a), context managers, exception hierarchy, `try/except/else/finally`, defining custom exception classes.
- **Final Project kickoff (~15 min, no code):** Walk through the IMS requirements only (products, checkout, invoices, sales-history files, full OOP). Frame it explicitly: "this uses everything you know now, plus the OOP we start next week." No building starts yet — this is scope-setting so students can start thinking about data design over the coming self-study block.

### Week 4, Session 1 — Review (30 min) + Classes, Instances, Attributes, Encapsulation, Inheritance
- **Review targets (anonymized Cart Engine + Log Analyzer bugs):** wrong/missing `key=` argument on `sorted`/`filter`, mutating the original `cart_items` list in place, bare `except:` swallowing real errors, forgetting `with` and leaving files open, miscounted tag aggregation.
- **Live-coded snippet (~15 lines):** A generic `Animal` class — `__init__(self, name)`, a "private" `__sound` attribute behind a getter/setter, and a `Dog(Animal)` subclass calling `super().__init__()` and overriding `speak()`.
- **Maps to Projects 5 & 6 without being either:** this is the private-attribute + `super()` inheritance shape both the RPG's `Character` base class and the IMS's product/entity hierarchy need — shown on animals, not characters or products.
- **Independent reading:** class vs. instance attributes, `self`, `@property` decorator, inheritance vs. composition.

### Week 4, Session 2 — Polymorphism, Abstraction, Magic Methods → Assign Final Project + Project 5
- **Live-coded snippet (~15 lines):** An `abc`-based `Shape` abstract class with an abstract `area()`, two subclasses `Circle`/`Square` implementing it differently, plus a small `Point` class demoing `__str__` and `__eq__`.
- **Maps to Projects 5 & 6 without being either:** the abstract-base + polymorphic-override pattern (RPG's `Character.attack()`, IMS's polymorphic line items) and custom object printing/comparison — shown on shapes and points, not characters or invoices.
- **Independent reading:** the `abc` module, common magic methods (`__add__`, `__repr__`), duck typing.
- **Assignments given here:**
  - **Final Project (Project 6 — IMS):** full spec, mandatory, the sole final assessment. No in-class review will occur — build it against this session's snippet patterns and everything from Weeks 1–4.
  - **Project 5 (RPG Arena):** explicitly framed as optional, ungraded, extra OOP repetition. Not reviewed, not required. Students who feel shaky on inheritance/polymorphism should do this first, before or alongside the IMS.

---

## Risk Assessment

**🔴 Highest risk — Week 3, Session 2 (Fri).** This single 90-minute session carries: the tail of Phase 3 (lambda), all of Phase 4 (file I/O, exceptions, custom errors), *and* the Final Project kickoff. Two projects (Cart Engine and Log Analyzer) get assigned off the back of it, due in the same five-day window. Exceptions and custom errors — a genuinely new mental model for beginners — get one snippet and roughly 30–35 minutes of live treatment before students are expected to build a file-parsing tool that leans on exactly that. This is where students will silently get stuck with no safety net before the next class. **Mitigation:** post a written exception-handling reference/FAQ the same day, hold optional office hours mid-week, and don't be surprised if Week 4's review skews heavily toward Log Analyzer bugs over Cart Engine bugs.

**🟠 Second risk — Week 4 overall.** OOP is the single hardest conceptual jump in the syllabus (4 pillars + magic methods), compressed into 2 sessions minus a 30-minute review, immediately followed by a final project that must integrate OOP *with* file I/O, exceptions, and functions simultaneously — the first time everything is combined. There is no in-class review of this integration before submission. **Mitigation:** the Week 4 kickoff briefing (already scheduled in Week 3) is load-bearing — do not let it slip or shrink, since it's the only head start students get on IMS's data design before OOP is even taught.

**🟡 Lower risk — Week 2.** Dictionaries-of-dictionaries (needed for Contact Book) are taught same-day as sets, with sets getting comparatively little runway. Low risk because the project's core structure (nested dict) is covered directly; sets are a minor feature by comparison.

**🟢 Low risk — Week 1.** Full two sessions, no review overhead, straightforward mapping from control flow to the ATM's loop/conditional structure. This week has the most in-class support per unit of project complexity.
