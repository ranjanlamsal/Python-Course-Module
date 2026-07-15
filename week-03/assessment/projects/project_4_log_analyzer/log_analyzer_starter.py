"""
Project 4: Server Log Analyzer
Starter file—implement the TODOs below.
"""

# TODO 1: Define custom exception class
class InvalidLogFormatError(Exception):
    """Raised when log line doesn't match expected format."""
    pass


# TODO 2: Implement parse_log_line function
def parse_log_line(line):
    """
    Parse a log line: timestamp | level | message

    Args:
        line: Raw log line (string)

    Returns:
        dict: {"timestamp": "...", "level": "...", "message": "..."}

    Raises:
        InvalidLogFormatError: If line format is incorrect
    """
    # Split by " | " delimiter
    # Check that there are exactly 3 parts
    # Validate that level is one of: INFO, WARNING, ERROR
    # Return dict with parsed fields

    pass  # Your code here


# TODO 3: Implement analyze_log_file function
def analyze_log_file(filename):
    """
    Analyze log file and return statistics.

    Args:
        filename: Path to log file

    Returns:
        dict: Statistics {"total": int, "malformed": int, "counts": {"INFO": ..., "WARNING": ..., "ERROR": ...}}

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    stats = {
        "total": 0,
        "malformed": 0,
        "counts": {"INFO": 0, "WARNING": 0, "ERROR": 0}
    }

    error_lines = []

    # TODO: Read file line-by-line with context manager
    # For each line:
    #   - Increment total count
    #   - Try to parse line with parse_log_line()
    #   - If successful, increment count for that level
    #   - If level is ERROR, add line to error_lines list
    #   - If InvalidLogFormatError, increment malformed count and print warning

    # TODO: Write ERROR lines to error_report.txt

    pass  # Your code here

    return stats


# TODO 4: Implement display_report function
def display_report(stats):
    """
    Display formatted report.

    Args:
        stats: Statistics dict from analyze_log_file()
    """
    valid = stats["total"] - stats["malformed"]

    print("\nSummary:")
    print("--------")
    print(f"Total lines: {stats['total']}")
    print(f"Malformed lines: {stats['malformed']}")
    print(f"Valid lines: {valid}")

    print("\nLog Level Counts:")
    # TODO: Display each log level with count and percentage
    # Format: "  INFO: 65 (67.0%)"

    pass  # Your code here

    print("\nERROR lines written to: error_report.txt")


# TODO 5: Implement main function
def main():
    """Main entry point."""
    print("Server Log Analyzer")
    filename = input("Enter log file name (default: server.log): ").strip()

    if not filename:
        filename = "server.log"

    print(f"\nAnalyzing log file: {filename}")

    try:
        # TODO: Call analyze_log_file() and display_report()
        pass

    except FileNotFoundError:
        print("Cannot proceed without log file.")


if __name__ == "__main__":
    main()
