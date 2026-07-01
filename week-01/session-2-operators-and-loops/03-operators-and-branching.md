# Module 3 — Operators & Branching Logic

## 3.1 Arithmetic Operators

| Operator | Name | Example | Result | Notes |
|---|---|---|---|---|
| `+` | Addition | `5 + 2` | `7` | Also joins (concatenates) strings: `"a" + "b"` → `"ab"` |
| `-` | Subtraction | `5 - 2` | `3` | |
| `*` | Multiplication | `5 * 2` | `10` | Also repeats strings: `"ab" * 3` → `"ababab"` |
| `/` | True division | `5 / 2` | `2.5` | **Always** returns a `float`, even if it divides evenly (`4 / 2` → `2.0`) |
| `//` | Floor division | `5 // 2` | `2` | Divides, then **rounds down** to the nearest whole number |
| `%` | Modulo (remainder) | `5 % 2` | `1` | The **leftover** after floor division |
| `**` | Exponentiation | `5 ** 2` | `25` | "5 to the power of 2" |

### Absolute clarity on `//` and `%`

These two confuse everyone at first because they only make sense *together*. Think of `//` and `%` as answering two halves of the same question: **"If I split this into equal groups, how many full groups do I get, and what's left over?"**

`17 // 5` and `17 % 5` are really one calculation, viewed two ways:

```
17 ÷ 5 = 3 full groups of 5, with 2 left over
         ^^^^^^^^^^^^^^^^^^^       ^^^^^^^^^
         this is 17 // 5 → 3       this is 17 % 5 → 2
```

Check it yourself: `(17 // 5) * 5 + (17 % 5)` always equals `17`, no matter what two numbers you use in place of `17` and `5`. If you ever forget what `%` does, mentally do the `//` first, multiply back, and subtract — that *is* the remainder.

### 🔴 LIVE CODE DEMO — Remainder math

Full file: [`code/demo_arithmetic_operators.py`](./code/demo_arithmetic_operators.py)

```python
# demo_arithmetic_operators.py

total_minutes = 130

hours = total_minutes // 60      # how many FULL hours fit inside 130 minutes?
leftover_minutes = total_minutes % 60   # what's left over after removing those full hours?

print(f"{total_minutes} minutes = {hours} hour(s) and {leftover_minutes} minute(s)")

# A classic use of % : checking if a number is even or odd
number = 17
print(number % 2)   # 1 means odd, 0 would mean even

# Division always returns a float, even when it divides evenly
print(10 / 2)    # 5.0, not 5
print(10 // 2)   # 5, a true integer result
```

**What to observe in your terminal:**
- The first line prints `130 minutes = 2 hour(s) and 10 minute(s)` — `//` gave the whole hours, `%` gave exactly what was left over.
- `10 / 2` prints `5.0` (a float) while `10 // 2` prints `5` (an int) — same numbers, genuinely different result *type*, not just formatting.
- `number % 2` prints `1` — any odd number `% 2` gives `1`; any even number gives `0`. This is the standard even/odd test you'll reuse constantly.

### ⚠️ Common Pitfalls
- **Using `/` when you meant `//`.** `/` always gives a float — if you need a whole-number count (like "how many boxes"), you almost always want `//`, not `/`.
- **Forgetting `%` gives the *remainder*, not a percentage.** The `%` symbol has nothing to do with percentages in Python — it's purely the modulo/remainder operator.
- **Assuming `**` means something else (like XOR or "to the power" written differently).** In Python, `**` is exponentiation; `^` is a *different* operator (bitwise XOR) that does **not** mean "power" — a common bug for people who've seen other languages/calculators.

### ✅ Self-Check
1. Predict the output of `29 // 6` and `29 % 6`, then verify: does `(29 // 6) * 6 + (29 % 6)` equal `29`?
2. A recipe serves 4 people. You're cooking for 22 people. Using `//` and `%`, how would you compute how many full recipes you need, and how many "extra" people's worth is left over?

<details>
<summary><b>Answer</b></summary>

1. `29 // 6` is `4` (4 full groups of 6 = 24), `29 % 6` is `5` (29 − 24 = 5 left over). `4 * 6 + 5 = 29` ✓.
2. `22 // 4` gives `5` full recipes, `22 % 4` gives `2` people's worth still uncovered — meaning you'd actually need to round up to 6 recipes in real life, but the raw `//`/`%` math tells you exactly why.

</details>

---

## 3.2 Comparison and Logical Operators

**Comparison operators** ask a yes/no question about two values and always produce a `bool` (`True`/`False`):

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal to |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |

**Logical operators** combine multiple `True`/`False` values into one:

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | both sides must be `True` | `True and False` | `False` |
| `or` | at least one side must be `True` | `True or False` | `True` |
| `not` | flips a single value | `not True` | `False` |

### 🔴 LIVE CODE DEMO — Comparisons and combining conditions

Full file: [`code/demo_comparison_and_logical.py`](./code/demo_comparison_and_logical.py)

```python
# demo_comparison_and_logical.py

age = 20
has_id_card = True

print(age == 20)              # True -- equality check
print(age != 20)               # False -- "not equal" check
print(age >= 18)               # True

# Combining two conditions -- BOTH must hold
can_enter_venue = (age >= 18) and has_id_card
print(can_enter_venue)         # True

# Combining two conditions -- EITHER is enough
has_student_or_senior_discount = (age < 13) or (age >= 65)
print(has_student_or_senior_discount)   # False, 20 is neither

# 'not' flips a boolean
is_minor = not (age >= 18)
print(is_minor)                # False
```

**What to observe in your terminal:**
- `age == 20` and `age != 20` are exact opposites — the terminal will show `True` then `False` for the same variable.
- `can_enter_venue` is only `True` because *both* halves of the `and` were true — change `has_id_card` to `False` mentally and re-run: the whole expression flips to `False` even though age alone still qualifies.
- `not (age >= 18)` reads naturally as "is age NOT at least 18" — parentheses make the intent easy to read even though they're not always required.

### ⚠️ Common Pitfalls
- **Writing `if age = 18:` instead of `if age == 18:`.** A single `=` is assignment, not comparison — Python will actually refuse to run this exact mistake with a `SyntaxError` inside an `if`, which is a helpful safety net, but the confusion still costs beginners real debugging time.
- **Chaining `and`/`or` without parentheses and losing track of grouping.** When combining three or more conditions, add parentheses even when not strictly required — `(a and b) or c` and `a and (b or c)` can produce different results for the same values.
- **Using `and` where `or` was meant, or vice versa.** "The user must be over 18 **and** under 65" vs "**or**" describes two completely different, easily confused rules — always restate the rule in plain English before writing the operator.

---

## 3.3 If / Elif / Else — Branching Logic

```python
if condition_1:
    # runs only if condition_1 is True
elif condition_2:
    # runs only if condition_1 was False AND condition_2 is True
else:
    # runs only if none of the above were True
```

Critical rule: Python checks conditions **top to bottom** and stops at the **first** one that's `True` — everything after that is skipped, even if it would also technically be true. `elif` and `else` are optional; you can have as many `elif` blocks as you need, but at most one `else`, and it must come last.

### 🔴 LIVE CODE DEMO — Multi-condition classification

Full file: [`code/demo_if_elif_else.py`](./code/demo_if_elif_else.py)

```python
# demo_if_elif_else.py

temperature = 28

if temperature < 0:
    category = "freezing"
elif temperature < 15:
    category = "cold"
elif temperature < 25:
    category = "mild"
elif temperature < 35:
    category = "hot"
else:
    category = "extreme heat"

print(f"{temperature}°C is classified as: {category}")

# Demonstrating "stops at the first True" -- change temperature above and re-run
# to see which single branch fires. Only ONE branch ever runs per pass through
# this block, no matter how many conditions would also technically be true.
```

**What to observe in your terminal:**
- With `temperature = 28`, the output is `28°C is classified as: hot` — Python checked `< 0` (false), `< 15` (false), `< 25` (false), then `< 35` (**true**) and stopped there, never even evaluating the `else`.
- Change `temperature` to `-5`, `10`, `20`, and `40` and re-run each time — exactly one line of output each time, never more than one.
- Reorder the `elif` chain (e.g., put `< 35` before `< 25`) and re-run with `temperature = 20` — notice how the *order* of conditions changes which branch catches a given value. Order matters.

### ⚠️ Common Pitfalls
- **Using separate `if` statements instead of `elif` when the conditions are mutually exclusive.** With standalone `if`s, Python checks *every single one* even after an earlier one matched — this can cause multiple branches to run when you intended only one, or wasted checks that shouldn't happen at all.
- **Writing overlapping conditions in the wrong order.** If `< 35` were checked before `< 15`, a temperature of `-5` would incorrectly be classified as "hot" (since `-5 < 35` is also true) — the first matching condition always wins, so put the most specific/narrow conditions first when ranges overlap.
- **Forgetting the colon `:`** at the end of `if`, `elif`, and `else` lines, or mismatching indentation — Python uses indentation (not `{}`) to know what belongs inside a branch, and inconsistent spacing causes an `IndentationError`.

### ✅ Self-Check
1. Predict the output:
   ```python
   score = 75
   if score >= 90:
       result = "A"
   elif score >= 70:
       result = "B"
   elif score >= 50:
       result = "C"
   else:
       result = "F"
   print(result)
   ```
2. A student writes three separate `if` statements (no `elif`) to classify age into "child", "teen", "adult" using `age < 13`, `age < 20`, `age >= 20`. For `age = 10`, could more than one branch's body run? Why or why not, given how the three conditions are written here?

<details>
<summary><b>Answer</b></summary>

1. `B` — `score >= 90` is false, `score >= 70` is true (75 ≥ 70) and Python stops there.
2. In this specific case, no — the three conditions (`< 13`, `< 20`, `>= 20`) happen to be mutually exclusive by construction, so only one is true for any given age. But this only works because the conditions were carefully written to not overlap; with separate `if`s, Python still checks all three every time (wasteful), and the *moment* any two conditions could both be true for the same value, using separate `if`s instead of `elif` would cause both bodies to run — which is almost never the intended behavior.

</details>

---

**Next:** [Module 4 — Iteration Essentials](./04-iteration-essentials.md)
