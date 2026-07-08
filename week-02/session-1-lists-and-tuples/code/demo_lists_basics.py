"""
Demo: List Basics — Creating, Indexing, and Slicing
Run this file to see lists in action.
"""

# Creating different types of lists
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
empty = []

print("=== Creating Lists ===")
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"nested: {nested}")
print(f"empty: {empty}")
print()

# Indexing (accessing single items)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("=== Indexing ===")
print(f"fruits: {fruits}")
print(f"First item (index 0): {fruits[0]}")
print(f"Third item (index 2): {fruits[2]}")
print(f"Last item (index -1): {fruits[-1]}")
print(f"Second from end (index -2): {fruits[-2]}")
print()

# Slicing (accessing ranges)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=== Slicing ===")
print(f"numbers: {numbers}")
print(f"numbers[2:5]: {numbers[2:5]}")      # [2, 3, 4]
print(f"numbers[:3]: {numbers[:3]}")        # [0, 1, 2]
print(f"numbers[7:]: {numbers[7:]}")        # [7, 8, 9]
print(f"numbers[::2]: {numbers[::2]}")      # [0, 2, 4, 6, 8] (every 2nd)
print(f"numbers[::-1]: {numbers[::-1]}")    # [9, 8, 7, ..., 0] (reversed)
print()

# Checking membership
print("=== Membership ===")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
