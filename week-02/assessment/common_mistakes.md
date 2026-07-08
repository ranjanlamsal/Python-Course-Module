# Week 2 Common Mistakes

Read this if you're stuck, or after you submit to see what others commonly trip on. These are anonymized bugs from past students.

---

## Lists

### 1. Modifying a list while iterating over it

**The Bug:**
```python
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)  # Breaks iteration!
```

**Why it's broken:** Removing items while iterating skips elements and causes unexpected behavior.

**The Fix:**
```python
# Option 1: Iterate over a copy
for n in numbers[:]:
    if n % 2 == 0:
        numbers.remove(n)

# Option 2: Use list comprehension (cleaner)
numbers = [n for n in numbers if n % 2 != 0]
```

---

### 2. Confusing `.sort()` (returns None) with `sorted()` (returns a new list)

**The Bug:**
```python
numbers = [3, 1, 2]
result = numbers.sort()  # result is None!
print(result)  # None
```

**The Fix:**
```python
# If you want the return value:
numbers = [3, 1, 2]
result = sorted(numbers)
print(result)  # [1, 2, 3]

# If you want to modify in place:
numbers.sort()
print(numbers)  # [1, 2, 3]
```

---

### 3. Shallow copy issues with nested lists

**The Bug:**
```python
matrix = [[1, 2], [3, 4]]
copy = matrix[:]
copy[0][0] = 99
print(matrix)  # [[99, 2], [3, 4]] — matrix changed too!
```

**Why it's broken:** `[:]` creates a shallow copy — the outer list is new, but the inner lists are still shared references.

**The Fix:**
```python
import copy
matrix = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(matrix)
deep_copy[0][0] = 99
print(matrix)  # [[1, 2], [3, 4]] — unchanged
```

---

## Dictionaries

### 4. Direct access to missing keys

**The Bug:**
```python
contacts = {"alice": {"phone": "555-1234"}}
name = input("Name: ").lower()  # User types "bob"
print(contacts[name]["phone"])  # KeyError: 'bob'
```

**The Fix:**
```python
contact = contacts.get(name)
if contact:
    print(contact["phone"])
else:
    print("Contact not found")

# Or one-liner:
print(contacts.get(name, {}).get("phone", "Not found"))
```

---

### 5. Case-sensitivity bugs in search

**The Bug:**
```python
contacts = {"alice": {...}, "bob": {...}}
name = input("Name: ")  # User types "Alice" (capital A)
if name in contacts:  # False! "Alice" != "alice"
    print(contacts[name])
```

**The Fix:**
```python
name = input("Name: ").lower()  # Always normalize
if name in contacts:
    print(contacts[name])
```

---

### 6. Forgetting that dicts are unordered (Python < 3.7)

**The Bug:**
Assuming dict order matches insertion order (only guaranteed in Python 3.7+).

**The Fix:**
If order matters, either:
- Rely on Python 3.7+ (order is preserved)
- Or use `sorted(contacts.items())` when iterating

---

### 7. Modifying dict while iterating

**The Bug:**
```python
scores = {"alice": 90, "bob": 75, "charlie": 60}
for name in scores:
    if scores[name] < 70:
        del scores[name]  # RuntimeError!
```

**The Fix:**
```python
# Iterate over a copy of the keys
for name in list(scores.keys()):
    if scores[name] < 70:
        del scores[name]
```

---

## Sets

### 8. Empty set syntax confusion

**The Bug:**
```python
empty = {}  # This is a dict, not a set!
empty.add(1)  # AttributeError: 'dict' object has no attribute 'add'
```

**The Fix:**
```python
empty = set()  # Correct empty set
empty.add(1)
```

---

### 9. Trying to index a set

**The Bug:**
```python
fruits = {"apple", "banana", "cherry"}
print(fruits[0])  # TypeError: 'set' object is not subscriptable
```

**The Fix:**
```python
# Convert to list if you need indexing (but order is arbitrary)
fruits_list = list(fruits)
print(fruits_list[0])
```

---

### 10. Forgetting sets lose order when deduplicating

**The Bug:**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4, 5, 6, 9] — order changed!
```

**The Fix:**
If order matters, use this pattern:
```python
seen = set()
unique = []
for n in numbers:
    if n not in seen:
        seen.add(n)
        unique.append(n)

# Or (Python 3.7+):
unique = list(dict.fromkeys(numbers))
```

---

## Contact Book Project-Specific Mistakes

### 11. Not validating empty inputs

**The Bug:**
```python
name = input("Name: ")  # User just hits Enter
contacts[name.lower()] = {...}  # Creates a contact with key ""
```

**The Fix:**
```python
name = input("Name: ").strip()
if not name:
    print("Name cannot be empty")
    continue
```

---

### 12. Not confirming before destructive actions

**The Bug:**
```python
# Delete immediately without asking
del contacts[name]
```

**The Fix:**
```python
confirm = input(f"Delete {name}? (y/n): ").lower()
if confirm == "y":
    del contacts[name]
    print("Contact deleted")
else:
    print("Cancelled")
```

---

### 13. Not handling duplicate contacts

**The Bug:**
```python
# Just overwrites without warning
contacts[name] = new_contact
```

**The Fix:**
```python
if name in contacts:
    overwrite = input(f"{name} already exists. Overwrite? (y/n): ").lower()
    if overwrite != "y":
        print("Cancelled")
        continue
contacts[name] = new_contact
```

---

### 14. Not splitting tags correctly

**The Bug:**
```python
tags = input("Tags (comma-separated): ")  # User types "work, urgent"
contact["tags"] = tags  # Stores as a single string, not a list
```

**The Fix:**
```python
tags_input = input("Tags (comma-separated): ")
tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
contact["tags"] = tags
```

---

## General Debugging Tips

1. **Print intermediate values** — don't assume, verify:
   ```python
   print(f"DEBUG: name = '{name}'")
   print(f"DEBUG: contacts.keys() = {list(contacts.keys())}")
   ```

2. **Test edge cases:**
   - Empty inputs
   - Missing keys
   - Duplicate entries
   - Invalid menu choices

3. **Read error messages carefully:**
   - `KeyError: 'alice'` → You tried to access a key that doesn't exist. Use `.get()`.
   - `TypeError: 'set' object is not subscriptable` → You tried to index a set. Convert to list first.

4. **Run your code end-to-end before submitting** — test every menu option at least once.

---

**Remember:** Everyone makes these mistakes — the learning happens when you debug them yourself. Use this guide as a reference, but try to fix bugs on your own first before reading the solutions here.
