# challenge_2_password_strength_auditor.py
# ---------------------------------------------------------
# SECTION 3, CHALLENGE 2 -- Password Strength Auditor  (OPTIONAL)
# Only attempt this once Sections 1 and 2 feel solid, and only if you
# have time and energy left this weekend. No solution code is provided.
# ---------------------------------------------------------
#
# PROBLEM:
#   1. Ask the user to enter a password as text.
#   2. Loop through it ONE CHARACTER AT A TIME and count:
#        - how many characters are digits
#        - how many characters are uppercase letters
#        - how many characters are "other" (symbols, spaces, etc.)
#   3. Using that breakdown PLUS the password's total length, print a
#      strength rating of "Weak", "Moderate", or "Strong" using rules
#      you design yourself (there is no single correct rule set here --
#      justify your own thresholds).
#
# THIS GOES SLIGHTLY BEYOND WHAT WAS TAUGHT IN CLASS ON PURPOSE.
# Research these on your own (docs.python.org or Real Python -- search
# for "Python string methods"):
#   - a_string.isdigit()   -> True if a single character is a digit
#   - a_string.isupper()   -> True if a single character is uppercase
#   - a_string.islower()   -> True if a single character is lowercase
#   - len(a_string)        -> the total length of a string
#
# HINTS:
#   - You already know how to loop over a string character by character
#     (see Module 4's demo_for_loop_range.py, the "Looping over a string"
#     section) -- this challenge reuses that exact pattern.
#   - Three counters, all starting at 0, updated inside one loop with
#     if/elif branching per character -- similar shape to earlier
#     exercises, just with string methods instead of arithmetic checks.

# TODO: it's your turn -- no scaffolding beyond the hints above.
