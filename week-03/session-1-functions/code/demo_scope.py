"""
Demo: Scope and LEGB Rule
Shows: Local, Enclosing, Global, Built-in scope resolution
"""

# Global scope
x = "global x"

def outer():
    """Enclosing scope for inner()."""
    x = "enclosing x"

    def inner():
        """Local scope."""
        x = "local x"
        print(f"inner() sees: {x}")  # local x

    inner()
    print(f"outer() sees: {x}")  # enclosing x

outer()
print(f"module sees: {x}")  # global x

print("\n--- Variable Shadowing ---")

name = "Alice"

def greet():
    """This creates a NEW local variable, doesn't affect global."""
    name = "Bob"
    print(f"Inside greet(): {name}")

greet()  # Bob
print(f"Outside greet(): {name}")  # Alice (unchanged)

print("\n--- The global Keyword ---")

counter = 0

def increment_wrong():
    """This FAILS because Python thinks counter is local."""
    # Uncommenting the line below causes UnboundLocalError:
    # counter += 1  # Error: local variable 'counter' referenced before assignment
    pass

def increment_right():
    """This works because we declare counter as global."""
    global counter
    counter += 1

increment_right()
increment_right()
print(f"Counter: {counter}")  # 2

print("\n--- Built-in Scope ---")

# len is a built-in function
def show_length(items):
    return len(items)  # Uses built-in len()

print(show_length([1, 2, 3]))  # 3

# ❌ Don't shadow built-ins (bad practice but allowed)
def bad_example():
    len = 10  # Shadows built-in len
    # print(len([1, 2, 3]))  # TypeError: 'int' object is not callable
    print(f"len is now: {len}")

bad_example()
