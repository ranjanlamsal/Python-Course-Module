"""
Demo: Tuple Unpacking — Extracting Values into Variables
Run this file to see unpacking patterns in action.
"""

# Basic unpacking
print("=== Basic Unpacking ===")
point = (3, 4)
x, y = point
print(f"point: {point}")
print(f"x: {x}, y: {y}")
print()

# Unpacking with more values
print("=== Unpacking Multiple Values ===")
record = ("Alice", 30, "Engineer")
name, age, role = record
print(f"record: {record}")
print(f"name: {name}, age: {age}, role: {role}")
print()

# Swapping variables (tuple unpacking trick)
print("=== Swapping Variables ===")
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")

a, b = b, a  # The Pythonic way!
print(f"After swap:  a = {a}, b = {b}")
print()

# Using * to capture the rest
print("=== Capturing Rest with * ===")
scores = (95, 88, 76, 92, 81)
first, second, *rest = scores
print(f"scores: {scores}")
print(f"first: {first}")
print(f"second: {second}")
print(f"rest: {rest} (note: this is a list, not a tuple)")
print()

# Ignoring values with _
print("=== Ignoring Values ===")
person = ("Bob", 25, "Engineer", "New York")
name, _, role, _ = person  # We don't care about age or city
print(f"person: {person}")
print(f"We only care about: name = {name}, role = {role}")
print()

# Unpacking in function returns
print("=== Function Return Unpacking ===")

def get_stats():
    """Return min, max, and average of a dataset."""
    data = [10, 20, 30, 40, 50]
    return min(data), max(data), sum(data) / len(data)

min_val, max_val, avg_val = get_stats()
print(f"Stats: min = {min_val}, max = {max_val}, avg = {avg_val}")
print()

# Common mistake: mismatched unpacking
print("=== Mismatch Error Example ===")
point = (3, 4, 5)
try:
    x, y = point  # Only 2 variables, but tuple has 3 items
except ValueError as e:
    print(f"Trying to unpack {point} into x, y → ValueError: {e}")

# Fix: match the count
x, y, z = point
print(f"Correct unpacking: x = {x}, y = {y}, z = {z}")
