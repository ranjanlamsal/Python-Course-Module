"""
Demo: File Writing
Shows: writing to files, append mode, overwrite behavior
"""

print("--- Writing (overwrite mode) ---")
with open("output.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

print("Wrote 3 lines to output.txt")

# Read it back to verify
with open("output.txt", "r") as f:
    print(f.read())

print("\n--- Writing again (overwrites!) ---")
with open("output.txt", "w") as f:
    f.write("This erases everything before!\n")

with open("output.txt", "r") as f:
    print(f.read())  # Only the new line remains

print("\n--- Appending (preserves existing content) ---")
with open("output.txt", "a") as f:
    f.write("Appended line 1\n")
    f.write("Appended line 2\n")

with open("output.txt", "r") as f:
    print(f.read())

print("\n--- Writing multiple lines with writelines() ---")
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("multiline.txt", "w") as f:
    f.writelines(lines)

with open("multiline.txt", "r") as f:
    print(f.read())

print("\n--- Writing without newlines (common mistake) ---")
with open("no_newlines.txt", "w") as f:
    f.write("Line 1")  # No \n
    f.write("Line 2")  # No \n
    f.write("Line 3")

with open("no_newlines.txt", "r") as f:
    print(f"Content: '{f.read()}'")  # All on one line!

print("\n--- Correct: Always add newlines ---")
with open("with_newlines.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

with open("with_newlines.txt", "r") as f:
    print(f.read())
