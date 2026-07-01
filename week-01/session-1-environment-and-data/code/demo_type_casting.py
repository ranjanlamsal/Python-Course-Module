# demo_type_casting.py
# ---------------------------------------------------------
# Module 2 - Data Fundamentals & Transformation
# Concept: EXPLICIT TYPE CASTING with int(), float(), and str().
# input() ALWAYS returns a string -- casting is how you convert it.
#
# RUN THIS WITH:  python demo_type_casting.py
# ---------------------------------------------------------

# Casting a numeric-looking string into a real integer.
raw_input_value = "42"                # this is a STRING, even though it looks like a number
as_integer = int(raw_input_value)     # now it's a real int -- math works on it
print(as_integer + 8, type(as_integer))   # 50 <class 'int'>

# Casting a number into a string -- useful for building display text with '+'.
price = 3.14
as_text = str(price)
print("The price is " + as_text, type(as_text))

# Casting a float DOWN to an int TRUNCATES (chops the decimal part) --
# it does NOT round to the nearest whole number.
print(int(9.99))    # 9, not 10
print(int(-9.99))   # -9, not -10 (it chops toward zero, it doesn't "round down")

# --- What happens when a cast is IMPOSSIBLE ---
# Uncomment the line below and run this file again to see a real crash.
# Read the red error text carefully -- it names the exact conversion that failed.
# This is a preview of "exceptions", which we learn to handle gracefully in Week 3.
#
# broken = int("hello")

# TRY IT YOURSELF: ask the user for their age with input(), cast it to an
# int, and print what their age will be in 10 years. If you forget to cast,
# what do you predict `input_value + 10` will do instead of adding 10?
