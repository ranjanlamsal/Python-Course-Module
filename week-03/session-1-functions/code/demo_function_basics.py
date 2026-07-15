"""
Demo: Function Basics
Shows: function definition, parameters, return values, calling functions
"""

def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

# Usage examples
print(greet("Alice"))           # Hello, Alice!
print(add(10, 20))              # 30
print(celsius_to_fahrenheit(0)) # 32.0
print(celsius_to_fahrenheit(100)) # 212.0

# Function with no return (returns None)
def print_greeting(name):
    """Print a greeting (no return value)."""
    print(f"Hi, {name}!")

result = print_greeting("Bob")
print(result)  # None

