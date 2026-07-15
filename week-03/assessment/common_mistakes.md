# Common Mistakes — Week 3

These are anonymized bugs from previous cohorts. Read this *before* starting your projects.

## Functions

### Missing `key=` in `sorted()`/`filter()`

```python
# ❌ WRONG: lambda is passed as first argument, not as key
sorted_items = sorted(lambda item: item[1], cart_items)

# ✅ CORRECT: use key= parameter
sorted_items = sorted(cart_items, key=lambda item: item[1])
```

### Mutating Original List/Dict

```python
# ❌ WRONG: mutates the original cart_items
def apply_discount(cart_items, discount):
    for item in cart_items:
        item["price"] *= (1 - discount)  # Modifies original!
    return cart_items

# ✅ CORRECT: work on a copy
def apply_discount(cart_items, discount):
    discounted = []
    for item in cart_items:
        new_item = item.copy()  # Shallow copy
        new_item["price"] *= (1 - discount)
        discounted.append(new_item)
    return discounted
```

### Not Returning from Functions

```python
# ❌ WRONG: prints instead of returns
def calculate_total(cart_items):
    total = sum(item["price"] for item in cart_items)
    print(total)  # Can't use this result in other calculations

# ✅ CORRECT: return the value
def calculate_total(cart_items):
    return sum(item["price"] for item in cart_items)
```

### Scope Confusion

```python
# ❌ WRONG: trying to access local variable outside function
def calculate():
    result = 42

calculate()
print(result)  # NameError: result is not defined

# ✅ CORRECT: return the value
def calculate():
    return 42

result = calculate()
print(result)
```

## Lambda

### Wrong Lambda Syntax (Statements Instead of Expressions)

```python
# ❌ WRONG: lambda can't have statements
filter(lambda x: print(x), numbers)  # SyntaxError

# ❌ WRONG: lambda can't have assignments
map(lambda x: y = x * 2; y, numbers)  # SyntaxError

# ✅ CORRECT: single expression only
map(lambda x: x * 2, numbers)
```

### Overusing Lambda (Hurts Readability)

```python
# ❌ WRONG: too complex for lambda
sorted_users = sorted(users, key=lambda u: (u["last"].lower(), u["first"].lower(), -u["age"]))

# ✅ CORRECT: use named function for clarity
def sort_key(user):
    return (user["last"].lower(), user["first"].lower(), -user["age"])

sorted_users = sorted(users, key=sort_key)
```

## File I/O

### Forgetting `with` Statement

```python
# ❌ WRONG: manual close is fragile
f = open("data.txt", "r")
content = f.read()
f.close()  # If exception occurs before this, file stays open

# ✅ CORRECT: with ensures file closes
with open("data.txt", "r") as f:
    content = f.read()
```

### Overwriting When You Meant to Append

```python
# ❌ WRONG: mode 'w' erases file every time
with open("log.txt", "w") as f:
    f.write("New entry\n")  # Previous entries are gone!

# ✅ CORRECT: mode 'a' appends
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

### Not Handling FileNotFoundError

```python
# ❌ WRONG: crashes if file missing
with open("data.txt", "r") as f:
    content = f.read()

# ✅ CORRECT: handle exception
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
    content = ""
```

### Reading Entire Large File Into Memory

```python
# ❌ WRONG: reads entire log into memory (could be GBs!)
with open("server.log", "r") as f:
    lines = f.readlines()  # Memory spike!
    for line in lines:
        process(line)

# ✅ CORRECT: iterate line-by-line
with open("server.log", "r") as f:
    for line in f:  # Streams one line at a time
        process(line)
```

## Exceptions

### Bare `except:` Catches Everything

```python
# ❌ WRONG: catches KeyboardInterrupt, SystemExit, etc.
try:
    process_file()
except:
    print("Something went wrong")  # Can't Ctrl+C to stop!

# ✅ CORRECT: catch specific exceptions
try:
    process_file()
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {e}")
```

### Swallowing Exceptions Without Logging

```python
# ❌ WRONG: exception is silently ignored
try:
    parse_log_line(line)
except ValueError:
    pass  # What went wrong? Which line?

# ✅ CORRECT: at least log what happened
try:
    parse_log_line(line)
except ValueError:
    print(f"Skipping malformed line: {line.strip()}")
```

### Not Handling Specific Exceptions

```python
# ❌ WRONG: catches everything as generic Exception
try:
    age = int(input("Age: "))
    result = 100 / age
except Exception as e:
    print("Error")  # Was it ValueError or ZeroDivisionError?

# ✅ CORRECT: handle each differently
try:
    age = int(input("Age: "))
    result = 100 / age
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Age cannot be zero")
```

## Project-Specific: Cart Engine

### Miscounting with Lambda

```python
# ❌ WRONG: filter returns iterator, len() doesn't work
eligible = filter(lambda item: item["price"] > 50, cart_items)
count = len(eligible)  # TypeError: object of type 'filter' has no len()

# ✅ CORRECT: convert to list first
eligible = list(filter(lambda item: item["price"] > 50, cart_items))
count = len(eligible)
```

### Wrong **kwargs Access

```python
# ❌ WRONG: tries to access as attribute
def calculate_total(cart_items, **fees):
    tax = fees.tax  # AttributeError: 'dict' object has no attribute 'tax'

# ✅ CORRECT: access as dict key
def calculate_total(cart_items, **fees):
    tax = fees.get("tax", 0)  # Default to 0 if not provided
```

## Project-Specific: Log Analyzer

### Wrong String Split

```python
# ❌ WRONG: splits on space, breaks if message has spaces
parts = line.split(" ")
timestamp, level, message = parts  # ValueError: too many values to unpack

# ✅ CORRECT: split on delimiter with limit
parts = line.split(" | ")  # Or whatever delimiter your format uses
```

### Miscounting Log Levels

```python
# ❌ WRONG: forgets to initialize counter for new levels
counts = {}
for line in lines:
    level = parse_level(line)
    counts[level] += 1  # KeyError: 'ERROR' not in dict yet

# ✅ CORRECT: use .get() or initialize
counts = {}
for line in lines:
    level = parse_level(line)
    counts[level] = counts.get(level, 0) + 1

# ✅ ALTERNATIVE: use defaultdict
from collections import defaultdict
counts = defaultdict(int)
for line in lines:
    level = parse_level(line)
    counts[level] += 1
```

### Not Stripping Whitespace

```python
# ❌ WRONG: \n at end of line breaks comparison
if line == "ERROR: Database connection failed":  # Never matches!

# ✅ CORRECT: strip whitespace first
if line.strip() == "ERROR: Database connection failed":
```

## General

### Hardcoding Test Data in Functions

```python
# ❌ WRONG: function only works with hardcoded data
def test_cart():
    cart = [{"name": "Apple", "price": 1.50}]  # Hardcoded
    total = calculate_total(cart)
    print(total)

# ✅ CORRECT: pass data as argument
def test_cart(cart_items):
    total = calculate_total(cart_items)
    print(total)
```

### Not Testing Edge Cases

Test these before submitting:
- Empty inputs (empty cart, empty file)
- Missing files (FileNotFoundError)
- Malformed data (bad numbers, wrong format)
- Negative numbers (prices, quantities)
- Large inputs (1000+ items)

## How to Avoid These

1. **Read the handbooks carefully** — every mistake listed here is covered
2. **Run demo code** — modify it, break it, fix it
3. **Test incrementally** — don't write 100 lines then test
4. **Use print statements** — see what your variables contain
5. **Read error messages** — they tell you exactly what went wrong
