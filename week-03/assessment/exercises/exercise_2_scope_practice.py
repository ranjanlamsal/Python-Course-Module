"""
Exercise 2: Scope Practice
Practice: LEGB rule, variable shadowing, avoiding global
"""

# TODO 1: Fix this function so it returns the correct value
# The variable 'result' is local to the function
def calculate_sum(a, b):
    result = a + b
    # return ???  # Add return statement

# Uncomment to test
# print(calculate_sum(10, 20))  # Expected: 30


# TODO 2: Predict the output without running
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"inner: {x}")

    inner()
    print(f"outer: {x}")

outer()
print(f"module: {x}")

# What will this print?
# Your prediction:
# inner: ???
# outer: ???
# module: ???


# TODO 3: Fix this function without using 'global'
# It should return the new counter value
counter = 0

def increment():
    # This fails because counter is not defined locally
    # counter += 1  # UnboundLocalError
    # return counter
    pass

# Fixed version (don't use 'global'):
def increment_fixed(current_count):
    pass  # Replace with your code


# Uncomment to test
# counter = increment_fixed(counter)
# counter = increment_fixed(counter)
# print(counter)  # Expected: 2


# TODO 4: Refactor this code to avoid global state
# Use function parameters and return values instead
total = 0

def add_to_total(value):
    global total
    total += value

# Rewrite as a pure function:
def add_pure(current_total, value):
    pass  # Replace with your code


# Uncomment to test
# total = 0
# total = add_pure(total, 10)
# total = add_pure(total, 20)
# print(total)  # Expected: 30


# TODO 5: Understand variable shadowing
# What does this print? Run it to check your prediction.
def shadowing_example():
    x = "outer"

    def inner():
        x = "inner"  # This shadows the outer x
        return x

    result = inner()
    print(f"inner returned: {result}")
    print(f"outer x is still: {x}")

# Uncomment to test
# shadowing_example()
# Your prediction:
# inner returned: ???
# outer x is still: ???
