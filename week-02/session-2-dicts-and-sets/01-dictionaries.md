# Module 1 — Dictionaries: Key-Value Mapping

## What is a dictionary?

A **dictionary** (or `dict`) stores data as **key-value pairs**. Instead of accessing items by numeric index (like lists), you access them by a unique key.

```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "role": "Engineer"
}

# Empty dict
empty = {}
```

**Why dictionaries matter:**
- **Fast lookup:** Finding a value by key is O(1) — instant, regardless of dict size.
- **Meaningful keys:** `person["age"]` is clearer than `person_list[1]`.
- **Real-world modeling:** Contacts, configurations, JSON APIs all use key-value structures.

---

## Accessing values

### Direct access (raises KeyError if key doesn't exist)

```python
person = {"name": "Alice", "age": 30}

print(person["name"])  # "Alice"
print(person["city"])  # KeyError: 'city' — crashes!
```

### Safe access with `.get()` (returns None or a default if key doesn't exist)

```python
person = {"name": "Alice", "age": 30}

print(person.get("name"))        # "Alice"
print(person.get("city"))        # None — no crash
print(person.get("city", "NYC")) # "NYC" — custom default
```

**⚠️ Always use `.get()` when you're not sure a key exists** — prevents crashes.

---

## Adding and updating values

```python
person = {"name": "Alice"}

# Add a new key
person["age"] = 30
print(person)  # {"name": "Alice", "age": 30}

# Update an existing key
person["age"] = 31
print(person)  # {"name": "Alice", "age": 31}
```

There's no separate "add" vs "update" operation — assignment does both.

---

## Removing items

```python
person = {"name": "Alice", "age": 30, "role": "Engineer"}

# Remove by key (raises KeyError if missing)
del person["age"]
print(person)  # {"name": "Alice", "role": "Engineer"}

# Remove by key and return the value
role = person.pop("role")
print(role)    # "Engineer"
print(person)  # {"name": "Alice"}

# Clear all items
person.clear()
print(person)  # {}
```

---

## Iterating over dictionaries

### Iterate over keys (default)

```python
person = {"name": "Alice", "age": 30, "role": "Engineer"}

for key in person:
    print(key)  # name, age, role (order preserved in Python 3.7+)
```

### Iterate over values

```python
for value in person.values():
    print(value)  # Alice, 30, Engineer
```

### Iterate over key-value pairs (most common)

```python
for key, value in person.items():
    print(f"{key}: {value}")
# name: Alice
# age: 30
# role: Engineer
```

**Best practice:** Use `.items()` when you need both the key and value.

---

## Nested dictionaries

Dictionaries can contain other dictionaries:

```python
contacts = {
    "alice": {
        "phone": "555-1234",
        "email": "alice@example.com"
    },
    "bob": {
        "phone": "555-5678",
        "email": "bob@example.com"
    }
}

# Access nested values
print(contacts["alice"]["phone"])  # "555-1234"

# Safely access nested values
print(contacts.get("charlie", {}).get("phone", "Not found"))  # "Not found"
```

This pattern is common in real-world apps (user profiles, API responses, config files).

---

## Common dictionary methods

```python
person = {"name": "Alice", "age": 30}

# Check if a key exists
print("name" in person)   # True
print("city" in person)   # False

# Get all keys as a list
print(list(person.keys()))    # ["name", "age"]

# Get all values as a list
print(list(person.values()))  # ["Alice", 30]

# Get number of key-value pairs
print(len(person))  # 2

# Copy a dictionary (shallow copy)
person_copy = person.copy()
```

---

## Dictionary keys must be immutable

```python
# Valid keys (immutable types)
valid = {
    "name": "Alice",      # str
    42: "answer",         # int
    (3, 4): "point",      # tuple
}

# Invalid keys (mutable types)
invalid = {
    [1, 2]: "list"  # TypeError: unhashable type: 'list'
}
```

**Rule:** Keys must be **hashable** (immutable). Lists and dicts cannot be keys; tuples can.

---

## ✅ Self-Check — Dictionaries

Before moving on, answer these *without* running code:

1. What's the difference between `dict["key"]` and `dict.get("key")`?
2. Write a loop that prints each key-value pair in `person = {"name": "Bob", "age": 25}`.
3. Why can `(3, 4)` be a dict key but `[3, 4]` cannot?

<details>
<summary>Answers</summary>

1. `dict["key"]` raises `KeyError` if the key doesn't exist. `dict.get("key")` returns `None` (or a default) instead of crashing.
2. 
```python
for key, value in person.items():
    print(f"{key}: {value}")
```
3. Tuples are immutable (hashable), so they can be keys. Lists are mutable (not hashable), so they can't.

</details>

---

## ⚠️ Common Pitfalls

### 1. Forgetting that dict keys are case-sensitive

```python
person = {"Name": "Alice"}
print(person["name"])  # KeyError — "Name" != "name"

# Fix: normalize keys (e.g., always lowercase)
person = {"name": "Alice"}
lookup_key = "NAME".lower()
print(person[lookup_key])  # Works
```

### 2. Modifying a dict while iterating over it

```python
# BAD — can cause RuntimeError
scores = {"alice": 90, "bob": 75, "charlie": 60}
for name in scores:
    if scores[name] < 70:
        del scores[name]  # RuntimeError: dictionary changed size during iteration

# GOOD — iterate over a copy of the keys
for name in list(scores.keys()):
    if scores[name] < 70:
        del scores[name]
```

### 3. Using `.get()` incorrectly with nested dicts

```python
contacts = {"alice": {"phone": "555-1234"}}

# BAD — crashes if "bob" doesn't exist
phone = contacts["bob"]["phone"]  # KeyError: 'bob'

# GOOD — safe nested access
phone = contacts.get("bob", {}).get("phone", "Not found")
```

---

## 🔗 Next

You've mastered dictionaries. Now learn about **sets** — collections that guarantee uniqueness and support set algebra.

Move on to **[Module 2 — Sets](./02-sets.md)**.
