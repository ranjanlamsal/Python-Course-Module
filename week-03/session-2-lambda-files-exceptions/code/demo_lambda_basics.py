"""
Demo: Lambda Basics
Shows: lambda syntax, simple examples
"""

# Lambda syntax: lambda args: expression
add = lambda a, b: a + b
print(add(3, 5))  # 8

square = lambda x: x ** 2
print(square(4))  # 16

is_even = lambda n: n % 2 == 0
print(is_even(4))  # True
print(is_even(7))  # False

# Lambda with no arguments
get_greeting = lambda: "Hello, world!"
print(get_greeting())  # Hello, world!

# Lambda with multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24

# Lambda vs named function
# These are equivalent:

def add_regular(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print(add_regular(10, 20))  # 30
print(add_lambda(10, 20))   # 30
