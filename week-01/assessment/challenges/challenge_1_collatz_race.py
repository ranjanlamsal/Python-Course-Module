# challenge_1_collatz_race.py
# ---------------------------------------------------------
# SECTION 3, CHALLENGE 1 -- The Collatz Race  (OPTIONAL)
# Only attempt this once Sections 1 and 2 feel solid, and only if you
# have time and energy left this weekend. No solution code is provided.
# ---------------------------------------------------------
#
# PROBLEM:
#   1. Ask the user for a positive integer.
#   2. Repeatedly apply this rule until the number reaches 1:
#        - if the number is EVEN, divide it by 2
#        - if the number is ODD, multiply it by 3 and add 1
#   3. Count how many steps it took to reach 1, and print that count.
#
# EXAMPLE (starting at 6):
#   6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1   (8 steps)
#
# HINTS (no code given, just direction):
#   - This is naturally a `while` loop: keep going WHILE the number
#     is not yet 1.
#   - You'll need a step counter, created before the loop, incremented
#     once per pass -- same pattern as the running-total exercise.
#   - Try printing the number at each step first, to visually confirm
#     your even/odd branching is correct, before you trust the final count.

# TODO: it's your turn -- no scaffolding beyond the hints above.
