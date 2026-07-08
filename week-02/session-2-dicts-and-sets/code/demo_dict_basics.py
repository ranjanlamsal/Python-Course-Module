"""
Demo: Dictionary Basics — Creating, Accessing, Modifying
Run this file to see dictionaries in action.
"""

# Creating dictionaries
print("=== Creating Dictionaries ===")
person = {
    "name": "Alice",
    "age": 30,
    "role": "Engineer"
}
print(f"person: {person}")

empty = {}
print(f"empty: {empty} (type: {type(empty)})")
print()

# Accessing values
print("=== Accessing Values ===")
print(f"person['name']: {person['name']}")
print(f"person['age']: {person['age']}")
print()

# Safe access with .get()
print("=== Safe Access with .get() ===")
print(f"person.get('name'): {person.get('name')}")
print(f"person.get('city'): {person.get('city')}")  # None, no crash
print(f"person.get('city', 'NYC'): {person.get('city', 'NYC')}")  # Default value
print()

# Direct access error demonstration
print("=== Direct Access Error ===")
try:
    print(person["city"])
except KeyError as e:
    print(f"KeyError when accessing missing key: {e}")
print()

# Adding and updating
print("=== Adding and Updating ===")
person["city"] = "Boston"
print(f"After adding 'city': {person}")

person["age"] = 31
print(f"After updating 'age': {person}")
print()

# Checking membership
print("=== Checking Membership ===")
print(f"'name' in person: {'name' in person}")
print(f"'salary' in person: {'salary' in person}")
