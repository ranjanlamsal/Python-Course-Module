"""
Demo: Custom Exception Classes
Shows: the TooShortError example from class
"""

# Define a custom exception
class TooShortError(Exception):
    """Raised when input is shorter than required length."""
    pass

def validate_message(message, min_length=10):
    """
    Check if message meets minimum length.

    Args:
        message: The message to validate
        min_length: Minimum required length (default: 10)

    Raises:
        TooShortError: If message is too short

    Returns:
        True if valid
    """
    if len(message) < min_length:
        raise TooShortError(f"Message must be at least {min_length} characters (got {len(message)})")
    return True

# Example 1: Valid message
try:
    validate_message("This is a long enough message", min_length=10)
    print("✓ Message is valid")
except TooShortError as e:
    print(f"✗ Validation failed: {e}")

# Example 2: Too short message
try:
    validate_message("Hi", min_length=10)
    print("✓ Message is valid")
except TooShortError as e:
    print(f"✗ Validation failed: {e}")

print("\n--- Another custom exception: InvalidLogFormat ---")

class InvalidLogFormatError(Exception):
    """Raised when log line doesn't match expected format."""
    pass

def parse_log_line(line):
    """
    Parse a log line: timestamp | level | message

    Raises:
        InvalidLogFormatError: If line format is incorrect
    """
    parts = line.strip().split(" | ")
    if len(parts) != 3:
        raise InvalidLogFormatError(f"Expected 3 parts, got {len(parts)}")

    timestamp, level, message = parts

    if level not in ["INFO", "WARNING", "ERROR"]:
        raise InvalidLogFormatError(f"Invalid log level: {level}")

    return {"timestamp": timestamp, "level": level, "message": message}

# Test cases
valid_log = "2024-01-15 10:30:00 | INFO | Server started"
invalid_log1 = "2024-01-15 10:30:00 INFO Server started"  # Missing separators
invalid_log2 = "2024-01-15 10:30:00 | DEBUG | Test"  # Invalid level

for log in [valid_log, invalid_log1, invalid_log2]:
    try:
        result = parse_log_line(log)
        print(f"✓ Parsed: {result}")
    except InvalidLogFormatError as e:
        print(f"✗ Parse failed: {e}")

print("\n--- Custom exception with additional data ---")

class OutOfStockError(Exception):
    """Raised when product is out of stock."""

    def __init__(self, product_name, requested, available):
        self.product_name = product_name
        self.requested = requested
        self.available = available
        message = f"{product_name}: requested {requested}, only {available} available"
        super().__init__(message)

def purchase(product_name, quantity, stock):
    """Purchase a product."""
    if quantity > stock:
        raise OutOfStockError(product_name, quantity, stock)
    return f"✓ Purchased {quantity} {product_name}"

try:
    print(purchase("Widget", 5, 10))  # OK
    print(purchase("Gadget", 15, 10))  # Out of stock
except OutOfStockError as e:
    print(f"✗ {e}")
    print(f"  Product: {e.product_name}")
    print(f"  Requested: {e.requested}")
    print(f"  Available: {e.available}")
