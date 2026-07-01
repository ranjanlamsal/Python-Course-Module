# exercise_4_loop_conditional_bridge.py
# ---------------------------------------------------------
# SECTION 1, EXERCISE 4 -- Number Classifier (Bridge Exercise)  (MANDATORY)
# Concept: loops + conditionals combined -- this is the closest exercise
# to the ATM project's actual structure. Get this one solid before you
# start the project in ../project/.
#
# Full problem description and expected terminal interaction are in
# ../README.md.
# ---------------------------------------------------------
#
# PROBLEM:
#   1. Repeatedly ask the user to enter a number.
#   2. For each number entered, classify and print BOTH:
#        - whether it's positive, negative, or zero
#        - whether it's even or odd
#   3. Keep asking forever UNTIL the user enters the sentinel value 0 --
#      when 0 is entered, stop the loop WITHOUT classifying it, and print
#      a goodbye message instead.
#
# ABSOLUTE BEGINNER TIP:
#   This is a `while True:` loop. Check for the sentinel value (0) FIRST,
#   with a `break`, before running any of the positive/negative/even/odd
#   classification logic. That "infinite loop + break-on-sentinel-value,
#   checked first" skeleton is exactly what the ATM Simulator's account
#   menu is built from.

# TODO: start an infinite loop (while True)

    # TODO: ask the user to enter a number, cast it to int

    # TODO: check for the sentinel value (0) FIRST -- if found, print a
    #       goodbye message and break out of the loop

    # TODO: otherwise, classify the number as positive/negative/zero
    #       (zero won't actually reach here if you break on 0 above --
    #       think about whether negative-zero-positive still needs all
    #       three branches, or just two)

    # TODO: also classify the number as even/odd, and print both
    #       classifications together
