# demo_for_loop_range.py
# ---------------------------------------------------------
# Module 4 - Iteration Essentials
# Concept: for loops + range(). CRITICAL RULE: range(stop) produces numbers
# starting at 0, up to but NOT INCLUDING stop. This trips up everyone at
# first -- read every comment below carefully.
#
# RUN THIS WITH:  python demo_for_loop_range.py
# ---------------------------------------------------------

# range(5) -- starts at 0, stops BEFORE 5. Produces exactly 5 numbers:
# 0, 1, 2, 3, 4 -- notice 5 itself never appears.
print("range(5):")
for i in range(5):
    print(i)

print("---")

# range(2, 6) -- starts at 2 (inclusive), stops before 6 (exclusive).
print("range(2, 6):")
for i in range(2, 6):
    print(i)

print("---")

# range(0, 10, 2) -- start 0, stop before 10, STEP by 2 (even numbers only).
print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(i)

print("---")

# for loops work over ANY sequence, not just range(). Looping directly over
# a string iterates one character at a time.
print("Looping over a string:")
for letter in "MIT":
    print(letter)

# TRY IT YOURSELF: write a for loop using range(...) that prints the numbers
# 1 through 10 INCLUSIVE (all ten numbers, including 10 itself). Remember:
# range's stop value is never included, so what stop value do you actually
# need to pass in?
