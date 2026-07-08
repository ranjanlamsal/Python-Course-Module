"""
Demo: Tuples — Immutable Ordered Collections
Run this file to see tuple basics and immutability in action.
"""

# Creating tuples
print("=== Creating Tuples ===")
point = (3, 4)
rgb_color = (255, 128, 0)
record = ("Alice", 25, "Engineer")
single_item = (42,)  # Note the trailing comma
empty = ()

print(f"point: {point}")
print(f"rgb_color: {rgb_color}")
print(f"record: {record}")
print(f"single_item: {single_item} (type: {type(single_item)})")
print(f"empty: {empty}")
print()

# Common mistake: forgetting the comma
not_a_tuple = (42)
print(f"not_a_tuple = (42) → type: {type(not_a_tuple)}")  # int, not tuple!
print()

# Tuple packing (implicit tuple creation)
print("=== Tuple Packing ===")
coordinates = 10, 20  # Parentheses are optional
print(f"coordinates = 10, 20 → {coordinates} (type: {type(coordinates)})")
print()

# Accessing tuple elements (same as lists)
print("=== Indexing ===")
point = (3, 4, 5)
print(f"point: {point}")
print(f"point[0]: {point[0]}")
print(f"point[-1]: {point[-1]}")
print(f"point[1:3]: {point[1:3]}")
print()

# Immutability demonstration
print("=== Immutability ===")
point = (3, 4)
print(f"Original point: {point}")
try:
    point[0] = 10
except TypeError as e:
    print(f"Trying point[0] = 10 → TypeError: {e}")
print()

# Tuple methods (count and index only)
print("=== Tuple Methods ===")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"numbers: {numbers}")
print(f"numbers.count(2): {numbers.count(2)}")
print(f"numbers.index(4): {numbers.index(4)}")
print(f"len(numbers): {len(numbers)}")
print(f"2 in numbers: {2 in numbers}")
print()

# Tuples as dictionary keys
print("=== Tuples as Dict Keys ===")
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
}
nyc_coords = (40.7128, -74.0060)
print(f"Location at {nyc_coords}: {locations[nyc_coords]}")
print("\nNote: Lists can't be dict keys because they're mutable!")
