"""
Exercise 4: Exception Handling
Practice: try/except for specific exceptions, try/except/else/finally
"""

# TODO 1: Write a function that safely converts a string to int
# Return the int if successful, or None if ValueError occurs
def safe_int(value):
    """
    Convert string to int safely.

    Args:
        value: String to convert

    Returns:
        int if successful, None if ValueError
    """
    pass  # Replace with your code


# Uncomment to test
# print(safe_int("42"))   # Expected: 42
# print(safe_int("abc"))  # Expected: None


# TODO 2: Write a function that reads a file and returns its content
# Handle FileNotFoundError by returning an empty string
def read_file_safely(filename):
    """
    Read file content safely.

    Args:
        filename: Path to file

    Returns:
        str: File content, or empty string if file not found
    """
    pass  # Replace with your code


# Uncomment to test
# content = read_file_safely("existing_file.txt")  # Returns content
# content = read_file_safely("missing_file.txt")    # Returns ""


# TODO 3: Write a function that divides two numbers
# Handle both ValueError (bad input) and ZeroDivisionError
def safe_divide(a, b):
    """
    Divide two numbers safely.

    Args:
        a: Numerator (can be string)
        b: Denominator (can be string)

    Returns:
        float if successful, None if error
    """
    pass  # Replace with your code


# Uncomment to test
# print(safe_divide("10", "2"))   # Expected: 5.0
# print(safe_divide("10", "0"))   # Expected: None (ZeroDivisionError)
# print(safe_divide("abc", "2"))  # Expected: None (ValueError)


# TODO 4: Write a function that demonstrates try/except/else/finally
# Open a file, read it, print success message, and ensure file closes
def read_with_finally(filename):
    """
    Read file with try/except/else/finally.

    try: Open and read file
    except FileNotFoundError: Print error
    else: Print success message (runs if no exception)
    finally: Print "Cleanup complete" (always runs)
    """
    pass  # Replace with your code


# Uncomment to test
# read_with_finally("existing_file.txt")
# read_with_finally("missing_file.txt")


# TODO 5: Create a custom exception and use it
class NegativeValueError(Exception):
    """Raised when a value is negative but must be positive."""
    pass


def calculate_square_root(value):
    """
    Calculate square root (simplified, no math.sqrt).

    Args:
        value: Number to find square root of

    Returns:
        float: Square root (using **0.5)

    Raises:
        NegativeValueError: If value is negative
    """
    pass  # Replace with your code


# Uncomment to test
# print(calculate_square_root(16))  # Expected: 4.0
# try:
#     calculate_square_root(-4)
# except NegativeValueError as e:
#     print(f"Error: {e}")


# TODO 6: Write a function that processes a list of strings to ints
# Skip any values that can't be converted (ValueError)
# Return list of successfully converted ints
def convert_list_to_ints(string_list):
    """
    Convert list of strings to ints, skipping invalid values.

    Args:
        string_list: List of strings

    Returns:
        list: List of ints (skips unconvertible values)
    """
    pass  # Replace with your code


# Uncomment to test
# result = convert_list_to_ints(["10", "20", "abc", "30", "xyz", "40"])
# print(result)  # Expected: [10, 20, 30, 40]


# TODO 7: Write a function that reads a file and counts lines
# Handle FileNotFoundError and return 0 if file doesn't exist
# Use try/except/else structure
def count_lines(filename):
    """
    Count lines in a file.

    Args:
        filename: Path to file

    Returns:
        int: Number of lines, or 0 if file not found
    """
    pass  # Replace with your code


# Uncomment to test
# Create test file first
# with open("test_lines.txt", "w") as f:
#     f.write("Line 1\n")
#     f.write("Line 2\n")
#     f.write("Line 3\n")
#
# print(count_lines("test_lines.txt"))  # Expected: 3
# print(count_lines("missing.txt"))     # Expected: 0
