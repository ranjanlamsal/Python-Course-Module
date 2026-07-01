# Module 2 — Data Fundamentals & Transformation

## 2.1 Variables — Labeled Storage Boxes

A **variable** is a name that points to a value stored in memory. Think of it as a **labeled box**: the label is the variable name, the contents are the value, and you can swap out what's inside the box at any time without changing the label.

```python
age = 25        # a box labeled "age" now holds 25
age = 26        # the same box now holds 26 -- the old value is gone
```

Naming rules: variable names can contain letters, digits, and underscores, but can't start with a digit, and are case-sensitive (`age` and `Age` are different boxes). Convention in Python is `snake_case` — lowercase words separated by underscores (e.g., `user_balance`, not `UserBalance` or `userBalance`).

### 🔴 LIVE CODE DEMO — Variables in action

Full file: [`code/demo_variables_and_types.py`](./code/demo_variables_and_types.py)

```python
# demo_variables_and_types.py

# Assign a value to a variable -- this is the box being labeled and filled
favorite_number = 7
print(favorite_number)          # look inside the box

# Reassign it -- same box, new contents
favorite_number = 42
print(favorite_number)

# Two variables can point at completely unrelated values
city = "Kathmandu"
temperature_celsius = 22.5

print(city)
print(temperature_celsius)
```

**What to observe in your terminal:**
- The first `print()` shows `7`, the second shows `42` — reassigning `favorite_number` fully replaced the old value, it didn't add to it.
- `city` and `temperature_celsius` are independent boxes — changing one has zero effect on the other.
- Nothing about the *name* `favorite_number` appears in the output — only the value inside the box does.

### ⚠️ Common Pitfalls
- **Confusing `=` (assignment) with `==` (comparison).** `x = 5` *stores* 5 into `x`. `x == 5` *asks* "does x currently equal 5?" and produces `True`/`False`. Using `=` where you meant `==` is one of the single most common beginner bugs — Python will often let you do it accidentally in certain contexts and fail in a confusing way.
- **Assuming a variable "remembers" its old value somehow.** It doesn't — once reassigned, the previous value is gone unless you saved it into another variable first.

---

## 2.2 The Four Core Types

Every value in Python has a **type** — it determines what operations make sense on it. This week you need four:

| Type | Name | Example | Notes |
|---|---|---|---|
| `int` | Integer | `42`, `-7`, `0` | Whole numbers, no decimal point |
| `float` | Floating-point | `3.14`, `-0.5`, `2.0` | Any number with a decimal point |
| `str` | String | `"hello"`, `'MIT'` | Text, wrapped in quotes (single or double, be consistent) |
| `bool` | Boolean | `True`, `False` | Exactly two possible values — capitalized, no quotes |

You can always check a value's type with the built-in `type()` function — you already saw this in Module 1's REPL demo.

## 2.3 Dynamic Typing

Python is **dynamically typed**: a variable is not permanently locked to one type. The *value* has a type; the *variable name* is just a label that can be re-pointed at any value of any type, at any time.

### 🔴 LIVE CODE DEMO — Watching a variable change type

Full file: [`code/demo_dynamic_typing.py`](./code/demo_dynamic_typing.py)

```python
# demo_dynamic_typing.py

mystery = 10
print(mystery, type(mystery))     # starts life as an int

mystery = "now I'm text"
print(mystery, type(mystery))     # same variable name, completely different type

mystery = True
print(mystery, type(mystery))     # and now a boolean
```

**What to observe in your terminal:**
- Each `print()` shows a different value **and** a different type report (`<class 'int'>`, `<class 'str'>`, `<class 'bool'>`) — same variable name throughout.
- Python never complains about this reassignment across types — this is *legal and normal*, unlike some other languages you may have heard of.
- This flexibility is convenient, but it means Python won't catch a type mistake for you automatically — you have to reason about it yourself (or cast deliberately — next section).

### ⚠️ Common Pitfalls
- **Relying on dynamic typing as an excuse to not think about types at all.** Just because Python *allows* a variable to silently change type doesn't mean doing so on purpose is good practice — it makes code confusing to read. Use it to understand flexibility, not as a design pattern.
- **Assuming `bool` is a "special case" separate from other types.** Under the hood `True` behaves like `1` and `False` like `0` (e.g., `True + True` is `2`) — this occasionally causes very confusing bugs if you're not aware of it.

### ✅ Self-Check
1. Predict the output:
   ```python
   x = 5
   x = "5"
   print(x + x)
   ```
2. What does `type(True)` report?

<details>
<summary><b>Answer</b></summary>

1. `"55"`. By the second line, `x` is a *string* `"5"`, not the integer `5` anymore — `+` on two strings **concatenates** them (joins them end to end) rather than adding numerically.
2. `<class 'bool'>`.

</details>

---

## 2.4 Explicit Type Casting

Sometimes Python has a value in one type but you need it in another — most commonly, `input()` **always** returns a string, even if the user types digits. To do math with it, you must explicitly convert it. This is called **casting**, done with the functions `int()`, `float()`, and `str()`.

```python
age_text = input("Enter your age: ")   # age_text is a str, e.g. "25", no matter what was typed
age_number = int(age_text)             # explicitly cast the string "25" to the integer 25
```

### 🔴 LIVE CODE DEMO — Casting between types (and what happens when it fails)

Full file: [`code/demo_type_casting.py`](./code/demo_type_casting.py)

```python
# demo_type_casting.py

# Casting a numeric string into a real number
raw_input_value = "42"
as_integer = int(raw_input_value)
print(as_integer + 8, type(as_integer))   # now real addition works: 50

# Casting a number into a string (useful for building display text)
price = 3.14
as_text = str(price)
print("The price is " + as_text, type(as_text))

# Casting a float down to an int -- this TRUNCATES, it does not round
print(int(9.99))   # 9, not 10

# What happens when a cast is impossible -- uncomment the next line and run again:
# broken = int("hello")
```

**What to observe in your terminal:**
- `as_integer + 8` prints `50` as a real number, not `"428"` as text — casting genuinely changed the type, not just how it displays.
- `int(9.99)` prints `9` — casting a float to an int **chops off the decimal part**, it does not round to the nearest whole number.
- If you uncomment the last line and run again, Python crashes with `ValueError: invalid literal for int() with base 10: 'hello'` — read this red text carefully: it's telling you exactly which conversion failed and on what value. This is a preview of **exceptions**, which we'll learn to handle gracefully in Week 3 — for now, just get comfortable reading what the error is telling you instead of panicking at red text.

### ⚠️ Common Pitfalls
- **Forgetting that `input()` always returns a string**, then trying to do arithmetic on it directly and either getting a crash (`int` + `str`) or silent string concatenation instead of addition (`str` + `str`).
- **Assuming `int()` rounds.** It doesn't — it truncates (chops toward zero). `int(9.99)` is `9`, and `int(-9.99)` is `-9`, not `-10`.
- **Trying to cast a non-numeric string to a number**, e.g. `int("twenty")` — this always crashes. Casting only works on strings that actually *look like* the target type.

### ✅ Self-Check
1. Predict the output:
   ```python
   value = str(100) + str(1)
   print(value)
   ```
2. A user is asked to enter their year of birth and types `2005`. Without casting anything, what type does that value have the instant `input()` returns it — and what would happen if you immediately tried `2026 - that_value`?

<details>
<summary><b>Answer</b></summary>

1. `"1001"` — both `100` and `1` were cast to strings *before* the `+`, so this is string concatenation (`"100"` joined with `"1"`), not numeric addition (which would have been `101`).
2. It's a `str`, always — regardless of what digits were typed, `input()` never returns a number. `2026 - that_value` would crash with a `TypeError`, because you can't subtract a string from an integer. You'd need `2026 - int(that_value)`.

</details>

---

**Next:** [Session 2 — Operators & Branching Logic](../session-2-operators-and-loops/03-operators-and-branching.md)
