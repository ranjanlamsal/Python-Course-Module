# demo_break_continue_pass.py
# ---------------------------------------------------------
# Module 4 - Iteration Essentials
# Concept: break (exit the loop entirely), continue (skip to the next
# iteration), and pass (do nothing -- a placeholder).
#
# RUN THIS WITH:  python demo_break_continue_pass.py
# ---------------------------------------------------------

# --- continue: skip even numbers, only print odd ones ---
print("Odd numbers 1-10:")
for number in range(1, 11):
    if number % 2 == 0:
        continue          # skip everything below, jump straight to the next number
    print(number)

print("---")

# --- break: stop the entire loop the moment we find what we're looking for ---
print("Searching for the first multiple of 7:")
for number in range(1, 100):
    if number % 7 == 0:
        print(f"Found it: {number}")
        break              # stop searching immediately -- 8..99 are never even checked
    # if we didn't break on this pass, the loop just moves on to the next number

print("---")

# --- pass: a deliberate no-op, used as a placeholder ---
print("Using pass as a placeholder:")
for number in range(1, 4):
    if number == 2:
        pass               # intentionally does nothing -- placeholder for logic to add later
    else:
        print(f"Handling {number}")

# NOTE: `pass` produced NO output for number == 2 -- that's expected. It is
# NOT the same as `continue`. Code placed after a `pass` in the same
# iteration still runs; code placed after a `break` in that iteration does not.

# TRY IT YOURSELF: loop through range(1, 21) and use `continue` to skip any
# number divisible by 3, printing all the others.
