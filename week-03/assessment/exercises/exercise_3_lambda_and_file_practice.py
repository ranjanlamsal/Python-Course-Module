"""
Exercise 3: Lambda and File Practice
Practice: lambda with sorted/filter, reading/writing files
"""

# TODO 1: Sort this list of tuples by the second element (age)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 28)]

# Use sorted() with a lambda function
sorted_by_age = None  # Replace with your code

# Uncomment to test
# print(sorted_by_age)  # Expected: [('Bob', 25), ('Diana', 28), ('Alice', 30), ('Charlie', 35)]


# TODO 2: Filter out all negative numbers from this list
numbers = [10, -5, 3, -2, 8, -1, 15, 0]

# Use filter() with a lambda function, convert to list
positive_numbers = None  # Replace with your code

# Uncomment to test
# print(positive_numbers)  # Expected: [10, 3, 8, 15]


# TODO 3: Sort this list of dictionaries by price (ascending)
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300},
]

# Use sorted() with a lambda function
sorted_by_price = None  # Replace with your code

# Uncomment to test
# print(sorted_by_price)
# Expected: [{'name': 'Mouse', 'price': 25}, ...]


# TODO 4: Write numbers 1-10 to a file, one per line
# Use a context manager (with statement)
def write_numbers_to_file(filename):
    pass  # Replace with your code


# Uncomment to test
# write_numbers_to_file("numbers.txt")
# Check that the file was created and contains 1-10, one per line


# TODO 5: Read a file and return a list of lines (without \n)
def read_lines(filename):
    """Read file and return list of lines with whitespace stripped."""
    pass  # Replace with your code


# Uncomment to test (after creating numbers.txt in TODO 4)
# lines = read_lines("numbers.txt")
# print(lines)  # Expected: ['1', '2', '3', ..., '10']


# TODO 6: Count how many lines in a file contain a specific word
def count_word_occurrences(filename, word):
    """
    Count how many lines contain the given word (case-insensitive).

    Returns:
        int: Number of lines containing the word
    """
    pass  # Replace with your code


# Uncomment to test
# Create a test file first
# with open("test_text.txt", "w") as f:
#     f.write("Hello world\n")
#     f.write("Python is great\n")
#     f.write("Hello again\n")
#     f.write("Goodbye\n")
#
# count = count_word_occurrences("test_text.txt", "hello")
# print(count)  # Expected: 2


# TODO 7: Use filter and lambda to get all products over $50
# Then use map and lambda to apply a 10% discount to those products
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300},
]

# Step 1: Filter products over $50
expensive = None  # Replace with filter() and lambda

# Step 2: Apply 10% discount (multiply price by 0.9)
discounted = None  # Replace with map() and lambda

# Convert to list and print
# Uncomment to test
# result = list(discounted)
# print(result)
# Expected: [{'name': 'Laptop', 'price': 900.0}, ...]
