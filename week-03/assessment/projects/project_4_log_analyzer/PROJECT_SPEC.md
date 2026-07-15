# Project 4: Server Log Analyzer

## Overview

Build a console tool that reads a server log file, counts log levels (INFO, WARNING, ERROR), generates a report, and handles malformed lines and missing files gracefully.

**Estimated time:** 4-6 hours  
**Due:** Wednesday night

## Learning Objectives

- Read and parse files line-by-line with context managers
- Handle specific exceptions (`FileNotFoundError`, `ValueError`)
- Create custom exception classes
- Process text data with string methods

## Requirements

### Core Features (Required)

Your log analyzer must:

1. **Read a log file** line-by-line (format: `timestamp | level | message`)
2. **Count log levels** (INFO, WARNING, ERROR)
3. **Generate summary report** (counts, percentages)
4. **Write ERROR lines** to `error_report.txt`
5. **Handle missing log file** (FileNotFoundError)
6. **Handle malformed lines** (wrong format, missing delimiters)
7. **Display statistics** (total lines, malformed lines, counts per level)

### Log File Format

```
2024-01-15 10:30:00 | INFO | Server started on port 8080
2024-01-15 10:30:15 | INFO | Database connection established
2024-01-15 10:31:00 | WARNING | High memory usage detected (85%)
2024-01-15 10:32:00 | ERROR | Failed to connect to external API
2024-01-15 10:32:05 | ERROR | Timeout after 30 seconds
malformed line without delimiters
2024-01-15 10:33:00 | INFO | Request processed successfully
```

### Technical Requirements

1. **Use context managers** (`with open(...)`) for all file operations
2. **Handle exceptions:**
   - `FileNotFoundError` — if log file doesn't exist
   - `ValueError` or `IndexError` — when parsing malformed lines
3. **Create custom exception** (e.g., `InvalidLogFormatError`) for specific validation
4. **Process line-by-line** (don't read entire file into memory at once)

### Example Output

```
Analyzing log file: server.log

Summary:
--------
Total lines: 100
Malformed lines: 3
Valid lines: 97

Log Level Counts:
  INFO: 65 (67.0%)
  WARNING: 20 (20.6%)
  ERROR: 12 (12.4%)

ERROR lines written to: error_report.txt

Done!
```

## Implementation Guide

### Step 1: Define Custom Exception

```python
class InvalidLogFormatError(Exception):
    """Raised when log line doesn't match expected format."""
    pass
```

### Step 2: Parse Log Line

```python
def parse_log_line(line):
    """
    Parse a log line: timestamp | level | message

    Args:
        line: Raw log line

    Returns:
        dict: {"timestamp": "...", "level": "...", "message": "..."}

    Raises:
        InvalidLogFormatError: If line format is incorrect
    """
    parts = line.strip().split(" | ")

    if len(parts) != 3:
        raise InvalidLogFormatError(f"Expected 3 parts, got {len(parts)}")

    timestamp, level, message = parts

    if level not in ["INFO", "WARNING", "ERROR"]:
        raise InvalidLogFormatError(f"Invalid log level: {level}")

    return {
        "timestamp": timestamp,
        "level": level,
        "message": message
    }
```

### Step 3: Count Log Levels

```python
def analyze_log_file(filename):
    """
    Analyze log file and return statistics.

    Args:
        filename: Path to log file

    Returns:
        dict: Statistics {"total": ..., "malformed": ..., "counts": {...}}

    Raises:
        FileNotFoundError: If file doesn't exist
    """
    stats = {
        "total": 0,
        "malformed": 0,
        "counts": {"INFO": 0, "WARNING": 0, "ERROR": 0}
    }

    error_lines = []

    try:
        with open(filename, "r") as f:
            for line in f:
                stats["total"] += 1

                try:
                    parsed = parse_log_line(line)
                    level = parsed["level"]
                    stats["counts"][level] += 1

                    if level == "ERROR":
                        error_lines.append(line.strip())

                except InvalidLogFormatError:
                    stats["malformed"] += 1
                    print(f"Warning: Malformed line {stats['total']}: {line.strip()}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        raise

    # Write ERROR lines to file
    if error_lines:
        with open("error_report.txt", "w") as f:
            f.write("\n".join(error_lines))

    return stats
```

### Step 4: Display Report

```python
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
    for level, count in stats["counts"].items():
        if valid > 0:
            percentage = (count / valid) * 100
            print(f"  {level}: {count} ({percentage:.1f}%)")
        else:
            print(f"  {level}: {count}")

    print("\nERROR lines written to: error_report.txt")
```

### Step 5: Main Function

```python
def main():
    """Main entry point."""
    print("Server Log Analyzer")
    filename = input("Enter log file name (default: server.log): ").strip()

    if not filename:
        filename = "server.log"

    print(f"\nAnalyzing log file: {filename}")

    try:
        stats = analyze_log_file(filename)
        display_report(stats)
        print("\nDone!")

    except FileNotFoundError:
        print("Cannot proceed without log file.")

if __name__ == "__main__":
    main()
```

## Sample Log File

Create `sample_server_log.txt` with this content (included in starter):

```
2024-01-15 10:00:00 | INFO | Server started on port 8080
2024-01-15 10:00:15 | INFO | Database connection established
2024-01-15 10:01:00 | INFO | User 'alice' logged in
2024-01-15 10:02:00 | WARNING | High memory usage (85%)
2024-01-15 10:03:00 | INFO | Request processed in 120ms
malformed line without delimiters
2024-01-15 10:04:00 | ERROR | Database connection lost
2024-01-15 10:04:05 | INFO | Attempting to reconnect
2024-01-15 10:04:10 | ERROR | Reconnection failed after 3 attempts
another malformed line
2024-01-15 10:05:00 | INFO | User 'bob' logged in
2024-01-15 10:06:00 | WARNING | API rate limit approaching (90%)
2024-01-15 10:07:00 | ERROR | External API timeout after 30s
2024-01-15 10:08:00 | INFO | Fallback to cached data
2024-01-15 10:09:00 | INFO | Request completed successfully
```

## Testing Checklist

Test these scenarios:

- [ ] Analyze valid log file (all lines parse correctly)
- [ ] Handle malformed lines (skip with warning)
- [ ] Handle missing log file (FileNotFoundError)
- [ ] Count each log level correctly
- [ ] Write ERROR lines to error_report.txt
- [ ] Calculate percentages correctly
- [ ] Handle empty log file
- [ ] Handle log with only malformed lines

## Stretch Goals (Optional)

- Filter by date range (e.g., show only logs from 10:00-11:00)
- Search for specific error messages (regex or substring)
- Generate HTML report instead of plain text
- Support multiple log formats (auto-detect delimiter)
- Chart log levels over time (ASCII bar chart)

## Submission

Submit `log_analyzer_starter.py` (renamed to `log_analyzer.py` with your implementation) and `sample_server_log.txt`.

## Grading Criteria

- **Functionality (40%):** All core features work
- **File I/O (25%):** Context managers used, line-by-line reading
- **Exception handling (25%):** Handles FileNotFoundError and malformed lines
- **Code quality (10%):** Clear names, docstrings, organized

## Common Mistakes

See [`../../common_mistakes.md`](../../common_mistakes.md) for patterns to avoid, especially:
- Forgetting `with` statement
- Reading entire file at once (memory issue for large logs)
- Bare `except:` catching everything
- Not stripping whitespace before parsing

## Need Help?

- Re-read [`session-2-lambda-files-exceptions/02-file-io.md`](../../../session-2-lambda-files-exceptions/02-file-io.md)
- Re-read [`session-2-lambda-files-exceptions/03-exceptions-and-custom-errors.md`](../../../session-2-lambda-files-exceptions/03-exceptions-and-custom-errors.md)
- Run [`demo_file_reading.py`](../../../session-2-lambda-files-exceptions/code/demo_file_reading.py)
- Run [`demo_custom_errors.py`](../../../session-2-lambda-files-exceptions/code/demo_custom_errors.py)
- Attend office hours
