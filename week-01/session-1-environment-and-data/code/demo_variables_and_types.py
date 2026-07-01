# demo_variables_and_types.py
# ---------------------------------------------------------
# Module 2 - Data Fundamentals & Transformation
# Concept: variables as "labeled storage boxes", and the type() function.
#
# RUN THIS WITH:  python demo_variables_and_types.py
# ---------------------------------------------------------

# Assign a value to a variable -- this is the box being labeled and filled.
# The name on the left (favorite_number) is the label; the value on the
# right (7) is what goes inside the box.
favorite_number = 7
print(favorite_number)          # look inside the box

# Reassign it -- same box, brand new contents. The old value (7) is gone
# completely the moment this next line runs.
favorite_number = 42
print(favorite_number)

# Two variables are two completely independent boxes.
# Changing one has ZERO effect on the other.
city = "Kathmandu"
temperature_celsius = 22.5

print(city)
print(temperature_celsius)

# type() tells you what kind of value is currently inside a box.
# Every single value in Python has a type -- there is no "untyped" data.
print(type(favorite_number))        # <class 'int'>
print(type(city))                   # <class 'str'>
print(type(temperature_celsius))    # <class 'float'>

# TRY IT YOURSELF: create a new variable called `is_student` set to True,
# print it, and print its type. What type name do you expect to see?
