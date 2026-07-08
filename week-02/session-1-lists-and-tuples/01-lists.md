# Module 1 — Working with Lists

## What is a list?

A **list** is Python's most versatile ordered collection type. It can hold any mix of types (numbers, strings, even other lists), grows and shrinks dynamically, and maintains insertion order.

```python
# Creating lists
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
empty = []
```

Lists are **mutable** — you can change them after creation without making a new list.

---

## Accessing items — indexing and slicing

### Indexing (single item)

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])   # "apple" — first item (0-based)
print(fruits[2])   # "cherry"
print(fruits[-1])  # "date" — last item
print(fruits[-2])  # "cherry" — second from end
```

**Why it matters:** Negative indexing lets you access the end of a list without knowing its length — `fruits[-1]` always gets the last item, even if the list grows.

### Slicing (range of items)

Syntax: `list[start:stop:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] — from index 2 up to (not including) 5
print(numbers[:3])     # [0, 1, 2] — from start up to index 3
print(numbers[7:])     # [7, 8, 9] — from index 7 to end
print(numbers[::2])    # [0, 2, 4, 6, 8] — every 2nd item
print(numbers[::-1])   # [9, 8, 7, ..., 0] — reverse the entire list
```

**⚠️ Common Pitfall:** Slicing never causes an `IndexError` — if you ask for `numbers[100:200]` on a 10-item list, you just get an empty list `[]`. Direct indexing (`numbers[100]`) *will* crash.

---

## Adding and removing items

### Adding items

```python
fruits = ["apple", "banana"]

# Append to the end (most common)
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# Insert at a specific position
fruits.insert(1, "apricot")
print(fruits)  # ["apple", "apricot", "banana", "cherry"]

# Extend with another list (merges in place)
fruits.extend(["date", "elderberry"])
print(fruits)  # ["apple", "apricot", "banana", "cherry", "date", "elderberry"]
```

**Key difference:**
- `append(x)` adds `x` as a single item (even if `x` is a list).
- `extend(iterable)` unpacks the iterable and adds each element individually.

```python
a = [1, 2]
a.append([3, 4])   # a is now [1, 2, [3, 4]] — nested list
b = [1, 2]
b.extend([3, 4])   # b is now [1, 2, 3, 4] — flattened
```

### Removing items

```python
fruits = ["apple", "banana", "cherry", "banana"]

# Remove by value (first occurrence only)
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "banana"]

# Remove by index and return the removed item
last = fruits.pop()      # removes and returns "banana"
first = fruits.pop(0)    # removes and returns "apple"
print(fruits)            # ["cherry"]

# Clear the entire list
fruits.clear()
print(fruits)  # []
```

**⚠️ Common Pitfall:** `.remove(value)` only removes the *first* match. If you have duplicates and want to remove all, use a list comprehension (covered below).

---

## Sorting and reversing

```python
numbers = [5, 2, 9, 1, 7]

# Sort in place (modifies the original list)
numbers.sort()
print(numbers)  # [1, 2, 5, 7, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 7, 5, 2, 1]

# Reverse in place (doesn't sort, just flips order)
numbers.reverse()
print(numbers)  # [1, 2, 5, 7, 9]
```

**Difference between `.sort()` and `sorted()`:**

```python
original = [5, 2, 9, 1]

# Method 1: .sort() — modifies in place, returns None
original.sort()
print(original)  # [1, 2, 5, 9] — list is changed

# Method 2: sorted() — returns a NEW sorted list, original unchanged
original = [5, 2, 9, 1]
new_sorted = sorted(original)
print(original)    # [5, 2, 9, 1] — unchanged
print(new_sorted)  # [1, 2, 5, 9]
```

Use `.sort()` when you want to modify in place (saves memory). Use `sorted()` when you need to keep the original order.

---

## Other useful list operations

```python
fruits = ["apple", "banana", "cherry", "banana"]

# Check if an item exists
print("apple" in fruits)        # True
print("grape" in fruits)        # False

# Count occurrences
print(fruits.count("banana"))   # 2

# Find the index of the first occurrence
print(fruits.index("cherry"))   # 2

# Get the length
print(len(fruits))              # 4
```

---

## List comprehensions — the Pythonic way to transform lists

Instead of writing a multi-line loop to build a new list, you can do it in one line.

### Basic comprehension

```python
# Old way (loop)
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Pythonic way (comprehension)
squares = [n ** 2 for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

### With a condition (filtering)

```python
# Only square the even numbers
evens_squared = [n ** 2 for n in range(1, 11) if n % 2 == 0]
print(evens_squared)  # [4, 16, 36, 64, 100]
```

### With string operations

```python
names = ["alice", "bob", "charlie"]
capitalized = [name.upper() for name in names]
print(capitalized)  # ["ALICE", "BOB", "CHARLIE"]
```

**When to use comprehensions:**
- When the transformation is simple (one expression).
- When you're building a new list from an existing iterable.
- **Avoid** if the logic inside is complex — a regular loop is more readable.

---

## ✅ Self-Check — Lists

Before moving on, answer these *without* running code:

1. What does `fruits[1:4]` return if `fruits = ["a", "b", "c", "d", "e", "f"]`?
2. What's the difference between `append([1, 2])` and `extend([1, 2])`?
3. Write a list comprehension that doubles every number in `[1, 2, 3, 4]`.

<details>
<summary>Answers</summary>

1. `["b", "c", "d"]` — slicing from index 1 up to (not including) 4.
2. `append([1, 2])` adds the entire list as a single nested element. `extend([1, 2])` unpacks it and adds `1` and `2` individually.
3. `doubled = [n * 2 for n in [1, 2, 3, 4]]` → `[2, 4, 6, 8]`

</details>

---

## ⚠️ Common Pitfalls

### 1. Modifying a list while iterating over it

```python
# BAD — removes only every other item
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)  # [1, 3, 5] — works by accident here, but breaks on [2, 4, 6]

# GOOD — iterate over a copy
numbers = [1, 2, 3, 4, 5]
for n in numbers[:]:  # [:] makes a shallow copy
    if n % 2 == 0:
        numbers.remove(n)

# BETTER — use a list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [n for n in numbers if n % 2 != 0]
```

### 2. Confusing `.sort()` (returns None) with `sorted()` (returns a new list)

```python
numbers = [3, 1, 2]
result = numbers.sort()  # result is None, not the sorted list
print(result)            # None

# Correct:
numbers.sort()
print(numbers)  # [1, 2, 3]

# OR use sorted() if you want the return value
result = sorted([3, 1, 2])
print(result)  # [1, 2, 3]
```

### 3. Forgetting that slicing creates a shallow copy (nested lists still reference the same objects)

```python
matrix = [[1, 2], [3, 4]]
copy = matrix[:]  # shallow copy
copy[0][0] = 99
print(matrix)  # [[99, 2], [3, 4]] — the inner lists are still shared!

# For deep copies, use copy.deepcopy()
import copy
matrix = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(matrix)
deep_copy[0][0] = 99
print(matrix)      # [[1, 2], [3, 4]] — unchanged
print(deep_copy)   # [[99, 2], [3, 4]]
```

---

## 🔗 Next

Move on to **[Module 2 — Tuples & Immutability](./02-tuples.md)** to understand when *not* to use a list.
