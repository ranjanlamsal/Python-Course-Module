# demo_while_loop.py
# ---------------------------------------------------------
# Module 4 - Iteration Essentials
# Concept: while loops repeat AS LONG AS a condition stays True. YOU are
# responsible for making that condition eventually become False, or the
# loop runs forever.
#
# RUN THIS WITH:  python demo_while_loop.py
# ---------------------------------------------------------

# --- A normal, self-terminating while loop ---
countdown = 5
while countdown > 0:
    print(countdown)
    countdown = countdown - 1   # THIS line is what eventually makes the condition False
print("Liftoff!")

print("---")

# --- An INTENTIONAL infinite loop, broken out of from inside ---
# `while True:` never becomes False on its own -- the ONLY thing that ends
# this loop is the `break` statement below.
attempts = 0
while True:
    attempts = attempts + 1
    print(f"Attempt number {attempts}")
    if attempts == 3:
        print("Reached 3 attempts -- breaking out now.")
        break                     # this is the ONLY thing that ends this loop

print("Done.")

# --- DANGEROUS EXPERIMENT (do this once, on purpose, so you recognize it) ---
# Uncomment the 3 lines below, save, and run this file again. You will need
# to press Ctrl+C in your terminal to force-stop the program, because the
# condition NEVER becomes False -- `runaway` is never changed inside the loop.
#
# runaway = 0
# while runaway < 5:
#     print("This never stops because `runaway` is never updated!")

# TRY IT YOURSELF: write a while loop that starts at 100 and prints every
# value as it counts DOWN by 10 each time, stopping once it reaches 0.
