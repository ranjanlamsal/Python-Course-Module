"""
Challenge 2: Recursive Functions (Optional, Ungraded)
Practice: recursion, base cases, recursive cases

Recursion is a powerful technique where a function calls itself.
This is NOT required for Week 3 projects, but it's great practice for understanding function calls.
"""

# TODO 1: Write a recursive function to calculate factorial
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# factorial(0) = 1 (base case)
def factorial(n):
    """
    Calculate factorial recursively.

    Args:
        n: Non-negative integer

    Returns:
        int: Factorial of n
    """
    pass  # Your code here


# Uncomment to test
# print(factorial(5))   # Expected: 120
# print(factorial(0))   # Expected: 1
# print(factorial(1))   # Expected: 1


# TODO 2: Write a recursive function to calculate Fibonacci
# fibonacci(0) = 0 (base case)
# fibonacci(1) = 1 (base case)
# fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
def fibonacci(n):
    """
    Calculate nth Fibonacci number recursively.

    Args:
        n: Non-negative integer

    Returns:
        int: nth Fibonacci number
    """
    pass  # Your code here


# Uncomment to test
# print(fibonacci(0))   # Expected: 0
# print(fibonacci(1))   # Expected: 1
# print(fibonacci(5))   # Expected: 5 (0, 1, 1, 2, 3, 5)
# print(fibonacci(10))  # Expected: 55


# TODO 3: Write a recursive function to sum a list
# sum_list([1, 2, 3, 4]) = 1 + sum_list([2, 3, 4]) = ... = 10
# sum_list([]) = 0 (base case)
def sum_list(numbers):
    """
    Sum a list recursively.

    Args:
        numbers: List of numbers

    Returns:
        int/float: Sum of numbers
    """
    pass  # Your code here


# Uncomment to test
# print(sum_list([1, 2, 3, 4]))  # Expected: 10
# print(sum_list([]))            # Expected: 0


# TODO 4 (ADVANCED): Recursive directory traversal
# List all .txt files in a directory and subdirectories
# Hint: Use os.listdir() and os.path.isdir()
import os

def find_txt_files(directory):
    """
    Find all .txt files in directory and subdirectories (recursively).

    Args:
        directory: Root directory to search

    Returns:
        list: List of paths to .txt files
    """
    pass  # Your code here


# Uncomment to test (after creating test directory structure)
# Create test directory structure:
# test_dir/
#   file1.txt
#   file2.py
#   subdir/
#     file3.txt
#     file4.md
#
# txt_files = find_txt_files("test_dir")
# print(txt_files)
# Expected: ['test_dir/file1.txt', 'test_dir/subdir/file3.txt']


# BONUS: Explain why this is a bad recursive function
def infinite_recursion(n):
    """What's wrong with this?"""
    return infinite_recursion(n - 1)  # Missing base case!

# Don't run this—it will crash with RecursionError!
# Lesson: Every recursive function MUST have a base case.
