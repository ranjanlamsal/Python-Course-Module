# demo_dynamic_typing.py
# ---------------------------------------------------------
# Module 2 - Data Fundamentals & Transformation
# Concept: Python is DYNAMICALLY TYPED -- a variable name is just a label
# that can be re-pointed at a value of ANY type, at any time.
#
# RUN THIS WITH:  python demo_dynamic_typing.py
# ---------------------------------------------------------

mystery = 10
print(mystery, type(mystery))     # starts life as an int -- <class 'int'>

# Reassigning `mystery` to a string does NOT cause an error.
# Python does not "lock" a variable to its first type the way some
# other languages do.
mystery = "now I'm text"
print(mystery, type(mystery))     # same variable name, completely different type

# And now the SAME name again, this time holding a boolean.
mystery = True
print(mystery, type(mystery))

# IMPORTANT QUIRK: booleans behave like numbers under the hood.
# True acts like 1, False acts like 0. This is legal Python, but it can
# surprise you if you're not expecting it:
print(True + True)     # 2, not an error and not "TrueTrue"
print(False + 5)       # 5

# TRY IT YOURSELF: add one more reassignment of `mystery` to a float value,
# print it and its type, then predict what `mystery + 1` would do BEFORE
# you add that line and run it.
