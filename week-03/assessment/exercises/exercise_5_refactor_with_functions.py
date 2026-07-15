"""
Exercise 5: Refactor with Functions
Practice: identifying repetition, extracting reusable functions
"""

# TODO 1: This code has repetition. Refactor it into a reusable function.

# Original code (don't modify this):
"""
name1 = "alice"
name1_normalized = name1.strip().lower()
print(f"Normalized: {name1_normalized}")

name2 = "  BOB  "
name2_normalized = name2.strip().lower()
print(f"Normalized: {name2_normalized}")

name3 = "Charlie"
name3_normalized = name3.strip().lower()
print(f"Normalized: {name3_normalized}")
"""

# Refactored version:
def normalize_name(name):
    """
    Normalize a name: strip whitespace and convert to lowercase.

    Args:
        name: Name to normalize

    Returns:
        str: Normalized name
    """
    pass  # Replace with your code


# Uncomment to test
# print(normalize_name("alice"))      # Expected: alice
# print(normalize_name("  BOB  "))    # Expected: bob
# print(normalize_name("Charlie"))    # Expected: charlie


# TODO 2: This code calculates percentage multiple times. Extract a function.

# Original code (don't modify this):
"""
score1 = 85
total1 = 100
percentage1 = (score1 / total1) * 100
print(f"Percentage: {percentage1}%")

score2 = 42
total2 = 50
percentage2 = (score2 / total2) * 100
print(f"Percentage: {percentage2}%")

score3 = 18
total3 = 25
percentage3 = (score3 / total3) * 100
print(f"Percentage: {percentage3}%")
"""

# Refactored version:
def calculate_percentage(score, total):
    """
    Calculate percentage.

    Args:
        score: Achieved score
        total: Total possible score

    Returns:
        float: Percentage (0-100)
    """
    pass  # Replace with your code


# Uncomment to test
# print(calculate_percentage(85, 100))  # Expected: 85.0
# print(calculate_percentage(42, 50))   # Expected: 84.0
# print(calculate_percentage(18, 25))   # Expected: 72.0


# TODO 3: Refactor this Contact Book code with functions

# Original code (don't modify this):
"""
contacts = {}

# Add contact
name = input("Name: ")
phone = input("Phone: ")
contacts[name.lower()] = {"phone": phone}

# Search contact
search = input("Search: ")
if search.lower() in contacts:
    print(contacts[search.lower()])
else:
    print("Not found")

# Delete contact
delete = input("Delete: ")
if delete.lower() in contacts:
    del contacts[delete.lower()]
    print("Deleted")
else:
    print("Not found")
"""

# Refactored version:

def add_contact(contacts, name, phone):
    """Add a contact (case-insensitive)."""
    pass  # Replace with your code


def search_contact(contacts, name):
    """Search for a contact (case-insensitive). Returns contact dict or None."""
    pass  # Replace with your code


def delete_contact(contacts, name):
    """Delete a contact (case-insensitive). Returns True if deleted, False if not found."""
    pass  # Replace with your code


# Uncomment to test
# contacts = {}
# add_contact(contacts, "Alice", "555-1234")
# add_contact(contacts, "Bob", "555-5678")
# print(search_contact(contacts, "alice"))  # Expected: {'phone': '555-1234'}
# print(search_contact(contacts, "ALICE"))  # Expected: {'phone': '555-1234'}
# print(delete_contact(contacts, "bob"))    # Expected: True
# print(search_contact(contacts, "Bob"))    # Expected: None


# TODO 4: Refactor this file processing code into reusable functions

# Original code (don't modify this):
"""
# Read log file
with open("app.log", "r") as f:
    lines = f.readlines()

# Count ERROR lines
error_count = 0
for line in lines:
    if "ERROR" in line:
        error_count += 1

print(f"Errors: {error_count}")

# Write error lines to file
with open("errors.txt", "w") as f:
    for line in lines:
        if "ERROR" in line:
            f.write(line)
"""

# Refactored version:

def count_level(lines, level):
    """
    Count how many lines contain a specific log level.

    Args:
        lines: List of log lines
        level: Log level to count (e.g., "ERROR", "WARNING")

    Returns:
        int: Count of matching lines
    """
    pass  # Replace with your code


def filter_lines_by_level(lines, level):
    """
    Filter lines that contain a specific log level.

    Args:
        lines: List of log lines
        level: Log level to filter (e.g., "ERROR")

    Returns:
        list: Lines containing the level
    """
    pass  # Replace with your code


def write_lines_to_file(lines, filename):
    """
    Write lines to a file.

    Args:
        lines: List of strings to write
        filename: Output filename
    """
    pass  # Replace with your code


# Uncomment to test
# Create test log file first
# with open("app.log", "w") as f:
#     f.write("INFO: App started\n")
#     f.write("ERROR: Connection failed\n")
#     f.write("WARNING: Low memory\n")
#     f.write("ERROR: Timeout\n")
#
# with open("app.log", "r") as f:
#     lines = f.readlines()
#
# errors = filter_lines_by_level(lines, "ERROR")
# print(count_level(lines, "ERROR"))  # Expected: 2
# write_lines_to_file(errors, "errors_only.txt")
