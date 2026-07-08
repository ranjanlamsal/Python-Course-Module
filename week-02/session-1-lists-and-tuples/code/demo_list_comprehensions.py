"""
Demo: List Comprehensions — The Pythonic Way to Transform Lists
Run this file to see list comprehensions in action.
"""

# Basic comprehension (transforming)
print("=== Basic Comprehension ===")
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(f"Original: {numbers}")
print(f"Squares: {squares}")
print()

# With a condition (filtering)
print("=== Comprehension with Filter ===")
numbers = range(1, 11)
evens = [n for n in numbers if n % 2 == 0]
print(f"Numbers 1-10: {list(numbers)}")
print(f"Even numbers: {evens}")

evens_squared = [n ** 2 for n in numbers if n % 2 == 0]
print(f"Squares of evens: {evens_squared}")
print()

# String transformations
print("=== String Transformations ===")
names = ["alice", "bob", "charlie"]
capitalized = [name.upper() for name in names]
print(f"Original: {names}")
print(f"Capitalized: {capitalized}")

# Filter strings by length
long_names = [name for name in names if len(name) > 4]
print(f"Names with > 4 chars: {long_names}")
print()

# Nested comprehensions (advanced)
print("=== Nested Comprehensions ===")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")
print()

# Comparison with traditional loop
print("=== Loop vs Comprehension ===")

# Traditional way
squares_loop = []
for n in range(1, 6):
    squares_loop.append(n ** 2)
print(f"Using loop: {squares_loop}")

# Comprehension way
squares_comp = [n ** 2 for n in range(1, 6)]
print(f"Using comprehension: {squares_comp}")
print("\nBoth produce the same result, but comprehension is more concise!")
