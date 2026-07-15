# File I/O — Reading and Writing Files

## Why File I/O Matters

Your programs so far lose all data when they exit. **File I/O** lets you persist data between runs: save user preferences, log events, store records, generate reports.

## File Modes

When opening a file, you specify a **mode**:

| Mode | Description | Creates if missing? | Overwrites? |
|------|-------------|---------------------|-------------|
| `'r'` | Read (default) | No (error if missing) | N/A |
| `'w'` | Write | Yes | **Yes** (truncates file) |
| `'a'` | Append | Yes | No (adds to end) |
| `'r+'` | Read + Write | No (error if missing) | No |
| `'w+'` | Write + Read | Yes | **Yes** (truncates file) |

**Most common:** `'r'` for reading, `'w'` for writing (overwrite), `'a'` for appending.

## Context Managers — The `with` Statement

**Always** use `with` when working with files. It ensures the file is closed, even if an exception occurs.

```python
# ✅ CORRECT: with statement
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed here

# ❌ WRONG: manual close (fragile)
f = open("data.txt", "r")
content = f.read()
f.close()  # If an exception occurs before this, file stays open!
```

**Why `with` matters:**
- Resource leak prevention (open file handles consume system resources)
- Works even if exception occurs inside the block
- Cleaner, more Pythonic code

## Reading Files

### Method 1: Read Entire File as String

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

**Use when:** File is small, you need the whole thing at once.

### Method 2: Read One Line

```python
with open("data.txt", "r") as f:
    first_line = f.readline()
    second_line = f.readline()
    print(first_line, second_line)
```

**Use when:** You only need a few lines.

### Method 3: Read All Lines as List

```python
with open("data.txt", "r") as f:
    lines = f.readlines()  # List of strings, each ending with \n

for line in lines:
    print(line.strip())  # .strip() removes trailing \n
```

**Use when:** File is small, you need all lines at once.

### Method 4: Iterate Line-by-Line (Best for Large Files)

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
```

**Use when:** File is large, or you only need one line at a time. Most memory-efficient.

## Writing Files

### Write a String

```python
with open("output.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is line 2.\n")
```

**Note:** `write()` does **not** add newlines automatically. You must include `\n`.

### Write Multiple Lines

```python
lines = ["First line\n", "Second line\n", "Third line\n"]

with open("output.txt", "w") as f:
    f.writelines(lines)
```

**Warning:** Mode `'w'` **overwrites** the file. To append instead, use `'a'`.

### Append to a File

```python
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

## File Paths

### Relative Paths

```python
# Relative to current working directory
with open("data.txt", "r") as f:
    pass

# Relative path with subdirectory
with open("data/input.txt", "r") as f:
    pass
```

### Absolute Paths

```python
# Full path (works regardless of working directory)
with open("/Users/alice/data.txt", "r") as f:
    pass
```

**Tip:** Use forward slashes `/` even on Windows (Python handles conversion).

## Example: Processing a Log File

```python
# Read log file, count ERROR lines, write report
error_count = 0

with open("server.log", "r") as infile:
    for line in infile:
        if "ERROR" in line:
            error_count += 1

with open("error_report.txt", "w") as outfile:
    outfile.write(f"Total errors: {error_count}\n")

print(f"Found {error_count} errors. Report saved to error_report.txt")
```

**This is the exact shape of Project 4 (Log Analyzer)**, shown on a simplified example.

## Mapping to Project 4 (Log Analyzer)

Your Log Analyzer will:
1. Open `server.log` in read mode
2. Iterate line-by-line (memory-efficient for large logs)
3. Parse each line (split by delimiter, extract log level)
4. Count occurrences of each level (INFO, WARNING, ERROR)
5. Write ERROR lines to `error_report.txt`
6. Handle `FileNotFoundError` if log doesn't exist (next section)

## Common Pitfalls

### Forgetting to Close the File

```python
# ❌ File stays open if you forget f.close()
f = open("data.txt", "r")
content = f.read()
# ... later code ...
f.close()  # Easy to forget!

# ✅ with ensures it closes
with open("data.txt", "r") as f:
    content = f.read()
# Closed automatically
```

### Overwriting When You Meant to Append

```python
# ❌ This erases the file every time!
with open("log.txt", "w") as f:
    f.write("New entry\n")

# ✅ Use 'a' to append
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

### Not Handling Missing Files

```python
# ❌ Crashes if file doesn't exist
with open("data.txt", "r") as f:
    content = f.read()

# ✅ Handle the exception (next section)
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found!")
```

## Key Takeaways

- **File modes:** `'r'` (read), `'w'` (write/overwrite), `'a'` (append)
- **Context managers:** Always use `with open(...)` to ensure files close
- **Reading:** `.read()` (whole file), `.readline()` (one line), iterate (line-by-line, best for large files)
- **Writing:** `.write()` (no auto-newline), `.writelines()` (list of strings)
- **Paths:** Relative or absolute, use `/` even on Windows

Next: [Exceptions and Custom Errors](./03-exceptions-and-custom-errors.md)
