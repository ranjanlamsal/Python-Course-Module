# exercise_2_branching_logic.py
# ---------------------------------------------------------
# SECTION 1, EXERCISE 2 -- Amusement Park Ride Eligibility Checker  (MANDATORY)
# Concept: complex decision branching with and / or / not
#
# Full problem description and expected terminal interaction are in
# ../README.md -- read both example interactions there before starting.
# ---------------------------------------------------------
#
# RULES TO IMPLEMENT:
#   1. Anyone under 100cm tall is NEVER allowed on the ride, no exceptions
#      -- this rule overrides everything else below.
#   2. Otherwise: a rider is allowed if they are at least 12 years old,
#      OR they are accompanied by an adult (an adult is present, answer
#      "yes").
#
# ABSOLUTE BEGINNER TIP:
#   The height rule is completely separate from, and overrides, the
#   age/adult rule. Think about checking it FIRST and independently,
#   before you even look at combining the other two conditions with
#   and/or.

# TODO: ask for rider age, cast to int

# TODO: ask for rider height in cm, cast to int (or float)

# TODO: ask whether an adult is accompanying them ("yes"/"no")

# TODO: apply the height rule first -- if it fails, the rider cannot ride,
#       regardless of anything else

# TODO: if the height rule passes, apply the age-OR-accompanied rule and
#       print the final result
