"""
Challenge 1: Advanced File Processor (Optional, Ungraded)
Merge multiple files, deduplicate, sort, handle missing files gracefully

This challenge integrates multiple Week 3 concepts:
- File I/O (reading multiple files)
- Exception handling (FileNotFoundError)
- Functions (organizing the logic)
- Data structures (sets for deduplication)
"""

def merge_and_process_files(file_list, output_file):
    """
    Merge multiple text files, remove duplicate lines, sort, and write to output.

    Process:
    1. Read all files in file_list
    2. If a file is missing, print warning and skip it
    3. Collect all lines (strip whitespace)
    4. Remove duplicates (use a set)
    5. Sort lines alphabetically
    6. Write sorted unique lines to output_file

    Args:
        file_list: List of input filenames
        output_file: Output filename

    Returns:
        dict: Statistics {"files_read": int, "total_lines": int, "unique_lines": int}
    """
    pass  # Your code here


# Uncomment to test
# Create test files first
# with open("file1.txt", "w") as f:
#     f.write("apple\n")
#     f.write("banana\n")
#     f.write("cherry\n")
#
# with open("file2.txt", "w") as f:
#     f.write("banana\n")
#     f.write("date\n")
#     f.write("apple\n")
#
# with open("file3.txt", "w") as f:
#     f.write("cherry\n")
#     f.write("elderberry\n")
#
# stats = merge_and_process_files(
#     ["file1.txt", "file2.txt", "file3.txt", "missing.txt"],
#     "merged.txt"
# )
# print(stats)
# Expected: {"files_read": 3, "total_lines": 8, "unique_lines": 5}
#
# # Check merged.txt content:
# with open("merged.txt", "r") as f:
#     print(f.read())
# Expected (sorted, unique):
# apple
# banana
# cherry
# date
# elderberry
