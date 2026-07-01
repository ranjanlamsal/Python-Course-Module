# Project Specification — The Smart ATM Simulator

**Status: Mandatory. This is the project Thursday's 30-minute review is built from.**
**No solution code is provided anywhere in this repo.** The starter file (`atm_simulator_starter.py`) gives you structure and `# TODO:` markers only.

## The Goal

Build a command-line tool that mimics a physical ATM: it authenticates a user with a PIN, then lets them check their balance, deposit money, and withdraw money — safely, without ever letting the balance go negative.

## Feature Requirements

### 1. Initial Setup
- Initialize a variable holding the user's starting **balance** (any starting number you choose, e.g. `1000`).
- Initialize a variable holding a **hardcoded 4-digit PIN** (e.g. `"1234"`) — this is fixed in the code itself, not something the user sets.

### 2. Authentication (build this part first — see the execution plan below)
- The user gets a **strict maximum of 3 attempts** to enter the correct PIN.
- Use a `while` loop to enforce this — it must be impossible to get a 4th attempt.
- If the PIN entered matches, authentication succeeds and the program moves on to account actions.
- If all 3 attempts are used without a correct match, the program should print a lockout message and end **without ever reaching the account menu.**

### 3. Account Actions (only reachable after successful authentication)
Once authenticated, present a menu, in an infinite loop, with these options:
- **Check balance** — display the current balance.
- **Deposit money** — ask for an amount, add it to the balance, confirm the new balance.
- **Withdraw money** — ask for an amount, and:
  - if the amount is **greater than the current balance**, reject it with a clear message and **do not change the balance**.
  - otherwise, subtract it from the balance and confirm the new balance.
  - **the balance must never be allowed to go negative, under any input.**
- **Exit** — ends the program cleanly (a normal, expected way out — not a crash).

The menu must keep reappearing after every action until the user chooses to exit.

### 4. What "done" looks like
A user can run your script, get 3 tries at a hardcoded PIN, and — if successful — check their balance, deposit, withdraw (with the negative-balance rule enforced), and exit cleanly, as many times through the menu as they want, in any order.

## Step-by-Step Execution Plan

**Do not try to build this all at once. Build and manually test each stage before moving to the next.**

1. **Stage 1 — Hardcode and print.** Just create the `balance` and `pin` variables and `print()` them. Confirm the file runs with no errors before adding any logic at all.
2. **Stage 2 — Single PIN check, no loop yet.** Ask the user once for a PIN with `input()`, compare it to the hardcoded PIN, and print "Access granted" or "Access denied." Get this exact comparison working correctly (watch for type/string issues) before adding the attempt limit.
3. **Stage 3 — Wrap it in the 3-attempt loop.** Now put Stage 2's logic inside a `while` loop bounded to 3 attempts. Test all three outcomes by hand: succeeding on attempt 1, succeeding on attempt 2 or 3, and failing all 3. Do not move on until all three outcomes behave correctly.
4. **Stage 4 — Add the menu skeleton, no real actions yet.** After authentication succeeds, add an infinite `while True:` loop that just prints menu options and reads a choice — have each option temporarily just `print("you chose X")` with no real logic yet. Confirm you can navigate the menu repeatedly and exit cleanly.
5. **Stage 5 — Implement Check Balance.** The simplest option — just display the current value of `balance`.
6. **Stage 6 — Implement Deposit.** Ask for an amount, cast it, add it to `balance`, confirm.
7. **Stage 7 — Implement Withdraw, with validation.** This is the trickiest step. Get the "reject if amount > balance" check working and test it deliberately by trying to overdraw.
8. **Stage 8 — Full manual test pass.** Run the whole program start to finish multiple times, deliberately trying to break it: wrong PIN 3 times, correct PIN on the last try, withdrawing more than the balance, withdrawing exactly the full balance, depositing then withdrawing, exiting and confirming nothing runs afterward.

**Why authentication first?** The account menu is useless without working authentication guarding it, and testing menu logic is much harder if you also have to fight through PIN entry every single run. Building and fully trusting Stage 3 before touching Stage 4 is the single biggest time-saver available to you this weekend.

## Self-Diagnosis Before Thursday

Before class, re-read [`../common_mistakes.md`](../common_mistakes.md) and honestly check your own code against each item — most of what gets discussed Thursday will be recognizable from that list.
