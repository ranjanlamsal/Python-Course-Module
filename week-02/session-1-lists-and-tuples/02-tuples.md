# Module 2 — Tuples & Immutability

## What is a tuple?

A **tuple** is an immutable, ordered collection. Once created, you cannot add, remove, or change its elements. Tuples use parentheses `()` instead of square brackets `[]`.

```python
# Creating tuples
point = (3, 4)
rgb_color = (255, 128, 0)
record = ("Alice", 25, "Engineer")
single_item = (42,)  # Note the trailing comma — required for single-item tuples
empty = ()
```

**Why tuples exist:**
- **Data integrity:** Use when you want to guarantee a collection won't be modified.
- **Performance:** Tuples are slightly faster than lists (less overhead).
- **Dictionary keys:** Tuples can be dict keys; lists cannot (because keys must be immutable).
- **Return multiple values:** Functions commonly return tuples to bundle related data.

---

## Tuples are immutable

```python
point = (3, 4)

# This works (reading)
print(point[0])  # 3

# This crashes (writing)
point[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

You can't append, remove, or modify elements. If you need to change something, convert to a list, modify, and convert back:

```python
point = (3, 4)
point_list = list(point)
point_list[0] = 10
point = tuple(point_list)
print(point)  # (10, 4)
```

But if you're doing this often, you probably should have used a list from the start.

---

## Tuple packing and unpacking

### Packing (creating a tuple without parentheses)

Python automatically creates a tuple when you separate values with commas:

```python
coordinates = 10, 20  # This is a tuple — parentheses are optional
print(type(coordinates))  # <class 'tuple'>
print(coordinates)        # (10, 20)
```

Parentheses are only *required* when clarity matters (e.g., in function calls).

### Unpacking (extracting tuple values into variables)

```python
point = (3, 4)
x, y = point  # Unpack into two variables
print(x)  # 3
print(y)  # 4
```

This works with any iterable (lists, tuples, ranges), but is most commonly used with tuples.

**⚠️ Common Pitfall:** The number of variables must match the tuple length:

```python
point = (3, 4, 5)
x, y = point  # ValueError: too many values to unpack (expected 2)

# Fix: match the count
x, y, z = point
```

### Using `*` to capture the rest

```python
scores = (95, 88, 76, 92, 81)
first, second, *rest = scores
print(first)   # 95
print(second)  # 88
print(rest)    # [76, 92, 81] — note: rest is a LIST, not a tuple
```

---

## Swapping variables (a classic tuple unpacking trick)

```python
a = 10
b = 20

# Old way (requires a temp variable)
temp = a
a = b
b = temp

# Pythonic way (tuple unpacking)
a, b = b, a
print(a, b)  # 20 10
```

This works because the right side creates a tuple `(b, a)` before unpacking into `a, b`.

---

## Tuples vs Lists — when to use which

| Use a **list** when... | Use a **tuple** when... |
|---|---|
| The collection will grow or shrink | The size is fixed |
| You need to sort, append, remove | You need to protect the data from modification |
| Items are all the same type (homogeneous) | Items are different types but related (heterogeneous) |
| Example: `transactions = [100, -50, 200]` | Example: `user_record = ("Alice", 25, "Engineer")` |

**Rule of thumb:** If it feels like a "record" (fixed fields with meaning), use a tuple. If it feels like a "collection" (items you'll add/remove), use a list.

---

## Common tuple operations

Tuples share many list operations, but *without* the mutating methods.

```python
point = (3, 4, 3, 7)

# Length
print(len(point))  # 4

# Indexing and slicing (same as lists)
print(point[0])    # 3
print(point[1:3])  # (4, 3)

# Check membership
print(3 in point)  # True

# Count occurrences
print(point.count(3))  # 2

# Find index of first occurrence
print(point.index(4))  # 1

# Concatenation (creates a NEW tuple)
point2 = point + (8, 9)
print(point2)  # (3, 4, 3, 7, 8, 9)

# Repetition (creates a NEW tuple)
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)
```

**Notice:** No `.append()`, `.remove()`, `.sort()`, or `.reverse()` — those would mutate the tuple.

---

## Tuple unpacking in function returns

Functions that need to return multiple related values often use tuples:

```python
def get_user():
    name = "Alice"
    age = 30
    role = "Engineer"
    return name, age, role  # Returns a tuple

# Unpack the return value
name, age, role = get_user()
print(f"{name} is {age} years old and works as a {role}.")
```

This is cleaner than returning a list or dictionary when the structure is known and fixed.

---

## Tuples as dictionary keys

Because tuples are immutable, they can be used as dict keys (lists cannot).

```python
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
    (35.6762, 139.6503): "Tokyo"
}

nyc_coords = (40.7128, -74.0060)
print(locations[nyc_coords])  # "New York"
```

This is useful when you need a composite key (e.g., coordinates, date+time pairs).

---

## ✅ Self-Check — Tuples

Before moving on, answer these *without* running code:

1. What happens if you try `my_tuple[0] = 10` on `my_tuple = (1, 2, 3)`?
2. What does `a, b = (10, 20)` do?
3. Why can a tuple be a dictionary key but a list cannot?

<details>
<summary>Answers</summary>

1. `TypeError: 'tuple' object does not support item assignment` — tuples are immutable.
2. It unpacks the tuple `(10, 20)` into `a = 10` and `b = 20`.
3. Dictionary keys must be immutable (hashable). Tuples are immutable; lists are mutable and thus can't be hashed.

</details>

---

## ⚠️ Common Pitfalls

### 1. Forgetting the trailing comma in single-item tuples

```python
not_a_tuple = (42)    # This is just the number 42 in parentheses
print(type(not_a_tuple))  # <class 'int'>

is_a_tuple = (42,)    # The comma makes it a tuple
print(type(is_a_tuple))   # <class 'tuple'>
```

### 2. Trying to modify a tuple after creation

```python
scores = (95, 88, 76)
scores[0] = 100  # TypeError — tuples are immutable

# If you need to "modify" it, convert to a list first:
scores = list(scores)
scores[0] = 100
scores = tuple(scores)
```

### 3. Confusing tuple unpacking with multiple assignment

```python
# This is tuple unpacking (right side is a tuple)
x, y = (10, 20)

# This is also tuple unpacking (parentheses implicit)
x, y = 10, 20

# This is NOT unpacking — it's just assignment
x = 10, 20  # x is now the tuple (10, 20)
```

---

## 🔗 Next

You've mastered lists (mutable, dynamic) and tuples (immutable, fixed). Next session we'll cover **dictionaries** (key-value mapping) and **sets** (unique, unordered collections).

Head to **[Session 2 — Dictionaries & Sets](../session-2-dicts-and-sets/README.md)** when you're ready.
