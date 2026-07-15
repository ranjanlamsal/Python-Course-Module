"""
Demo: Exception Handling
Shows: try/except for ValueError and FileNotFoundError
"""

print("--- Example 1: ValueError (bad int() cast) ---")
try:
    age = int("abc")
    print(f"Age: {age}")
except ValueError as e:
    print(f"ValueError caught: {e}")

print("\n--- Example 2: FileNotFoundError ---")
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError caught: {e}")

print("\n--- Example 3: Multiple exception types ---")
def divide(a, b):
    try:
        result = int(a) / int(b)
        print(f"{a} / {b} = {result}")
    except ValueError:
        print("Error: Invalid number format")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

divide("10", "2")   # OK
divide("abc", "5")  # ValueError
divide("10", "0")   # ZeroDivisionError

print("\n--- Example 4: try/except/else/finally ---")
def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
    else:
        # Runs if NO exception
        print(f"Successfully read {len(content)} characters")
    finally:
        # ALWAYS runs
        print(f"Finished attempting to read {filename}")

read_file("sample_data.txt")  # If exists from previous demo
read_file("missing.txt")

print("\n--- Example 5: Catching multiple exceptions same handler ---")
try:
    # This could raise ValueError or ZeroDivisionError
    result = int("10") / int("0")
except (ValueError, ZeroDivisionError) as e:
    print(f"Math error: {e}")

print("\n--- Example 6: Bare except (DON'T DO THIS) ---")
# ❌ This catches EVERYTHING, including KeyboardInterrupt
# try:
#     risky_code()
# except:
#     print("Something went wrong")

# ✅ Better: catch Exception
try:
    x = 1 / 0
except Exception as e:
    print(f"Caught exception: {type(e).__name__}: {e}")
