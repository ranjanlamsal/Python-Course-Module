# Module 1 — Local Environment Setup & Isolation

> **Self-sufficiency note:** This module assumes you have no instructor in the room. Every command below is exact — type it character for character. If something doesn't match what's described, stop and re-read the step before moving forward; don't guess.

## 1.1 Installing Your Tools

You need two things installed before anything else works: **Python itself**, and **VS Code** (the editor you'll write Python in).

- **Python:** Download from the official source, `python.org` → Downloads. During installation on Windows, **check the box that says "Add Python to PATH"** — this is the single most common setup failure. On macOS/Linux, Python 3 is often preinstalled, but check the version (Step 1.2) before assuming.
- **VS Code:** Download from `code.visualstudio.com`. Once installed, open it and install the **"Python" extension** (search the Extensions panel, the icon that looks like four squares, on the left sidebar) — this gives you syntax highlighting, run buttons, and error underlining.

### 🔴 LIVE CODE DEMO — Confirming your install (terminal)

Open a terminal. In VS Code, that's **Terminal → New Terminal** from the top menu (or `` Ctrl+` `` / `` Cmd+` ``).

```bash
# Check that Python is installed and see which version you have
python --version

# On some Mac/Linux systems the command is python3, not python
python3 --version

# Confirm pip (Python's package installer) is available too
pip --version
```

**What to observe in your terminal:**
- You should see a version string like `Python 3.11.4` or similar — **any 3.10+ is fine for this course.**
- If you get `command not found` or `'python' is not recognized`, Python is not on your PATH — this is an installation problem to fix *before* continuing, not a Python problem.
- Note whether your machine uses `python` or `python3` — you'll need to use that exact word consistently for the rest of the course.

### ⚠️ Common Pitfalls
- **Using `python` when your system only has `python3`** (or vice versa) — if a command "does nothing" or errors immediately, this is the first thing to check.
- **Installing Python but skipping "Add to PATH"** on Windows — the terminal will claim Python doesn't exist even though it's installed on disk.
- **Confusing the VS Code editor window with the terminal** — code you type in the editor does not run anywhere until you either click "Run" or type a command in the terminal yourself.

---

## 1.2 Virtual Environments — Why Isolation Matters

Here's the problem a virtual environment solves: imagine two different Python projects on your laptop. Project A needs version 1.0 of a library. Project B needs version 2.0 of the *same* library. If you install libraries "globally" (system-wide), only one version can exist at a time — installing one breaks the other.

A **virtual environment (`venv`)** is a self-contained, disposable copy of Python plus its own private library folder, scoped to a single project folder. Each project gets its own isolated environment. Nothing you install inside it touches your system Python or any other project. If you break it, you delete the folder and make a new one — zero damage done.

**Rule for this course: every project folder gets its own venv, created before you write a single line of code in it.**

### 🔴 LIVE CODE DEMO — Creating and activating a venv

Run these from inside your project folder (e.g., `week-01/`):

```bash
# Create a virtual environment named ".venv" in the current folder
python -m venv .venv

# Activate it — the command differs by operating system:

# macOS / Linux:
source .venv/bin/activate

# Windows (Command Prompt):
.venv\Scripts\activate.bat

# Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

**What to observe in your terminal:**
- After running `python -m venv .venv`, a new folder named `.venv` appears in your file explorer — that's the entire isolated environment, sitting right there as files.
- After activation, your terminal prompt changes to show `(.venv)` at the start of the line — **this is your only reliable signal that the environment is active.** If you don't see it, activation failed or you're in a new terminal tab that needs re-activating.
- Run `python --version` again — it still works, but now it's *this environment's* Python, not the system one.

To leave the environment when you're done for the day: type `deactivate`.

### ⚠️ Common Pitfalls
- **Forgetting to re-activate in a new terminal tab.** Activation only lasts for the terminal session it was run in — opening a fresh terminal window means you start deactivated again. Check for `(.venv)` every time.
- **Committing the `.venv` folder to Git.** It's large, machine-specific, and regenerable — it should always be excluded via `.gitignore`, never shared.
- **Thinking `venv` installs a different Python version.** It doesn't — it isolates *libraries*, not the interpreter version itself (that comes from whichever `python` command you used to create it).

### ✅ Self-Check
1. You close your laptop mid-session, come back tomorrow, open a new terminal, and immediately run `pip install requests`. Is that install going into your project's isolated environment or somewhere else? How would you know before installing?
2. True or false: deleting the `.venv` folder deletes your project's `.py` files too.

<details>
<summary><b>Answer</b> (click to expand once you've attempted it yourself)</summary>

1. It goes **system-wide**, not into your isolated environment — a fresh terminal always starts deactivated. You'd know beforehand by checking whether `(.venv)` appears in your prompt; if it's missing, activate first with the command for your OS before installing anything.
2. **False.** `.venv` only contains the isolated Python copy and installed libraries — your actual source code lives elsewhere in the project folder and is untouched.

</details>

---

## 1.3 The REPL — Python as a Calculator

**REPL** stands for **R**ead-**E**valuate-**P**rint-**L**oop. It's an interactive Python session where you type one line, it runs immediately, and you see the result — no file needed. It's the fastest way to test a small idea.

### 🔴 LIVE CODE DEMO — Using the REPL

With your venv activated, type just `python` (or `python3`) with no filename, and press Enter. You'll enter the REPL, marked by a `>>>` prompt. Type each of these one at a time:

```python
>>> 2 + 2
>>> "hello" * 3
>>> len("python")
>>> type(42)
```

**What to observe in your terminal:**
- Unlike a script, the REPL **prints the result of every expression automatically** — you never needed a `print()` call above.
- `"hello" * 3` produces `'hellohellohello'` — multiplying a string by a number *repeats* it; this is not arithmetic in the usual sense.
- `type(42)` reports `<class 'int'>` — every value in Python has a type, and `type()` is how you ask what it is.

To leave the REPL: type `exit()` or press `Ctrl+D` (Mac/Linux) / `Ctrl+Z` then Enter (Windows).

### ⚠️ Common Pitfalls
- **Writing multi-line programs directly in the REPL and expecting them to save.** The REPL forgets everything the moment you close it — it's for quick experiments, not real programs. Real programs go in `.py` files (next section).
- **Forgetting you're still inside the REPL** and typing terminal commands like `ls` or `cd` into it — those aren't Python and will error. If your prompt is `>>>`, you're in Python; if it's your normal shell prompt, you're not.

---

## 1.4 Writing and Running a Script

A **script** is a `.py` file containing a full program, run all at once from top to bottom — this is how every real project in this course will work, starting today.

### 🔴 LIVE CODE DEMO — `hello_world.py`

Create a file called `hello_world.py` in your project folder (in VS Code: **File → New File**, save it with that exact name). The full runnable version is at [`code/hello_world.py`](./code/hello_world.py):

```python
# hello_world.py
# This is a comment -- Python ignores everything after a '#' on a line.
# Comments exist purely to explain code to humans reading it later.

print("Hello, MIT Kathmandu!")   # print() displays text in the terminal
print("Today we start Python.")  # each print() call outputs on its own new line
```

Run it from the terminal (make sure your venv is active and you're in the same folder as the file):

```bash
python hello_world.py
```

**What to observe in your terminal:**
- Both lines of text appear, each on its own line, in the exact order they were written — scripts execute top to bottom.
- Nothing about the comments (the `#` lines) appears in the output — comments are invisible to the running program.
- If you see `python: can't open file 'hello_world.py': [Errno 2] No such file or directory`, your terminal isn't in the same folder as the file — use `cd` to navigate there, or `ls` (`dir` on Windows) to confirm what's in your current folder.

### ⚠️ Common Pitfalls
- **Running the wrong file** or running from the wrong folder — always double-check your terminal's current directory matches where the file actually is.
- **Saving the file with the wrong extension** (e.g., `hello_world.txt` or no extension at all) — VS Code sometimes hides extensions by default; confirm the full filename.
- **Expecting VS Code's "Run" button to behave identically to the terminal command** — it usually does, but it may silently use a different Python interpreter than your activated venv. When in doubt, use the terminal directly so you know exactly which environment ran your code.

### ✅ Self-Check
1. You add a third line to `hello_world.py`: `# print("This is a test")`. What happens when you run the file?
2. You run `python hello_world.py` but nothing prints, and no error appears either. What's the most likely explanation?

<details>
<summary><b>Answer</b></summary>

1. **Nothing extra happens.** The line starts with `#`, so it's a comment — Python skips it entirely, whether or not it looks like valid code.
2. Most likely, the `print()` calls exist in a *different* file than the one you ran, or the file you edited and the file you ran are not the same file (e.g., you saved to a new file by accident). Confirm the filename and folder match exactly.

</details>

---

**Next:** [Module 2 — Data Fundamentals & Transformation](./02-data-fundamentals.md)
