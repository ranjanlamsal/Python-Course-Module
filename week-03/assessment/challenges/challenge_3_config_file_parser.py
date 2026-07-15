"""
Challenge 3: Config File Parser (Optional, Ungraded)
Parse custom config format, validate, handle errors

This challenge simulates parsing a simple .ini-style config file:

[section1]
key1=value1
key2=value2

[section2]
key3=value3

Parse this into a nested dict:
{
    "section1": {"key1": "value1", "key2": "value2"},
    "section2": {"key3": "value3"}
}
"""

class ConfigParseError(Exception):
    """Raised when config file has invalid format."""
    pass


def parse_config(filename):
    """
    Parse a custom config file.

    Format:
    - [section_name] starts a new section
    - key=value defines a key-value pair in current section
    - Blank lines and lines starting with # are ignored

    Args:
        filename: Path to config file

    Returns:
        dict: Nested dict {section: {key: value}}

    Raises:
        FileNotFoundError: If file doesn't exist
        ConfigParseError: If line is malformed
    """
    pass  # Your code here


# Uncomment to test
# Create test config file
# with open("test_config.ini", "w") as f:
#     f.write("# This is a comment\n")
#     f.write("[database]\n")
#     f.write("host=localhost\n")
#     f.write("port=5432\n")
#     f.write("\n")
#     f.write("[app]\n")
#     f.write("name=MyApp\n")
#     f.write("version=1.0\n")
#
# config = parse_config("test_config.ini")
# print(config)
# Expected:
# {
#     "database": {"host": "localhost", "port": "5432"},
#     "app": {"name": "MyApp", "version": "1.0"}
# }


def validate_config(config, required_sections):
    """
    Validate that config has required sections.

    Args:
        config: Config dict from parse_config()
        required_sections: List of required section names

    Raises:
        ConfigParseError: If required section is missing
    """
    pass  # Your code here


# Uncomment to test
# validate_config(config, ["database", "app"])  # Should pass
# try:
#     validate_config(config, ["database", "app", "logging"])
# except ConfigParseError as e:
#     print(f"Validation failed: {e}")


def get_config_value(config, section, key, default=None):
    """
    Safely get a config value with default fallback.

    Args:
        config: Config dict
        section: Section name
        key: Key name
        default: Default value if not found

    Returns:
        Value from config, or default if not found
    """
    pass  # Your code here


# Uncomment to test
# print(get_config_value(config, "database", "host"))  # Expected: localhost
# print(get_config_value(config, "database", "user", "admin"))  # Expected: admin (default)


# BONUS: Write a function to save config back to file
def save_config(config, filename):
    """
    Save config dict to file in the same format.

    Args:
        config: Nested dict {section: {key: value}}
        filename: Output filename
    """
    pass  # Your code here


# Uncomment to test
# save_config(config, "output_config.ini")
# # Check that output_config.ini matches the format
