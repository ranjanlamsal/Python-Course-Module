# demo_if_elif_else.py
# ---------------------------------------------------------
# Module 3 - Operators & Branching Logic
# Concept: if/elif/else branching. Python checks conditions TOP TO BOTTOM
# and stops at the FIRST one that is True -- everything after is skipped.
#
# RUN THIS WITH:  python demo_if_elif_else.py
# Then CHANGE the `temperature` value below and run it again several times.
# ---------------------------------------------------------

temperature = 28

if temperature < 0:
    category = "freezing"
elif temperature < 15:
    category = "cold"
elif temperature < 25:
    category = "mild"
elif temperature < 35:
    category = "hot"
else:
    category = "extreme heat"

print(f"{temperature}°C is classified as: {category}")

# Only ONE branch ever runs per pass through this block, no matter how many
# conditions would ALSO technically be true. With temperature = 28:
#   - "< 0"  is False
#   - "< 15" is False
#   - "< 25" is False
#   - "< 35" is True   <-- Python stops HERE, "hot" is chosen
#   - the else branch is never even checked
#
# TRY IT YOURSELF: set temperature to -5, then 10, then 20, then 40, saving
# and re-running each time. Confirm exactly one category prints each time.
#
# THEN TRY THIS: swap the order of the "< 35" and "< 15" lines above and
# re-run with temperature = 10. Does the result change? Why does order
# matter here when conditions can overlap?
