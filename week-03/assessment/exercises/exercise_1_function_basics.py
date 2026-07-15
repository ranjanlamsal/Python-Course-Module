"""
Exercise 1: Function Basics
Practice: defining functions, default parameters, *args, **kwargs
"""

# TODO 1: Write a function that takes two numbers and returns their sum
def add(a, b):
    pass  # Replace with your code


# TODO 2: Write a function that greets a person with a default greeting
# Example: greet("Alice") -> "Hello, Alice!"
# Example: greet("Bob", "Hi") -> "Hi, Bob!"
def greet(name, greeting="Hello"):
    pass  # Replace with your code


# TODO 3: Write a function that takes any number of arguments and returns their product
# Example: multiply(2, 3, 4) -> 24
# Example: multiply(5) -> 5
# Example: multiply() -> 1 (identity for multiplication)
def multiply(*numbers):
    pass  # Replace with your code


# TODO 4: Write a function that creates a user profile dict
# It should accept username as required, any number of hobbies, and any keyword settings
# Example: make_profile("alice", "reading", "coding", theme="dark", lang="en")
# Returns: {"username": "alice", "hobbies": ["reading", "coding"], "settings": {"theme": "dark", "lang": "en"}}
def make_profile(username, *hobbies, **settings):
    pass  # Replace with your code


# TODO 5: Write a function that calculates the area of a rectangle
# It should have width as required, height with default 10, and accept a **kwargs for "unit"
# Example: area(5) -> "Area: 50 square units"
# Example: area(5, 3, unit="meters") -> "Area: 15 square meters"
def calculate_area(width, height=10, **kwargs):
    pass  # Replace with your code


# Test your functions (uncomment to test)
if __name__ == "__main__":
    # Test TODO 1
    # print(add(3, 5))  # Expected: 8

    # Test TODO 2
    # print(greet("Alice"))  # Expected: Hello, Alice!
    # print(greet("Bob", "Hi"))  # Expected: Hi, Bob!

    # Test TODO 3
    # print(multiply(2, 3, 4))  # Expected: 24
    # print(multiply(5))  # Expected: 5
    # print(multiply())  # Expected: 1

    # Test TODO 4
    # profile = make_profile("alice", "reading", "coding", theme="dark", lang="en")
    # print(profile)
    # Expected: {"username": "alice", "hobbies": ["reading", "coding"], "settings": {"theme": "dark", "lang": "en"}}

    # Test TODO 5
    # print(calculate_area(5))  # Expected: Area: 50 square units
    # print(calculate_area(5, 3, unit="meters"))  # Expected: Area: 15 square meters

    pass
