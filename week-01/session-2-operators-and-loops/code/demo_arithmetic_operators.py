# demo_arithmetic_operators.py
# ---------------------------------------------------------
# Module 3 - Operators & Branching Logic
# Concept: +, -, *, /, //, %, ** -- with special focus on // (floor
# division) and % (modulo/remainder), which only make sense TOGETHER.
#
# RUN THIS WITH:  python demo_arithmetic_operators.py
# ---------------------------------------------------------

total_minutes = 130

# // gives the number of FULL groups of 60 that fit inside total_minutes.
hours = total_minutes // 60
# % gives whatever is LEFT OVER after removing those full groups.
leftover_minutes = total_minutes % 60

print(f"{total_minutes} minutes = {hours} hour(s) and {leftover_minutes} minute(s)")

# Sanity check: floor-division result * divisor + remainder always
# reconstructs the original number. Try changing total_minutes above
# and confirm this still holds.
print((hours * 60) + leftover_minutes == total_minutes)   # True, always

# A classic use of % : checking if a number is even or odd.
number = 17
print(number % 2)   # 1 means odd, 0 would mean even

# Division (/) ALWAYS returns a float, even when it divides evenly.
print(10 / 2)    # 5.0, not 5 -- notice the decimal point
print(10 // 2)   # 5, a true integer result -- no decimal point

# Exponentiation.
print(5 ** 2)    # 25 ("5 to the power of 2")
print(2 ** 10)   # 1024

# TRY IT YOURSELF: you have 50 cookies and each box holds 6. Using // and %,
# compute how many full boxes you can pack, and how many cookies are left
# over unpacked.
