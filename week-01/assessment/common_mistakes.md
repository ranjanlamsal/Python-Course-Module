# Common Mistakes to Learn From — ATM Simulator

Read this **before** Thursday's review, against your own finished (or unfinished) code. This is not a solution key — it's a list of failure *patterns*, so you can recognize whether you fell into one yourself and come to class already knowing what to ask about. Everything here is deliberately generic enough to apply to many possible implementations.

## Authentication mistakes

- **Comparing types that don't match.** If the hardcoded PIN is a string (`"1234"`) but the entered PIN was somehow cast to an int, `==` will always be `False`, even when the digits are "the same" — the ATM will reject a correct PIN forever. Print `type()` of both sides while debugging if a correct PIN is being rejected.
- **Resetting the attempt counter inside the loop instead of before it.** If the counter is created *inside* the `while` loop body, it gets reset to its starting value on every single pass, and the loop condition (`attempts < 3`) can never become false — an accidental infinite loop that looks like "the ATM lets me try forever."
- **Off-by-one on the attempt limit.** Depending on exactly when the counter increments relative to the comparison, it's easy to end up granting 2 or 4 attempts instead of exactly 3. Trace through the loop by hand, attempt by attempt, before trusting it.
- **Letting the account menu run even after 3 failed attempts.** This usually happens when the "authenticated" flag is checked incorrectly, or the menu code isn't actually inside a conditional block tied to that flag at all — it's easy to write code that happens to look indented correctly but isn't logically gated by authentication success.

## Balance / validation mistakes

- **Checking the withdrawal amount against balance in the wrong direction**, e.g. writing the condition for "allowed" when you meant "rejected," which silently flips the entire rule and lets overdrafts through instead of blocking them.
- **Forgetting to cast the deposit/withdrawal input before doing arithmetic on it**, causing either a crash (`str` + `int`) or, worse, no crash but silently wrong behavior (string concatenation instead of numeric addition, e.g. `"100"` becomes `"100" + "50"` = `"10050"` instead of `150`).
- **Updating the balance before validating, instead of after.** If the subtraction happens first and the "is this allowed" check happens second, a rejected withdrawal can still leave the balance changed, because the change already happened before the rejection was decided.
- **Using `<` instead of `<=` (or vice versa) at the exact-balance boundary.** Withdrawing exactly the full balance down to `0` is a common edge case that reveals whether your comparison operator is correct — if this case behaves unexpectedly, that's usually where the bug is.

## Menu / structure mistakes

- **Building the menu before the authentication loop is fully trusted**, then debugging both at once — this makes every bug ambiguous ("is this an auth bug or a menu bug?"). The project spec's staged build order exists specifically to prevent this.
- **No real exit path**, so the only way to stop the program is force-closing the terminal (`Ctrl+C`) — a working "exit" menu option that actually breaks the loop is part of the spec, not a nice-to-have.
- **One giant unbroken block of code with no logical separation between "authentication" and "account actions."** This isn't a functional bug yet, but it becomes one the moment something needs to change (this is exactly the shape Week 3's Functions module exists to fix — this project is deliberately built without functions to make you feel that pain first).

## How to use this list

Don't just read it — go back to your actual code and check each bullet against it honestly. If you find one, that's useful data to bring to Thursday, not something to hide. The review works best when it's grounded in real mistakes people actually made.
