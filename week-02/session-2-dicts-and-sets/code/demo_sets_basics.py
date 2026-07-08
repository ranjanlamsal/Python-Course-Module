"""
Demo: Set Basics — Creating, Adding, Removing, Deduplication
Run this file to see sets in action.
"""

# Creating sets
print("=== Creating Sets ===")
fruits = {"apple", "banana", "cherry"}
print(f"fruits: {fruits}")

# Automatic deduplication
numbers = {1, 2, 2, 3, 3, 3, 4}
print(f"{{1, 2, 2, 3, 3, 3, 4}} becomes: {numbers}")

# From a list
numbers_list = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers_list)
print(f"set([1, 2, 2, 3, 3, 3, 4]): {unique}")

# Empty set (must use set(), not {})
empty = set()
print(f"empty set: {empty} (type: {type(empty)})")
print()

# Adding and removing
print("=== Adding and Removing ===")
fruits = {"apple", "banana"}
print(f"Starting: {fruits}")

fruits.add("cherry")
print(f"After add('cherry'): {fruits}")

fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

fruits.discard("grape")  # No error if not found
print(f"After discard('grape'): {fruits}")
print()

# Membership testing
print("=== Membership Testing ===")
allowed_users = {"alice", "bob", "charlie"}
print(f"allowed_users: {allowed_users}")
print(f"'alice' in allowed_users: {'alice' in allowed_users}")
print(f"'dana' in allowed_users: {'dana' in allowed_users}")
print()

# Deduplicating a list
print("=== Deduplicating a List ===")
emails = ["alice@x.com", "bob@x.com", "alice@x.com", "charlie@x.com"]
print(f"Original emails: {emails}")
unique_emails = list(set(emails))
print(f"Unique emails: {unique_emails}")
print("Note: Order may change when converting to set and back to list")
