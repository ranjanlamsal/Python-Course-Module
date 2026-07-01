# demo_comparison_and_logical.py
# ---------------------------------------------------------
# Module 3 - Operators & Branching Logic
# Concept: comparison operators (==, !=, <, >, <=, >=) always produce a
# bool. Logical operators (and, or, not) combine multiple bools into one.
#
# RUN THIS WITH:  python demo_comparison_and_logical.py
# ---------------------------------------------------------

age = 20
has_id_card = True

# --- Comparison operators: each one asks a yes/no question ---
print(age == 20)              # True  -- equality check
print(age != 20)               # False -- "not equal" check
print(age >= 18)               # True
print(age < 18)                # False

# --- Logical operators: combining conditions ---

# 'and' -- BOTH sides must be True for the whole thing to be True
can_enter_venue = (age >= 18) and has_id_card
print(can_enter_venue)         # True

# 'or' -- EITHER side being True is enough
has_student_or_senior_discount = (age < 13) or (age >= 65)
print(has_student_or_senior_discount)   # False -- 20 satisfies neither side

# 'not' -- flips a single boolean value
is_minor = not (age >= 18)
print(is_minor)                # False, because (age >= 18) was True

# Common bug demonstration: mixing up 'and' and 'or' changes the meaning
# entirely. Compare these two carefully:
print((age >= 18) and has_id_card)   # must satisfy BOTH conditions
print((age >= 18) or has_id_card)    # only needs ONE of the two conditions

# TRY IT YOURSELF: write a single boolean expression that is True only when
# someone is a teenager (13 <= age <= 19). You'll need 'and'.
