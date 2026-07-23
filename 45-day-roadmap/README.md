# 45-Day Accelerated Python → Django Roadmap

**Who this is for:** Students who finished the 4-week (8-session) intro course and can already write basic Python (variables, loops, lists/dicts, simple functions). This roadmap takes them from "knows the basics" to "can build and deploy a real Django web app."

**How to use this document:** This is a self-study map, not a textbook. Each day lists:
- **Topic** — what to learn
- **Why** — why it matters / where it's used
- **Resources** — where to learn it (docs, blogs, YouTube channels — search the given title on the channel, links change often but titles don't)
- **Exercise** — something to actually build, so you prove you understand it

**Rules for self-study:**
1. Spend 1.5–3 hours/day. Consistency beats marathon sessions.
2. Never copy-paste code from a tutorial without retyping it yourself.
3. Every day ends with you writing code, not just reading/watching.
4. If a day's exercise breaks you, that's normal — struggle for 30 min before searching the error message.
5. Keep all your code in a personal GitHub repo, one folder per day. This becomes your portfolio.

**Structure:** 9 weeks × 5 days = 45 days. Weekends are free for review/catch-up (recommended, not required).

---

## Table of Contents
- [Week 1 – Python Fundamentals, Properly](#week-1--python-fundamentals-properly)
- [Week 2 – Data Structures Deep Dive](#week-2--data-structures-deep-dive)
- [Week 3 – Functions & The Start of OOP](#week-3--functions--the-start-of-oop)
- [Week 4 – OOP, Errors, Files](#week-4--oop-errors-files)
- [Week 5 – Intermediate Python](#week-5--intermediate-python)
- [Week 6 – Tooling, Data & the Web](#week-6--tooling-data--the-web)
- [Week 7 – Web Foundations & Django Intro](#week-7--web-foundations--django-intro)
- [Week 8 – Django Core](#week-8--django-core)
- [Week 9 – Django Advanced + Capstone](#week-9--django-advanced--capstone)

---

## Week 1 – Python Fundamentals, Properly

### Day 1 — Environment & the Command Line
**Topic:** Setting up a real dev environment: Python install, VS Code, running scripts from terminal, basic shell commands (`cd`, `ls`/`dir`, `mkdir`).
**Why:** You'll live in the terminal for the rest of this roadmap and in every real job.
**Resources:**
- YouTube: "Command Line Crash Course" — freeCodeCamp
- Blog: realpython.com → "Python Environment Setup"
**Exercise:** Create a folder `45-day-roadmap/day-01`, write a script that prints your name and today's date, run it purely from the terminal (no IDE "run" button).

### Day 2 — Variables, Data Types & Type Casting (Deep Recap)
**Topic:** int, float, str, bool, `None`; implicit vs explicit type conversion; f-strings.
**Why:** Sloppy type handling is the #1 source of bugs for beginners.
**Resources:**
- Docs: docs.python.org → "Built-in Types"
- YouTube: Corey Schafer — "Python Tutorial: Variables and Data Types"
**Exercise:** Build a small "unit converter" CLI (km↔miles, celsius↔fahrenheit) using f-strings for output.

### Day 3 — Operators & Control Flow (Deep Recap)
**Topic:** Comparison/logical/bitwise operators, `if/elif/else`, nested conditionals, `match/case` (Python 3.10+).
**Why:** Control flow is the backbone of every program's logic.
**Resources:**
- Blog: realpython.com → "Conditional Statements in Python"
- YouTube: Tech With Tim — "Python match case Tutorial"
**Exercise:** Build a simple grading system (input a score → prints letter grade) using both `if/elif` and `match/case`.

### Day 4 — Loops & Iteration (Deep Recap)
**Topic:** `for`, `while`, `break`/`continue`/`else` on loops, `range()`, nested loops, loop patterns (accumulator, counter, sentinel).
**Why:** Iteration patterns show up constantly in data processing and web backends.
**Resources:**
- Blog: realpython.com → "Python 'while' Loops"
- YouTube: Programming with Mosh — "Python Loops Tutorial"
**Exercise:** Print a multiplication table (formatted grid) and a simple number-guessing game with limited attempts.

### Day 5 — Strings Deep Dive
**Topic:** String methods (`split`, `join`, `strip`, `replace`, `format`), slicing, immutability.
**Why:** String manipulation is everywhere — parsing input, cleaning data, templating.
**Resources:**
- Docs: docs.python.org → "Text Sequence Type — str"
- YouTube: Corey Schafer — "Python String Formatting"
**Exercise:** Write a simple text-processing script: count words, find longest word, reverse each word in a sentence.

---

## Week 2 – Data Structures Deep Dive

### Day 6 — Lists & Tuples Deep Dive
**Topic:** List methods, slicing tricks, list vs tuple (mutability), tuple unpacking, nested lists.
**Why:** Lists are the most-used data structure in Python.
**Resources:**
- Blog: realpython.com → "Lists and Tuples in Python"
- YouTube: Corey Schafer — "Python Lists"
**Exercise:** Build a simple to-do list CLI app (add, remove, view, mark done) using a list of dicts.

### Day 7 — List Comprehensions
**Topic:** List/set/dict comprehensions, conditional comprehensions, nested comprehensions.
**Why:** Pythonic, faster, and expected in any real codebase.
**Resources:**
- Blog: realpython.com → "When to Use a List Comprehension in Python"
- YouTube: Corey Schafer — "Python List Comprehensions"
**Exercise:** Rewrite 5 of your earlier loop-based scripts using comprehensions.

### Day 8 — Dictionaries & Sets Deep Dive
**Topic:** Dict methods (`.get`, `.items`, `.setdefault`), dict comprehensions, sets & set operations (union, intersection).
**Why:** Dicts model real-world data (JSON, database rows); sets are key for dedup/lookup problems.
**Resources:**
- Docs: docs.python.org → "Mapping Types — dict"
- YouTube: Corey Schafer — "Python Dictionaries"
**Exercise:** Build a word-frequency counter that reads a paragraph and outputs a sorted dict of word counts.

### Day 9 — Working with Nested Data
**Topic:** Combining lists, dicts, tuples (e.g., list of dicts, dict of lists); simulating real JSON-like structures.
**Why:** This is exactly the shape of API responses and database query results you'll deal with in Django.
**Resources:**
- Blog: realpython.com → "Working With JSON Data in Python" (structure part only, skip file I/O for now)
**Exercise:** Model a small "student database" as a list of dicts (name, grades list, address dict) and write functions to compute each student's average grade.

### Day 10 — Week 1-2 Review + Mini Project
**Topic:** Consolidate everything so far.
**Resources:** None — this is a build day.
**Exercise (Mini Project):** Build a **Contact Book CLI**: add/search/delete/update contacts, stored in a list of dicts, with a menu loop. This should feel easy — if it doesn't, revisit Days 1–9.

---

## Week 3 – Functions & The Start of OOP

### Day 11 — Functions Deep Dive
**Topic:** Parameters vs arguments, default args, `*args`/`**kwargs`, return values, docstrings.
**Why:** Functions are how you organize and reuse logic — critical before OOP.
**Resources:**
- Blog: realpython.com → "Defining Your Own Python Function"
- YouTube: Corey Schafer — "Python *args and **kwargs"
**Exercise:** Refactor your Contact Book (Day 10) so every action is its own function with clear inputs/outputs.

### Day 12 — Scope & Lambda Functions
**Topic:** Local vs global scope, `global`/`nonlocal`, lambda functions, `map`/`filter`/`reduce`.
**Why:** Needed to understand closures, decorators, and functional-style Django code (e.g., queryset filtering).
**Resources:**
- Blog: realpython.com → "Python Scope"
- YouTube: Tech With Tim — "Lambda Functions in Python"
**Exercise:** Use `map`/`filter` to process a list of numbers (e.g., square all even numbers) without writing a `for` loop.

### Day 13 — Modules & Packages
**Topic:** `import`, creating your own modules, `__name__ == "__main__"`, the standard library tour (`math`, `random`, `datetime`, `os`).
**Why:** Every real project is split across multiple files/modules.
**Resources:**
- Docs: docs.python.org → "Modules"
- YouTube: Corey Schafer — "Python Modules and Packages"
**Exercise:** Split the Contact Book into multiple files (`main.py`, `contacts.py`, `utils.py`) and import between them.

### Day 14 — Virtual Environments & pip
**Topic:** `venv`, `pip install`, `requirements.txt`, why isolate project dependencies.
**Why:** Non-negotiable skill before installing Django next week.
**Resources:**
- Blog: realpython.com → "Python Virtual Environments: A Primer"
- YouTube: Corey Schafer — "Python Tutorial: VENV"
**Exercise:** Create a venv, install `requests` inside it, write a `requirements.txt`, and confirm a teammate could recreate your environment from scratch.

### Day 15 — Intro to OOP: Classes & Objects
**Topic:** `class`, `__init__`, instance attributes/methods, `self`.
**Why:** OOP is the paradigm Django itself is built on — models, views, forms are all classes.
**Resources:**
- Blog: realpython.com → "Object-Oriented Programming (OOP) in Python 3"
- YouTube: Corey Schafer — "Python OOP Tutorial 1: Classes and Instances"
**Exercise:** Model your Contact Book contacts as a `Contact` class instead of a dict.

---

## Week 4 – OOP, Errors, Files

### Day 16 — Class & Static Methods, Properties
**Topic:** `@classmethod`, `@staticmethod`, `@property`, class attributes vs instance attributes.
**Why:** Property-based access appears constantly in Django models.
**Resources:**
- YouTube: Corey Schafer — "Python OOP Tutorial 2: Class Variables" and "Tutorial 3: classmethods and staticmethods"
**Exercise:** Add a `@property` to your `Contact` class (e.g., `full_info`) and a `@classmethod` that builds a `Contact` from a raw string.

### Day 17 — Inheritance
**Topic:** Base/child classes, `super()`, method overriding.
**Why:** Django's class-based views and models rely heavily on inheritance.
**Resources:**
- YouTube: Corey Schafer — "Python OOP Tutorial 4: Inheritance"
- Blog: realpython.com → "Inheritance and Composition: A Python OOP Guide"
**Exercise:** Create a `Person` base class, then `Student` and `Teacher` subclasses that extend it differently.

### Day 18 — Polymorphism & Abstraction
**Topic:** Duck typing, abstract base classes (`abc` module), interfaces in Python.
**Why:** Understanding this makes Django's generic views and mixins click later.
**Resources:**
- Blog: realpython.com → "Inheritance and Composition" (polymorphism section)
- YouTube: ArjanCodes — "Polymorphism in Python"
**Exercise:** Give `Student` and `Teacher` a shared `describe()` method that behaves differently per class; loop over a list of mixed objects and call `describe()` on each.

### Day 19 — Exception Handling
**Topic:** `try/except/else/finally`, raising exceptions, custom exception classes.
**Why:** Production code must handle failure gracefully — this is non-optional in web apps.
**Resources:**
- Docs: docs.python.org → "Errors and Exceptions"
- YouTube: Corey Schafer — "Python Exceptions Tutorial"
**Exercise:** Add error handling to the Contact Book (e.g., handle invalid input, duplicate contacts) using a custom `DuplicateContactError`.

### Day 20 — File I/O & Working with JSON
**Topic:** Reading/writing text files, `with open(...)`, the `json` module (`json.load`/`dump`).
**Why:** This is how you'll persist data before databases enter the picture (and JSON is the language of web APIs).
**Resources:**
- Blog: realpython.com → "Reading and Writing Files in Python" and "Working With JSON Data in Python"
- YouTube: Corey Schafer — "Python Tutorial: File Objects"
**Exercise:** Make the Contact Book persist to a `contacts.json` file so data survives between runs.

---

## Week 5 – Intermediate Python

### Day 21 — Iterators & Generators
**Topic:** `__iter__`/`__next__`, `yield`, generator expressions, why generators save memory.
**Why:** Django querysets are lazy and generator-like; understanding this avoids confusing bugs later.
**Resources:**
- Blog: realpython.com → "How to Use Generators and yield in Python"
- YouTube: Corey Schafer — "Python Generators Tutorial"
**Exercise:** Write a generator that yields Fibonacci numbers up to N, and one that reads a huge file line-by-line lazily.

### Day 22 — Decorators
**Topic:** Functions as first-class objects, closures, writing your own decorators, `functools.wraps`.
**Why:** Django uses decorators constantly (`@login_required`, `@csrf_exempt`, etc.) — you must understand what they actually do.
**Resources:**
- Blog: realpython.com → "Primer on Python Decorators"
- YouTube: Corey Schafer — "Python Decorators"
**Exercise:** Write a `@timer` decorator that prints how long a function took, and a `@retry` decorator that reruns a failing function N times.

### Day 23 — Regular Expressions
**Topic:** `re` module basics: `search`, `match`, `findall`, `sub`, common patterns (email, phone, digits).
**Why:** Constantly used for form validation and data cleaning.
**Resources:**
- Blog: realpython.com → "Regular Expressions: Regexes in Python"
- Tool: regex101.com (practice patterns interactively)
**Exercise:** Write a validator function that checks if a string is a valid email and one that extracts all phone numbers from a block of text.

### Day 24 — Working with APIs (`requests`)
**Topic:** HTTP basics (GET/POST, status codes, headers), the `requests` library, parsing JSON responses.
**Why:** This is your bridge into "the web" and prep for understanding what Django does on the server side.
**Resources:**
- Blog: realpython.com → "Python's Requests Library (Guide)"
- YouTube: Corey Schafer — "Python Requests Tutorial"
**Exercise:** Pull data from a free public API (e.g., a jokes or weather API) and print formatted results; handle a failed request gracefully.

### Day 25 — Git & GitHub Properly
**Topic:** `git init/add/commit/push/pull`, branches, `.gitignore`, writing a good README, pull requests.
**Why:** You cannot collaborate on Django projects (or get hired) without real Git fluency.
**Resources:**
- Blog: Atlassian Git Tutorials (atlassian.com/git)
- YouTube: freeCodeCamp — "Git and GitHub for Beginners"
**Exercise:** Push everything you've built so far to a public GitHub repo with a proper README and a sensible commit history (not one giant commit).

---

## Week 6 – Tooling, Data & the Web

### Day 26 — SQL Fundamentals I
**Topic:** What a relational database is, tables/rows/columns, `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`.
**Why:** Django ORM is a Python layer over SQL — you must understand SQL first to understand what the ORM is doing for you.
**Resources:**
- Interactive: sqlbolt.com (do all the exercises)
- YouTube: freeCodeCamp — "SQL Tutorial for Beginners"
**Exercise:** Complete the SQLBolt exercises through the `WHERE`/filtering lessons.

### Day 27 — SQL Fundamentals II
**Topic:** `JOIN` (inner/left), `GROUP BY`, aggregate functions (`COUNT`, `SUM`, `AVG`), primary/foreign keys.
**Why:** Django's `ForeignKey` relationships map directly to this.
**Resources:**
- Interactive: sqlbolt.com (remaining lessons)
- Blog: mode.com/sql-tutorial (joins section)
**Exercise:** Design (on paper) a schema for a simple blog: `Author`, `Post`, `Comment` tables with proper foreign keys.

### Day 28 — Python + SQLite
**Topic:** `sqlite3` module, connecting, executing queries, parameterized queries (SQL injection basics).
**Why:** Hands-on bridge from raw SQL to what an ORM automates.
**Resources:**
- Docs: docs.python.org → "sqlite3 — DB-API 2.0 interface"
- YouTube: Corey Schafer — "Python SQLite Tutorial"
**Exercise:** Rebuild the Contact Book one more time — this time backed by a real SQLite database instead of JSON.

### Day 29 — HTML & CSS Crash Course
**Topic:** HTML document structure, common tags, forms, basic CSS selectors/box model.
**Why:** Django Templates generate HTML — you need to read/write basic HTML to build any UI.
**Resources:**
- Interactive: freecodecamp.org "Responsive Web Design" (first few modules only)
- YouTube: Kevin Powell — "CSS basics" playlist
**Exercise:** Hand-build a static `index.html` + `style.css` for a simple "About Me" page. No frameworks.
**Note:** Don't go deep here — 1 day is enough. Django templates will teach you the rest incrementally.

### Day 30 — HTTP & How the Web Works
**Topic:** Client-server model, request/response cycle, URLs, status codes, cookies/sessions basics.
**Why:** This is the mental model every web framework (including Django) is built on top of.
**Resources:**
- Blog: MDN Web Docs → "An overview of HTTP"
- YouTube: freeCodeCamp — "How the Web Works"
**Exercise:** Use your browser DevTools (Network tab) to inspect the request/response of visiting a real website. Identify the status code, headers, and response body.

---

## Week 7 – Web Foundations & Django Intro

### Day 31 — Django Setup & Project Structure
**Topic:** Installing Django, `django-admin startproject`, `manage.py`, project vs app structure, running the dev server.
**Why:** First contact with the framework.
**Resources:**
- Docs: docs.djangoproject.com → Official Tutorial, Part 1
- YouTube: Corey Schafer — "Django Tutorial" playlist (video 1)
**Exercise:** Create a new Django project, create one app inside it, and get "Hello World" rendering at a URL.

### Day 32 — URLs & Views
**Topic:** `urls.py`, path converters, function-based views, `HttpResponse`.
**Why:** URL routing + views is how Django decides "what code runs for this request."
**Resources:**
- Docs: docs.djangoproject.com → Official Tutorial, Part 1 (URLconf section)
- YouTube: Corey Schafer — "Django Tutorial" (URLs/views videos)
**Exercise:** Build 3 routes: a homepage, an `/about/`, and a dynamic `/greet/<name>/` that returns a personalized message.

### Day 33 — Templates
**Topic:** Django Template Language (DTL): `{{ }}`, `{% %}`, template inheritance (`{% extends %}`, `{% block %}`), passing context from views.
**Why:** This is how Python data becomes HTML pages.
**Resources:**
- Docs: docs.djangoproject.com → "Templates" topic guide
- YouTube: Corey Schafer — "Django Templates" video
**Exercise:** Build a `base.html` with a navbar, then 2 pages that extend it and display data passed from the view (e.g., a list of "projects").

### Day 34 — Models & the ORM I
**Topic:** Defining models, field types, migrations (`makemigrations`/`migrate`), the Django admin site.
**Why:** This replaces the SQLite-by-hand work from Day 28 with the ORM abstraction.
**Resources:**
- Docs: docs.djangoproject.com → Official Tutorial, Part 2
- YouTube: Corey Schafer — "Django Models" video
**Exercise:** Create a `BlogPost` model (title, content, created_at, author) and register it in `admin.py`. Add a few posts through the admin panel.

### Day 35 — Models & the ORM II
**Topic:** QuerySets (`.all()`, `.filter()`, `.get()`, `.order_by()`), `ForeignKey` relationships, `related_name`.
**Why:** This is where your SQL/JOIN knowledge from Week 6 pays off directly.
**Resources:**
- Docs: docs.djangoproject.com → "Making queries" topic guide
- YouTube: Corey Schafer — "Django QuerySets" video
**Exercise:** Add a `Comment` model with a `ForeignKey` to `BlogPost`. In a view, query and display all comments for a given post.

---

## Week 8 – Django Core

### Day 36 — Connecting Models, Views & Templates
**Topic:** Passing querysets to templates, looping in DTL (`{% for %}`), `get_object_or_404`.
**Why:** This is the full request→data→HTML loop, the core Django pattern.
**Resources:**
- Docs: docs.djangoproject.com → Official Tutorial, Part 3
**Exercise:** Build a blog list page (all posts) and a blog detail page (single post + its comments), fully wired to the database.

### Day 37 — Forms
**Topic:** `forms.Form` vs `forms.ModelForm`, rendering forms in templates, validation, CSRF tokens.
**Why:** Forms are how users create/edit data — essential for any interactive app.
**Resources:**
- Docs: docs.djangoproject.com → Official Tutorial, Part 4 (forms section) and "Working with forms" topic guide
- YouTube: Corey Schafer — "Django Forms" video
**Exercise:** Add a "Create Post" form so users can add a `BlogPost` from the browser, not just the admin panel.

### Day 38 — Class-Based Views
**Topic:** `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView` — generic CBVs.
**Why:** This connects directly back to your Week 4 inheritance/polymorphism study — CBVs are OOP in action.
**Resources:**
- Docs: docs.djangoproject.com → "Class-based views" topic guide
- YouTube: Corey Schafer — "Django Class Based Views" videos
**Exercise:** Rewrite your blog's function-based views as class-based views using the generic CBVs above.

### Day 39 — User Authentication
**Topic:** Django's built-in auth system: login/logout/register, `@login_required`, `User` model, permissions basics.
**Why:** Almost every real app needs accounts.
**Resources:**
- Docs: docs.djangoproject.com → "Using the Django authentication system"
- YouTube: Corey Schafer — "Django User Registration" videos
**Exercise:** Add login/logout/signup to the blog. Restrict "Create Post" to logged-in users only, and set `author` automatically to the logged-in user.

### Day 40 — Static Files, Media & Styling
**Topic:** `STATIC_URL`, serving CSS/JS/images, `MEDIA_ROOT` for user uploads (e.g., `ImageField`).
**Why:** Needed to make your app look like a real product, not a wireframe.
**Resources:**
- Docs: docs.djangoproject.com → "Managing static files"
- YouTube: Corey Schafer — "Django Static Files & Templates" video
**Exercise:** Style the blog with basic CSS (use your Day 29 skills) and add an optional image upload to `BlogPost`.

---

## Week 9 – Django Advanced + Capstone

### Day 41 — Intro to REST APIs with Django REST Framework
**Topic:** What REST is, installing DRF, serializers, `APIView`/`ModelViewSet`, browsable API.
**Why:** Modern apps separate frontend/backend — DRF is the industry-standard way to expose Django data as JSON.
**Resources:**
- Docs: django-rest-framework.org → Official Tutorial, Part 1–2
- YouTube: Very Academy or Corey Schafer — "Django REST Framework" intro videos
**Exercise:** Expose your `BlogPost` model as a JSON API endpoint (list + detail) using DRF.

### Day 42 — DRF: Serializers, Permissions & Auth
**Topic:** `ModelSerializer`, nested serializers (posts + comments), `permission_classes`, token/session auth basics.
**Why:** Real APIs need controlled access, not just open read access.
**Resources:**
- Docs: django-rest-framework.org → Tutorial Part 3–4
**Exercise:** Add a `CommentSerializer` nested inside `PostSerializer`, and restrict create/update endpoints to authenticated users.

### Day 43 — Testing Django Apps
**Topic:** `django.test.TestCase`, testing models/views, `pytest-django` (optional), why tests matter.
**Why:** Untested code is not production code — this is a professional-grade habit.
**Resources:**
- Docs: docs.djangoproject.com → "Writing and running tests"
- YouTube: Corey Schafer — "Python Unit Testing" (general `unittest` basics apply directly)
**Exercise:** Write at least 5 tests for the blog app (e.g., "homepage returns 200," "only logged-in users can create a post").

### Day 44 — Deployment
**Topic:** Environment variables, `DEBUG=False` settings, `requirements.txt`, deploying to a free host (Render/Railway/PythonAnywhere), `ALLOWED_HOSTS`, static file collection (`collectstatic`).
**Why:** A project only counts as "done" once someone else can visit it on the internet.
**Resources:**
- Docs: docs.djangoproject.com → "Deploying Django"
- Blog: Render.com or Railway.app official Django deployment guide (search "deploy Django" on their docs site)
**Exercise:** Deploy your blog app live. Get a real URL you can share.

### Day 45 — Capstone Project Day
**Topic:** No new topic — integrate everything.
**Why:** Proof of mastery over a checklist of topics.
**Exercise (Capstone):** Polish and ship one complete Django project that includes:
- At least 2 models with a `ForeignKey` relationship
- Full CRUD (create/read/update/delete) through both templates AND a DRF API
- User authentication with permission-restricted actions
- At least 5 automated tests
- Deployed live with a public URL
- A clean GitHub repo with a proper README (what it does, how to run it, tech used)

Ideas if you need one: a personal blog, a simple task manager, a book/movie review site, a small inventory tracker, an event RSVP app. Pick something you'd actually want to use.

---

## After Day 45 — Where to Go Next
- **Celery + Redis** — background tasks (e.g., sending emails asynchronously)
- **Docker** — containerizing your Django app
- **React or HTMX** — modern frontend paired with Django
- **PostgreSQL** — swap SQLite for a production-grade database
- **CI/CD basics** — GitHub Actions running your tests automatically

Look up "Django for Professionals" (book, by William S. Vincent) as a natural next resource once this roadmap is complete — it picks up almost exactly where Day 45 ends.
