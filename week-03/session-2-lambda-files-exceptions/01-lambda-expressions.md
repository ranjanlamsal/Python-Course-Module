# Lambda Expressions

## What Is a Lambda?

A **lambda** is an anonymous (unnamed) function defined in a single expression. It's Python's way of creating small, throwaway functions inline.

**Regular function:**
```python
def add(a, b):
    return a + b
```

**Lambda equivalent:**
```python
add = lambda a, b: a + b
```

## Syntax

```python
lambda arguments: expression
```

- `lambda` keyword
- Arguments (same as function parameters, comma-separated)
- Colon `:`
- **Single expression** (not a statement)
- No `return` keyword (the expression result is automatically returned)

## When to Use Lambda

✅ **Good use cases:**
- Inline transformations with `sorted()`, `filter()`, `map()`
- Short, simple functions passed as arguments
- One-off functions you won't reuse

❌ **When NOT to use lambda:**
- Complex logic (more than one expression)
- Multiple statements (lambda can't have statements)
- Functions you'll reuse multiple times (use `def` and give it a name)
- Readability matters more than brevity

**Guideline:** If you need to think for more than 5 seconds to understand the lambda, use a named function instead.

## Lambda with `sorted()`

Sort by a custom key using `key=` parameter.

### Example 1: Sort by Second Element

```python
# List of (word, length) tuples
word_pairs = [("apple", 5), ("banana", 6), ("cherry", 6), ("date", 4)]

# Sort by length (second element of tuple)
sorted_pairs = sorted(word_pairs, key=lambda pair: pair[1])
print(sorted_pairs)
# [('date', 4), ('apple', 5), ('banana', 6), ('cherry', 6)]
```

**Without lambda (named function):**
```python
def get_length(pair):
    return pair[1]

sorted_pairs = sorted(word_pairs, key=get_length)
```

### Example 2: Sort by Absolute Value

```python
numbers = [-5, 2, -3, 8, -1]
sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print(sorted_numbers)  # [-1, 2, -3, -5, 8]
```

### Example 3: Sort Dictionaries by Value

```python
prices = {"apple": 1.50, "banana": 0.75, "cherry": 2.00}
sorted_items = sorted(prices.items(), key=lambda item: item[1])
print(sorted_items)
# [('banana', 0.75), ('apple', 1.5), ('cherry', 2.0)]
```

## Lambda with `filter()`

Filter an iterable based on a condition (predicate).

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

**Without lambda:**
```python
def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, numbers))
```

**List comprehension equivalent (often clearer):**
```python
evens = [n for n in numbers if n % 2 == 0]
```

## Lambda with `map()`

Apply a function to every item in an iterable.

```python
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda n: n ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

**List comprehension equivalent (often clearer):**
```python
squared = [n ** 2 for n in numbers]
```

## Mapping to Project 3 (Cart Engine)

In the Cart Engine, you might need to filter or scale prices based on discount rules:

```python
# Example: Apply 10% discount to items over $50
cart_items = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
]

# Filter items eligible for discount
expensive = filter(lambda item: item["price"] > 50, cart_items)

# Scale prices with discount
discounted = map(lambda item: {**item, "price": item["price"] * 0.9}, expensive)
```

This is shown on word pairs and numbers, not carts—but the *pattern* is identical.

## Lambda Limitations

### Can't Use Statements

```python
# ❌ WRONG: lambda can't have statements
lambda x: print(x)  # SyntaxError

# ❌ WRONG: lambda can't have multiple statements
lambda x: x += 1; return x  # SyntaxError
```

### Can't Have Multiple Expressions

```python
# ❌ WRONG: lambda is single expression only
lambda x: (
    result = x * 2  # SyntaxError
    return result
)

# ✅ CORRECT: use a named function
def double(x):
    result = x * 2
    return result
```

## When Lambda Hurts Readability

```python
# ❌ Hard to understand at a glance
sorted_users = sorted(users, key=lambda u: (u["last_name"].lower(), u["first_name"].lower(), -u["age"]))

# ✅ Much clearer with a named function
def sort_key(user):
    """Sort by last name, then first name, then age (descending)."""
    return (user["last_name"].lower(), user["first_name"].lower(), -user["age"])

sorted_users = sorted(users, key=sort_key)
```

## Key Takeaways

- **Syntax:** `lambda args: expression`
- **Use case:** Inline, simple transformations (especially with `sorted()`, `filter()`, `map()`)
- **Single expression only:** No statements, no multiple lines
- **Readability matters:** If the lambda is complex, use a named function
- **List comprehensions:** Often clearer than `filter()` or `map()` with lambda

Next: [File I/O](./02-file-io.md)
