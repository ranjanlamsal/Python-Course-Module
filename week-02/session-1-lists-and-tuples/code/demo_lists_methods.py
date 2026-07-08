"""
Demo: List Methods — Adding, Removing, Sorting
Run this file to see list modification in action.
"""

# Adding items
print("=== Adding Items ===")
fruits = ["apple", "banana"]
print(f"Starting list: {fruits}")

fruits.append("cherry")
print(f"After append('cherry'): {fruits}")

fruits.insert(1, "apricot")
print(f"After insert(1, 'apricot'): {fruits}")

fruits.extend(["date", "elderberry"])
print(f"After extend(['date', 'elderberry']): {fruits}")
print()

# Difference between append and extend
print("=== Append vs Extend ===")
list1 = [1, 2]
list1.append([3, 4])
print(f"After append([3, 4]): {list1}")  # [1, 2, [3, 4]] — nested

list2 = [1, 2]
list2.extend([3, 4])
print(f"After extend([3, 4]): {list2}")  # [1, 2, 3, 4] — flattened
print()

# Removing items
print("=== Removing Items ===")
fruits = ["apple", "banana", "cherry", "banana", "date"]
print(f"Starting list: {fruits}")

fruits.remove("banana")  # Removes first occurrence
print(f"After remove('banana'): {fruits}")

last_item = fruits.pop()  # Remove and return last item
print(f"Popped item: {last_item}")
print(f"After pop(): {fruits}")

first_item = fruits.pop(0)  # Remove and return item at index 0
print(f"Popped item at index 0: {first_item}")
print(f"After pop(0): {fruits}")
print()

# Sorting
print("=== Sorting ===")
numbers = [5, 2, 9, 1, 7, 3]
print(f"Original: {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() creates a new list
original = [5, 2, 9, 1]
new_sorted = sorted(original)
print(f"\nOriginal list: {original}")
print(f"sorted(original): {new_sorted}")
print()

# Other useful methods
print("=== Other Methods ===")
fruits = ["apple", "banana", "cherry", "banana"]
print(f"List: {fruits}")
print(f"count('banana'): {fruits.count('banana')}")
print(f"index('cherry'): {fruits.index('cherry')}")
print(f"len(fruits): {len(fruits)}")
