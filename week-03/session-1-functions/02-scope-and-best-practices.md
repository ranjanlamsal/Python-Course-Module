# Scope and Best Practices

## The LEGB Rule

When Python looks up a variable, it searches four scopes in order:

1. **L**ocal — inside the current function
2. **E**nclosing — inside any enclosing functions (nested functions)
3. **G**lobal — module-level (outside all functions)
4. **B**uilt-in — Python's built-in names (`len`, `print`, `int`, etc.)

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)  # local
    
    inner()
    print(x)  # enclosing

outer()
print(x)  # global
```

### Variable Shadowing

Inner scopes **shadow** (hide) outer scopes:

```python
name = "Alice"

def greet():
    name = "Bob"  # This is a NEW local variable, doesn't affect global
    print(f"Hello, {name}")

greet()       # Hello, Bob
print(name)   # Alice (unchanged)
```

## The `global` Keyword

To **modify** a global variable inside a function, you must declare it `global`:

```python
counter = 0

def increment():
    global counter  # Without this, Python creates a new local variable
    counter += 1

increment()
increment()
print(counter)  # 2
```

### When NOT to Use `global` (Almost Always)

Using `global` couples your function to module state, making it:
- **Hard to test** (tests must set up global state)
- **Hard to reuse** (can't import function without its global dependencies)
- **Hard to reason about** (function behavior depends on invisible state)

**Better approach — pass state as arguments, return new state:**

```python
# ❌ WRONG: global state
counter = 0
def increment():
    global counter
    counter += 1

# ✅ CORRECT: pure function
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
counter = increment(counter)
print(counter)  # 2
```

## Pure Functions vs Side Effects

### Pure Function
- Same input → same output (no hidden state)
- No side effects (doesn't modify external state, no I/O)
- Easiest to test, reason about, compose

```python
def add(a, b):
    return a + b  # Pure: always returns a + b, no side effects

def format_price(cents):
    return f"${cents / 100:.2f}"  # Pure
```

### Function with Side Effects
- Modifies external state (global var, list passed in, file, database)
- I/O operations (print, file write, network request)
- Harder to test (must verify side effects occurred)

```python
def log_message(message):
    print(message)  # Side effect: prints to console
    with open("log.txt", "a") as f:
        f.write(message + "\n")  # Side effect: modifies file
```

**Both are necessary.** Prefer pure functions when possible; isolate side effects into dedicated functions.

## Mutable vs Immutable Arguments

**Immutable types** (int, float, str, tuple) — changes inside function don't affect caller:

```python
def modify_number(x):
    x += 10
    return x

num = 5
result = modify_number(num)
print(num)     # 5 (unchanged)
print(result)  # 15
```

**Mutable types** (list, dict, set) — changes inside function **do** affect caller:

```python
def add_item(items, item):
    items.append(item)  # Modifies the original list!

my_items = ["apple"]
add_item(my_items, "banana")
print(my_items)  # ["apple", "banana"]
```

**To avoid surprises:**
- Document whether your function mutates its arguments
- Or make a copy if you don't want to mutate:

```python
def add_item(items, item):
    """Return a new list with item added (doesn't mutate original)."""
    return items + [item]  # Creates new list

my_items = ["apple"]
new_items = add_item(my_items, "banana")
print(my_items)   # ["apple"] (unchanged)
print(new_items)  # ["apple", "banana"]
```

## `return` vs `print`

**`print` is for humans.** Functions that print their result can't be composed:

```python
# ❌ Can't use this in another calculation
def add_bad(a, b):
    print(a + b)

add_bad(2, 3)  # Prints 5
result = add_bad(2, 3)  # Prints 5, but result is None!
```

**`return` is for programs.** Functions that return can be tested, chained, reused:

```python
# ✅ Composable, testable
def add_good(a, b):
    return a + b

result = add_good(2, 3)       # result = 5
double = add_good(result, result)  # double = 10
print(add_good(10, 20))       # 30
```

**Guideline:** If a function computes a value, `return` it. If it needs to show something to the user, `print` it (but that's a side effect—keep those functions separate from logic).

## Docstrings

A **docstring** is a string literal that appears as the first statement in a function (or class, module). It documents what the function does.

### Basic Docstring

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32
```

### Google-Style Docstring (Recommended for Complex Functions)

```python
def calculate_discount(price, discount_percent, min_purchase=0):
    """
    Calculate the discounted price.
    
    Args:
        price (float): Original price in dollars.
        discount_percent (float): Discount as a percentage (0-100).
        min_purchase (float, optional): Minimum purchase required. Defaults to 0.
    
    Returns:
        float: Final price after discount, or original price if minimum not met.
    
    Raises:
        ValueError: If discount_percent is negative or > 100.
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    if price < min_purchase:
        return price
    
    return price * (1 - discount_percent / 100)
```

**Why docstrings matter:**
- Your future self will forget what the function does
- Other developers (or AI assistants) need to understand your code
- Tools like `help()` and IDEs show docstrings

```python
help(calculate_discount)  # Shows the docstring
```

## Refactoring Contact Book with Functions

**Before (Week 2 style — no functions):**

```python
contacts = {}

# Add
name = input("Name: ")
contacts[name.lower()] = {"phone": input("Phone: ")}

# Search
search = input("Search: ")
if search.lower() in contacts:
    print(contacts[search.lower()])
```

**After (Week 3 style — with functions):**

```python
def normalize_name(name):
    """Return lowercase version of name for case-insensitive lookup."""
    return name.strip().lower()

def add_contact(contacts, name, phone):
    """Add a contact to the contacts dict."""
    key = normalize_name(name)
    contacts[key] = {"phone": phone}

def search_contact(contacts, name):
    """Return contact details if found, else None."""
    key = normalize_name(name)
    return contacts.get(key)

# Usage:
contacts = {}
add_contact(contacts, "Alice", "555-1234")
result = search_contact(contacts, "ALICE")  # Case-insensitive!
if result:
    print(result)
```

Notice:
- `normalize_name` is reused everywhere (DRY — Don't Repeat Yourself)
- Functions are testable (pass fake data, check return value)
- Pure functions (`normalize_name`, `search_contact`) have no side effects

## Key Takeaways

- **LEGB rule:** Local → Enclosing → Global → Built-in
- **Avoid `global`:** Pass state as arguments, return new state
- **Pure functions:** Same input → same output, no side effects (prefer these)
- **Mutable arguments:** Be careful—changes inside function affect caller
- **`return`, don't `print`:** Functions that return are composable and testable
- **Docstrings:** Document what your function does, especially complex ones

Next: [Session 2 — Lambda, Files, Exceptions](../session-2-lambda-files-exceptions/)
