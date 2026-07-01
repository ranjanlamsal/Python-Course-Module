# `assignment_week1` — Week 1 Weekend Workbook

**Window:** Saturday → Wednesday. **Grading:** none — this is entirely ungraded.
**The only consequence of this workbook is Thursday's first 30 minutes**, which will be a live, instructor-led architecture review built directly from real (anonymized) student attempts at Section 2's project. If you don't do the work, you'll have nothing to recognize or contribute to that discussion — the review assumes you've struggled with this material firsthand.

## How to budget your weekend (suggested, not enforced)

This is intentionally more than "quick homework." Respect your own time — the breakdown below is a guide so nothing quietly eats your whole weekend:

| Section | Status | Suggested timing | Rough effort |
|---|---|---|---|
| 1 — Core Coding Practices | **Mandatory** | Saturday | ~1–1.5 hrs total |
| 2 — Smart ATM Simulator (the project) | **Mandatory** | Saturday evening → Tuesday | ~3–5 hrs total |
| 3 — Multiplier Challenges | **Optional** | Only if 1 & 2 are solid with time left | Open-ended |
| 4 — Reflection Log | **Mandatory, but short** | Wednesday, right after you stop coding | ~10 minutes |

If you only have time for one thing this weekend, it's **Section 2**. Everything else supports it.

---

## Section 1 — Core Coding Practices (Syntax & Logic)

**Mandatory.** No code solutions are provided anywhere in this section, or anywhere in this repo's assessment folder — that's intentional. Struggling honestly with these for a few minutes before it clicks is the point.

Each exercise has a matching stub file in [`exercises/`](./exercises/) with the problem restated as comments and a `# TODO:` marker — write your solution directly into that file and run it from the terminal as you go.

### Exercise 1 — Bakery Box Packer
**Concept: `input()`, type casting, `%` / `//`.**

A bakery needs to pack cookies into boxes. Ask the user for the total number of cookies baked, and the number of cookies that fit in one box. Using `//` and `%`, compute and print how many **full boxes** can be packed, and how many cookies are **left over**, unboxed.

- **Expected interaction:**
  ```
  How many cookies did you bake? 50
  How many cookies fit in one box? 6
  You can pack 8 full box(es), with 2 cookie(s) left over.
  ```
- **Absolute Beginner Tip:** `input()` gives you text, not a number — cast both values with `int()` *before* you try `//` or `%` on them, or Python will crash immediately.

### Exercise 2 — Amusement Park Ride Eligibility Checker
**Concept: complex branching with `and` / `or` / `not`.**

A ride has these rules: a rider must be **at least 12 years old**, OR be **accompanied by an adult** (age 18+) if they're younger. Separately, regardless of age, anyone **under 100cm tall is never allowed on**, no exceptions. Ask for the rider's age, height in cm, and whether an accompanying adult is present (`yes`/`no`), and print whether they can ride.

- **Expected interaction (example 1):**
  ```
  Rider age: 9
  Rider height (cm): 120
  Accompanied by an adult? (yes/no): yes
  Result: Allowed to ride.
  ```
- **Expected interaction (example 2):**
  ```
  Rider age: 9
  Rider height (cm): 95
  Accompanied by an adult? (yes/no): yes
  Result: Not allowed to ride.
  ```
- **Absolute Beginner Tip:** Notice the height rule is completely separate from the age/adult rule, and it overrides everything else — think about which condition needs to be checked *first*, independent of the others, before you start combining `and`/`or`.

### Exercise 3 — Weekly Expense Tracker (Lite)
**Concept: basic loop execution and running totals.**

Using a loop that runs **exactly 7 times** (one for each day of the week), ask the user to enter how much they spent that day. Keep a running total as you go, and after the loop finishes, print the total spent for the week and the average daily spend.

- **Expected interaction (abbreviated):**
  ```
  Day 1 spending: 500
  Day 2 spending: 200
  ...
  Day 7 spending: 100
  Total spent this week: 1850
  Average daily spend: 264.29
  ```
- **Absolute Beginner Tip:** The running total variable must be created and set to `0` *before* the loop starts, not inside it — otherwise it gets reset back to zero on every single iteration.

### Exercise 4 — Number Classifier (Bridge Exercise)
**Concept: loops + conditionals combined — this is the closest exercise to the ATM project's actual structure.**

Write a program that repeatedly asks the user to enter a number. For each number entered, classify and print **both**: whether it's positive, negative, or zero, **and** whether it's even or odd. Keep asking for more numbers forever — **until the user enters the sentinel value `0`, which should stop the loop without being classified.**

- **Expected interaction (abbreviated):**
  ```
  Enter a number (0 to quit): 7
  7 is positive and odd.
  Enter a number (0 to quit): -4
  -4 is negative and even.
  Enter a number (0 to quit): 0
  Goodbye!
  ```
- **Absolute Beginner Tip:** This is a `while True:` loop with a `break` condition checked first, then multiple independent `if` classifications applied to whatever number survives past that check — that combination (infinite loop + break-on-sentinel + several branching rules per pass) is *exactly* the skeleton the ATM Simulator below is built from. If you get this exercise working cleanly, the ATM's structure will feel familiar rather than new.

---

## Section 2 — Week 1 Core Project: "The Smart ATM Simulator"

**Mandatory. This is the project Thursday's review is built from.**

Full specification: **[`project/PROJECT_SPEC.md`](./project/PROJECT_SPEC.md)**
Starter file (structure + `# TODO:` markers, no solution code): **[`project/atm_simulator_starter.py`](./project/atm_simulator_starter.py)**

Read the spec fully before opening the starter file.

---

## Section 3 — Optional Weekend Multiplier Challenges

**Optional.** Only attempt these once Sections 1 and 2 feel solid, and only if you have time and energy left — these exist to push students who are ready for more, not to add pressure. Skipping them has no bearing on Thursday's review.

Stub files: [`challenges/challenge_1_collatz_race.py`](./challenges/challenge_1_collatz_race.py) and [`challenges/challenge_2_password_strength_auditor.py`](./challenges/challenge_2_password_strength_auditor.py).

### Challenge 1 — The Collatz Race
Take any positive integer entered by the user. Repeatedly apply this rule until the number reaches `1`: if the number is even, divide it by 2; if it's odd, multiply it by 3 and add 1. Count and print how many steps it took to reach `1`. (This sequence is famous precisely because nobody knows a simple reason it always *does* reach 1 — you're not proving that, just simulating it.)

### Challenge 2 — Password Strength Auditor
Ask the user to enter a password as text. Without using any library beyond what you already know plus basic string methods you can look up (`.isdigit()`, `.isupper()`, `.islower()` are worth researching for this one), loop through every character and count how many are digits, how many are uppercase letters, and how many are "other" (symbols/spaces). Use that breakdown plus the password's total length to print a strength rating of `"Weak"`, `"Moderate"`, or `"Strong"` using rules you design yourself.

---

## Section 4 — Pre-Class Reflection Log (bring this Thursday)

**Mandatory — but it's writing, not code, and takes about 10 minutes.**

This is the raw material for Thursday's review. Students who skip it will have nothing concrete to bring to the discussion — vague memories of "it was hard" don't translate into a useful architecture conversation, but "my balance went negative because I checked the withdrawal amount before casting it to a float" absolutely does.

Fill in **[`reflection_log.md`](./reflection_log.md)** honestly, right after you finish building (or right after you stop for the week, even if unfinished) — not from memory days later.
