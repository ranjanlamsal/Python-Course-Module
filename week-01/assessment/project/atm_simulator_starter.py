# atm_simulator_starter.py
# ---------------------------------------------------------
# THE SMART ATM SIMULATOR -- Week 1 Mandatory Project
#
# This file is a STRUCTURE ONLY -- it contains no working solution.
# Read PROJECT_SPEC.md fully before writing anything here, and follow
# its Step-by-Step Execution Plan: build and test one stage at a time,
# do not attempt Stage 4+ until Stage 3 is fully working.
# ---------------------------------------------------------

# ===========================================================
# STAGE 1 -- Setup
# ===========================================================
# TODO: create a `balance` variable with a starting value of your choice
# TODO: create a `pin` variable holding a hardcoded 4-digit PIN (as a string)


# ===========================================================
# STAGE 2 & 3 -- Authentication: max 3 attempts, using a while loop
# ===========================================================
# Build Stage 2 (a single PIN check with no loop) FIRST, get it fully
# working, and only then wrap it in the attempt-limited while loop below.
#
# You need a variable to track HOW MANY attempts have been made so far,
# and a variable to track WHETHER authentication has succeeded -- both
# need to exist before the loop starts.

# TODO: create an attempts counter, starting at 0
# TODO: create an "authenticated" flag, starting as False

# TODO: while attempts is less than 3 AND not yet authenticated:
    # TODO: ask the user to enter the PIN
    # TODO: increase the attempts counter
    # TODO: compare the entered PIN to the hardcoded PIN
    #       - if it matches: set the authenticated flag to True, print a
    #         success message
    #       - if it doesn't match: print how many attempts remain

# TODO: after the loop ends, check the authenticated flag:
#       - if True: proceed to Stage 4 below
#       - if False: print a lockout message and make sure the account
#         menu code below is NEVER reached in this case


# ===========================================================
# STAGE 4 -- Account menu skeleton (only reachable if authenticated)
# ===========================================================
# TODO: an infinite loop (while True) that:
#         - prints the menu options (check balance / deposit / withdraw / exit)
#         - reads the user's choice
#         - for now, just print("you chose ...") for each option --
#           don't implement the real logic until the menu itself works


# ===========================================================
# STAGE 5 -- Check Balance
# ===========================================================
# TODO: replace the placeholder for this option with real logic:
#       print the current balance


# ===========================================================
# STAGE 6 -- Deposit
# ===========================================================
# TODO: ask for a deposit amount, cast it to a number, add it to balance,
#       print the confirmed new balance


# ===========================================================
# STAGE 7 -- Withdraw (with validation)
# ===========================================================
# TODO: ask for a withdrawal amount, cast it to a number
# TODO: if the amount is greater than the current balance:
#           reject it with a clear message, balance stays unchanged
#       else:
#           subtract it from balance, print the confirmed new balance


# ===========================================================
# STAGE 4 (continued) -- Exit
# ===========================================================
# TODO: when the user chooses exit, print a goodbye message and make sure
#       the infinite loop actually stops (what keyword ends a loop
#       immediately?)


# ===========================================================
# STAGE 8 -- Manual test checklist (do this before Thursday)
# ===========================================================
# Run this file multiple times and confirm ALL of the following happen
# correctly. Check each one off in your own head (or with a comment) --
# this list is not graded, it's for YOU:
#
#   [ ] Wrong PIN 3 times in a row -> locked out, menu never appears
#   [ ] Correct PIN on attempt 1 -> menu appears
#   [ ] Correct PIN on attempt 2 or 3 -> menu appears
#   [ ] Check balance shows the right number after no other actions
#   [ ] Deposit increases balance correctly
#   [ ] Withdraw decreases balance correctly when amount <= balance
#   [ ] Withdraw is REJECTED when amount > balance, and balance is unchanged
#   [ ] Withdrawing the EXACT full balance brings it to exactly 0, not negative
#   [ ] Exit ends the program cleanly, menu does not reappear afterward
