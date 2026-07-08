# Module 2 — Sets: Unique Collections

## What is a set?

A **set** is an unordered collection of unique items. No duplicates are allowed, and there's no concept of indexing (no `set[0]`).

```python
# Creating sets
numbers = {1, 2, 3, 4, 5}
mixed = {42, "hello", 3.14}

# Empty set (must use set(), not {})
empty = set()  # {} would be an empty dict, not a set
```

**Why sets matter:**
- **Automatic deduplication:** `{1, 2, 2, 3}` becomes `{1, 2, 3}` instantly.
- **Fast membership testing:** `x in my_set` is O(1) — instant, like dicts.
- **Set algebra:** union, intersection, difference — mathematical operations on collections.

---

## Creating sets

```python
# From a literal
fruits = {"apple", "banana", "cherry"}

# From a list (deduplicates automatically)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)  # {1, 2, 3, 4}

# From a string (each character becomes an element)
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'} — no duplicate 'l'
```

---

## Adding and removing items

```python
fruits = {"apple", "banana"}

# Add a single item
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

# Remove an item (raises KeyError if not found)
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry'}

# Remove an item (no error if not found)
fruits.discard("grape")  # Does nothing, no error

# Remove and return an arbitrary item
item = fruits.pop()
print(item)    # Could be 'apple' or 'cherry' (order is undefined)

# Clear all items
fruits.clear()
print(fruits)  # set()
```

---

## Set operations — the real power of sets

Sets support mathematical operations like union, intersection, and difference.

### Union (items in either set)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Method 1: .union()
print(set1.union(set2))  # {1, 2, 3, 4, 5}

# Method 2: | operator (preferred)
print(set1 | set2)       # {1, 2, 3, 4, 5}
```

### Intersection (items in both sets)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Method 1: .intersection()
print(set1.intersection(set2))  # {3}

# Method 2: & operator (preferred)
print(set1 & set2)              # {3}
```

### Difference (items in first set but not second)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Method 1: .difference()
print(set1.difference(set2))  # {1, 2} — in set1, not in set2

# Method 2: - operator (preferred)
print(set1 - set2)            # {1, 2}
```

### Symmetric Difference (items in either set, but not both)

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Method 1: .symmetric_difference()
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}

# Method 2: ^ operator (preferred)
print(set1 ^ set2)                      # {1, 2, 4, 5}
```

**Visual (Venn diagram):**
```
set1 = {1, 2, 3}
set2 = {3, 4, 5}

Union (|):               {1, 2, 3, 4, 5}
Intersection (&):        {3}
Difference (-):          {1, 2}
Symmetric Diff (^):      {1, 2, 4, 5}
```

---

## Common use cases

### 1. Deduplicating a list

```python
emails = ["alice@x.com", "bob@x.com", "alice@x.com", "charlie@x.com"]
unique_emails = list(set(emails))
print(unique_emails)  # ['alice@x.com', 'bob@x.com', 'charlie@x.com']
```

**⚠️ Warning:** This loses the original order. If order matters, use a different approach:

```python
# Preserve order while deduplicating
seen = set()
unique_emails = []
for email in emails:
    if email not in seen:
        seen.add(email)
        unique_emails.append(email)
```

Or use `dict.fromkeys()` (Python 3.7+):

```python
unique_emails = list(dict.fromkeys(emails))
```

### 2. Fast membership testing

```python
allowed_users = {"alice", "bob", "charlie"}  # Set: O(1) lookup

if "alice" in allowed_users:  # Instant, even with millions of users
    print("Access granted")
```

### 3. Finding common elements between collections

```python
last_week_visitors = {"alice", "bob", "charlie"}
this_week_visitors = {"charlie", "dana", "eve"}

# Who visited both weeks?
repeat_visitors = last_week_visitors & this_week_visitors
print(repeat_visitors)  # {'charlie'}

# Who visited only this week (not last week)?
new_visitors = this_week_visitors - last_week_visitors
print(new_visitors)  # {'dana', 'eve'}
```

---

## Sets cannot contain mutable items

```python
# Valid (immutable elements)
valid_set = {1, "hello", (3, 4)}

# Invalid (lists are mutable)
invalid_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'

# Workaround: convert list to tuple
valid_set = {1, 2, (3, 4)}
```

**Rule:** Set elements must be **hashable** (immutable). Same rule as dict keys.

---

## ✅ Self-Check — Sets

Before moving on, answer these *without* running code:

1. What does `{1, 2, 2, 3}` become when you create the set?
2. What's the difference between `.remove()` and `.discard()`?
3. Write an expression to find items in `set1` OR `set2` (union).

<details>
<summary>Answers</summary>

1. `{1, 2, 3}` — duplicates are automatically removed.
2. `.remove(x)` raises `KeyError` if `x` is not in the set. `.discard(x)` does nothing if `x` is missing.
3. `set1 | set2` or `set1.union(set2)`

</details>

---

## ⚠️ Common Pitfalls

### 1. Empty set syntax

```python
# WRONG — this is an empty dict, not a set
not_a_set = {}
print(type(not_a_set))  # <class 'dict'>

# CORRECT — use set()
empty_set = set()
print(type(empty_set))  # <class 'set'>
```

### 2. Sets are unordered (no indexing)

```python
fruits = {"apple", "banana", "cherry"}
print(fruits[0])  # TypeError: 'set' object is not subscriptable

# If you need ordering, convert to a list first
fruits_list = list(fruits)
print(fruits_list[0])  # Works, but order is arbitrary
```

### 3. Forgetting that sets lose duplicates and order

```python
numbers = [3, 1, 2, 1, 3, 2]
unique = set(numbers)
print(unique)  # {1, 2, 3} — duplicates removed, order arbitrary
```

---

## When to use sets vs lists vs dicts

| Use a **list** when... | Use a **set** when... | Use a **dict** when... |
|---|---|---|
| Order matters | Uniqueness matters | You need key-value mapping |
| You need indexing | You need fast membership tests | You need fast lookup by key |
| Duplicates are meaningful | Duplicates should be ignored | You're modeling entities with attributes |
| Example: `[100, -50, 100]` (transactions) | Example: `{"alice", "bob"}` (unique users) | Example: `{"alice": {...}}` (user profiles) |

---

## 🔗 Next

You've completed Week 2's core content! Head to the **[Weekend Assessment](../assessment/README.md)** and build the Contact Book Manager project.
