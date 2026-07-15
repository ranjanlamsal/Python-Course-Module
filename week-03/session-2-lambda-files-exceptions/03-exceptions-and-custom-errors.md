# Exceptions and Custom Errors

## What Are Exceptions?

**Exceptions** are errors that occur during program execution. They interrupt normal flow and, if not handled, crash the program.

```python
int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
```

Without exception handling, this crashes. With handling, you can recover gracefully.

## Exception Hierarchy

All exceptions inherit from `BaseException`, but you should usually catch subclasses of `Exception`:

```
BaseException
├── SystemExit (raised by sys.exit())
├── KeyboardInterrupt (Ctrl+C)
└── Exception
    ├── ValueError (bad value for a type)
    ├── TypeError (wrong type)
    ├── FileNotFoundError (file doesn't exist)
    ├── KeyError (dict key doesn't exist)
    ├── IndexError (list index out of range)
    ├── ZeroDivisionError (divide by zero)
    └── ... (many more)
```

**Why this matters:** You can catch specific exceptions and handle each differently.

## Basic try/except

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("That's not a valid number!")
```

**Flow:**
1. Try to run code in `try` block
2. If `ValueError` occurs, jump to `except` block
3. If no exception, skip `except` block

## Catching Multiple Exceptions

### Separate handlers

```python
try:
    data = {"name": "Alice"}
    print(data["age"])  # KeyError
except KeyError:
    print("Key not found")
except TypeError:
    print("Type error")
```

### Same handler for multiple types

```python
try:
    result = int("abc") / 0
except (ValueError, ZeroDivisionError) as e:
    print(f"Math error: {e}")
```

## try/except/else/finally

```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found")
else:
    # Runs if NO exception occurred
    print(f"Read {len(content)} characters")
finally:
    # ALWAYS runs (cleanup)
    if 'f' in locals():
        f.close()
```

**Structure:**
- `try`: Code that might raise an exception
- `except`: Handles specific exceptions
- `else`: Runs if no exception (optional)
- `finally`: Always runs, even if exception (optional, used for cleanup)

**With context managers, you rarely need `finally` for files:**

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
else:
    print(f"Read {len(content)} characters")
# No finally needed—with closes the file
```

## Why Bare `except:` Is Dangerous

```python
# ❌ WRONG: catches EVERYTHING, even KeyboardInterrupt
try:
    risky_operation()
except:
    print("Something went wrong")
```

This catches `KeyboardInterrupt` (Ctrl+C), `SystemExit`, and other exceptions you shouldn't catch. You can't interrupt the program!

**Better:**

```python
# ✅ Catch only Exception subclasses
try:
    risky_operation()
except Exception as e:
    print(f"Error: {e}")
```

**Best:**

```python
# ✅ Catch specific exceptions
try:
    age = int(input("Age: "))
except ValueError as e:
    print(f"Invalid input: {e}")
```

## Raising Exceptions

You can raise exceptions explicitly:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except ValueError as e:
    print(f"Transaction failed: {e}")
```

## Custom Exception Classes

Create domain-specific exceptions for clarity:

```python
class TooShortError(Exception):
    """Raised when input is shorter than required length."""
    pass

def validate_message(message, min_length=10):
    """Check if message meets minimum length."""
    if len(message) < min_length:
        raise TooShortError(f"Message must be at least {min_length} characters")
    return True

# Usage
try:
    validate_message("Hi", min_length=10)
except TooShortError as e:
    print(f"Validation failed: {e}")
```

**This is the exact example from class.** Notice:
- Custom exception inherits from `Exception`
- Can pass a message when raising
- Can catch it specifically

## Example: File Processing with Error Handling

```python
def process_file(filename):
    """Read a file, parse each line as an integer, return sum."""
    total = 0
    
    try:
        with open(filename, "r") as f:
            for line_num, line in enumerate(f, start=1):
                try:
                    value = int(line.strip())
                    total += value
                except ValueError:
                    print(f"Line {line_num}: skipping malformed data '{line.strip()}'")
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return None
    
    return total

# Usage
result = process_file("numbers.txt")
if result is not None:
    print(f"Total: {result}")
```

**This is the Log Analyzer pattern:** read file line-by-line, handle malformed lines, handle missing file.

## Mapping to Project 4 (Log Analyzer)

Your Log Analyzer will:
1. **Handle `FileNotFoundError`** if `server.log` doesn't exist
2. **Handle malformed lines** (lines that don't match expected format)
   - Use `try/except ValueError` when parsing log level or timestamp
3. **Optional: Create custom error** for specific validation (e.g., `InvalidLogFormatError`)

```python
# Example shape (not full solution):
try:
    with open("server.log", "r") as f:
        for line in f:
            try:
                # Parse line: timestamp, level, message
                parts = line.strip().split(" | ")
                level = parts[1]
                # ... count levels ...
            except (IndexError, ValueError):
                print(f"Skipping malformed line: {line.strip()}")
except FileNotFoundError:
    print("Log file not found")
```

## Key Takeaways

- **Exception hierarchy:** `BaseException` → `Exception` → specific types
- **try/except:** Catches exceptions, prevents crashes
- **Catch specific exceptions:** `ValueError`, `FileNotFoundError`, etc. (not bare `except:`)
- **try/except/else/finally:** else = no exception, finally = always runs
- **Raise exceptions:** `raise ValueError("message")`
- **Custom exceptions:** `class MyError(Exception): pass`
- **Why specific exceptions matter:** You can handle different errors differently

Next: [Assessment Projects](../../assessment/)
