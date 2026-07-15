# Function Anatomy and Arguments

## Why Functions Matter

Your Week 2 Contact Book probably looks like this:

```python
contacts = {}

# Add contact
name = input("Name: ")
contacts[name.lower()] = {"phone": ..., "email": ...}

# Search contact
search = input("Search: ")
if search.lower() in contacts:
    print(contacts[search.lower()])

# Delete contact
delete = input("Delete: ")
if delete.lower() in contacts:
    del contacts[delete.lower()]
```

Notice the pattern? `.lower()` everywhere, `input()` prompts scattered, no way to test logic without running the whole script. **Functions fix this.**

## Basic Function Syntax

```python
def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Hello, Alice!
```

**Anatomy:**
- `def` keyword starts the definition
- `greet` is the function name (lowercase_with_underscores by PEP 8)
- `(name)` is the parameter list
- Docstring (optional but recommended) describes what the function does
- `return` sends a value back to the caller
- If no `return`, function returns `None`

## Positional vs Keyword Arguments

```python
def describe_book(title, author, year):
    return f"{title} by {author} ({year})"

# Positional: order matters
describe_book("1984", "Orwell", 1949)

# Keyword: order doesn't matter
describe_book(author="Orwell", year=1949, title="1984")

# Mix: positional first, then keyword
describe_book("1984", year=1949, author="Orwell")
```

**Rule:** Positional arguments must come before keyword arguments.

## Default Parameters

```python
def greet(name, greeting="Hello"):
    """Greet someone with a customizable greeting."""
    return f"{greeting}, {name}!"

greet("Alice")              # Hello, Alice!
greet("Bob", "Hi")          # Hi, Bob!
greet("Charlie", greeting="Hey")  # Hey, Charlie!
```

**When to use defaults:**
- Optional configuration (logging level, timeout, retry count)
- Sensible fallbacks (default file format, default encoding)

**Common trap — mutable defaults:**

```python
# ❌ WRONG: default list is shared across calls
def add_item(item, items=[]):
    items.append(item)
    return items

add_item("apple")   # ['apple']
add_item("banana")  # ['apple', 'banana'] — SURPRISE!

# ✅ CORRECT: use None as sentinel
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## *args — Arbitrary Positional Arguments

Collects extra positional arguments into a **tuple**.

```python
def sum_all(*numbers):
    """Sum an arbitrary number of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

sum_all(1, 2, 3)        # 6
sum_all(10, 20, 30, 40) # 100
sum_all()               # 0 (empty tuple)
```

**The name `args` is a convention.** You could call it `*values`, `*nums`, etc. The `*` is what matters.

**When to use:**
- Functions like `print()` that accept any number of items
- Wrappers that forward arguments to another function

## **kwargs — Arbitrary Keyword Arguments

Collects extra keyword arguments into a **dictionary**.

```python
def print_info(name, **details):
    """Print a person's name and arbitrary details."""
    print(f"Name: {name}")
    for key, value in details.items():
        print(f"{key}: {value}")

print_info("Alice", age=30, city="NYC", job="Engineer")
# Name: Alice
# age: 30
# city: NYC
# job: Engineer
```

**When to use:**
- Configuration options (many optional params)
- Forwarding options to another function
- Building flexible APIs

## Combining All Argument Types

**Order matters:**
1. Positional arguments
2. `*args`
3. Keyword-only arguments (after `*args`)
4. `**kwargs`

```python
def describe_pet(name, species="dog", *tricks, **extra_info):
    """
    Describe a pet with flexible details.
    
    Args:
        name: Pet's name (required)
        species: Type of animal (default: "dog")
        *tricks: Any number of tricks the pet knows
        **extra_info: Additional details (age, color, etc.)
    """
    print(f"{name} is a {species}")
    
    if tricks:
        print(f"Tricks: {', '.join(tricks)}")
    
    for key, value in extra_info.items():
        print(f"{key}: {value}")

# Example calls:
describe_pet("Buddy")
# Buddy is a dog

describe_pet("Whiskers", "cat", "jump", "hide", age=3, color="orange")
# Whiskers is a cat
# Tricks: jump, hide
# age: 3
# color: orange
```

## Mapping to Project 3 (Cart Engine)

This signature pattern is exactly what you need for `calculate_total()`:

```python
def calculate_total(cart_items, discount_coupon=None, **fees):
    """
    Calculate cart total with optional discount and fees.
    
    Args:
        cart_items: List of (item, price, quantity) tuples
        discount_coupon: Optional discount code (default: None)
        **fees: Additional fees (tax=0.08, shipping=5.99, etc.)
    """
    # Your logic here
    pass
```

Notice:
- `cart_items` is required (positional)
- `discount_coupon` has a default (optional)
- `**fees` accepts arbitrary fees: `tax=0.08, shipping=5.99, handling=2.00`

This is shown on pets/tricks, not carts, so you can't copy-paste it—but the *shape* is identical.

## Key Takeaways

- **Positional arguments:** order matters, required by default
- **Keyword arguments:** order doesn't matter, explicit names
- **Default parameters:** make arguments optional with sensible fallbacks
- **`*args`:** accept any number of positional arguments (tuple)
- **`**kwargs`:** accept any number of keyword arguments (dict)
- **Order:** positional → `*args` → keyword-only → `**kwargs`

Next: [Scope and Best Practices](./02-scope-and-best-practices.md)
