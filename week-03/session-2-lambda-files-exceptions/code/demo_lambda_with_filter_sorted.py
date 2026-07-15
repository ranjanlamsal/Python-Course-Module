"""
Demo: Lambda with sorted() and filter()
Shows: the EXACT examples from class
"""

print("--- Lambda with sorted() ---")

# Example 1: Sort by second element of tuple
word_pairs = [("apple", 5), ("banana", 6), ("cherry", 6), ("date", 4)]
sorted_pairs = sorted(word_pairs, key=lambda pair: pair[1])
print(f"Word pairs sorted by length: {sorted_pairs}")
# [('date', 4), ('apple', 5), ('banana', 6), ('cherry', 6)]

# Example 2: Sort by absolute value
numbers = [-5, 2, -3, 8, -1]
sorted_by_abs = sorted(numbers, key=lambda x: abs(x))
print(f"Numbers sorted by absolute value: {sorted_by_abs}")
# [-1, 2, -3, -5, 8]

# Example 3: Sort dictionaries by value
prices = {"apple": 1.50, "banana": 0.75, "cherry": 2.00}
sorted_prices = sorted(prices.items(), key=lambda item: item[1])
print(f"Prices sorted: {sorted_prices}")
# [('banana', 0.75), ('apple', 1.5), ('cherry', 2.0)]

print("\n--- Lambda with filter() ---")

# Example 1: Filter even numbers (EXACT from class)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(f"Even numbers: {evens}")
# [2, 4, 6, 8, 10]

# Example 2: Filter strings longer than 5 chars
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"Words longer than 5 chars: {long_words}")
# ['banana', 'cherry', 'elderberry']

# Example 3: Filter positive numbers
mixed = [-5, 3, -2, 8, 0, -1, 4]
positives = list(filter(lambda x: x > 0, mixed))
print(f"Positive numbers: {positives}")
# [3, 8, 4]

print("\n--- Lambda with map() ---")

# Example 1: Square each number
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n ** 2, numbers))
print(f"Squared: {squared}")
# [1, 4, 9, 16, 25]

# Example 2: Uppercase strings
words = ["hello", "world", "python"]
upper = list(map(lambda s: s.upper(), words))
print(f"Uppercase: {upper}")
# ['HELLO', 'WORLD', 'PYTHON']

print("\n--- Chaining: filter then map ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Get even numbers, then square them
result = list(map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers)))
print(f"Evens squared: {result}")
# [4, 16, 36, 64, 100]
