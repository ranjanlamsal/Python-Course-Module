"""
Demo: File Reading
Shows: reading files with context managers, different reading methods
"""

# First, let's create a sample file to read
with open("sample_data.txt", "w") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: World\n")
    f.write("Line 3: Python\n")
    f.write("Line 4: Programming\n")

print("--- Method 1: Read entire file as string ---")
with open("sample_data.txt", "r") as f:
    content = f.read()
    print(content)

print("\n--- Method 2: Read one line at a time ---")
with open("sample_data.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"First: {line1.strip()}")
    print(f"Second: {line2.strip()}")

print("\n--- Method 3: Read all lines as list ---")
with open("sample_data.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line.strip()}")

print("\n--- Method 4: Iterate line-by-line (best for large files) ---")
with open("sample_data.txt", "r") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"Line {line_num}: {line.strip()}")

print("\n--- Processing: Count words per line ---")
with open("sample_data.txt", "r") as f:
    for line in f:
        words = line.strip().split()
        print(f"{line.strip()} -> {len(words)} words")
