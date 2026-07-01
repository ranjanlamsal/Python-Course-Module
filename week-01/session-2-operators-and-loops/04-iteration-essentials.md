# Module 4 — Iteration Essentials

## 4.1 `while` Loops — Condition-Based Repetition

A `while` loop repeats its body **as long as a condition stays `True`**. Python checks the condition *before* every single pass — including the very first one. If the condition is `False` from the start, the body never runs at all.

```python
while condition:
    # runs repeatedly, as long as condition is True
```

**You are responsible for making the condition eventually become `False`.** Nothing does this automatically — if nothing inside the loop body changes whatever the condition depends on, the loop runs forever (an "infinite loop").

### 🔴 LIVE CODE DEMO — Controlled loop + intentional infinite loop with `break`

Full file: [`code/demo_while_loop.py`](./code/demo_while_loop.py)

```python
# demo_while_loop.py

# A normal, self-terminating while loop
countdown = 5
while countdown > 0:
    print(countdown)
    countdown = countdown - 1   # THIS line is what eventually makes the condition False
print("Liftoff!")

# An infinite loop, deliberately broken out of from inside
attempts = 0
while True:                      # True is always True -- this NEVER stops on its own
    attempts = attempts + 1
    print(f"Attempt number {attempts}")
    if attempts == 3:
        print("Reached 3 attempts -- breaking out now.")
        break                     # this is the ONLY thing that ends this loop
```

**What to observe in your terminal:**
- The countdown prints `5, 4, 3, 2, 1` then `Liftoff!` — exactly 5 passes, because `countdown` was decremented each time until the condition became false.
- The second loop prints "Attempt number 1", "2", "3", then the break message, then **stops** — even though `while True:` by itself never stops, the `if attempts == 3: break` inside it is doing all the work of ending the loop.
- If you comment out the `countdown = countdown - 1` line in the first loop and run again, you get a real infinite loop — you'll need to force-stop it with `Ctrl+C` in the terminal. **Try this once on purpose** so you recognize what a runaway loop looks like and know how to escape it.

### ⚠️ Common Pitfalls
- **Forgetting to update the variable the condition depends on** — this is the #1 cause of accidental infinite loops. Before running any `while` loop, ask: "what line makes this condition eventually false?"
- **Writing `while True:` with no `break` anywhere inside it.** This pattern (an intentionally infinite loop controlled entirely by an internal `break`) is extremely common and useful — but only if a `break` actually exists and is reachable.
- **Off-by-one confusion in attempt-counting loops.** Deciding whether to check `attempts == 3` or `attempts < 3` or `attempts <= 3` changes whether you get 2, 3, or 4 total attempts — always trace through by hand with real numbers before trusting it.

---

## 4.2 `for` Loops and `range()`

A `for` loop repeats its body once per item in a sequence. The most common sequence to loop over when you just need to repeat something N times (rather than loop over existing data) is `range()`.

```python
for i in range(5):
    print(i)
```

**`range(stop)` produces numbers starting at 0, up to but *not including* `stop`.** `range(5)` produces `0, 1, 2, 3, 4` — five numbers total, never `5` itself. This trips up nearly everyone at first.

`range()` also accepts a start and a step: `range(start, stop)` and `range(start, stop, step)`.

### 🔴 LIVE CODE DEMO — `range()` boundaries

Full file: [`code/demo_for_loop_range.py`](./code/demo_for_loop_range.py)

```python
# demo_for_loop_range.py

# range(5) -- starts at 0, stops BEFORE 5
for i in range(5):
    print(i)

print("---")

# range(2, 6) -- starts at 2, stops before 6
for i in range(2, 6):
    print(i)

print("---")

# range(0, 10, 2) -- start 0, stop before 10, step by 2 (even numbers only)
for i in range(0, 10, 2):
    print(i)

print("---")

# Looping directly over a string -- iterates one character at a time
for letter in "MIT":
    print(letter)
```

**What to observe in your terminal:**
- The first block prints `0` through `4` — five lines, **not** including `5`.
- The second block prints `2, 3, 4, 5` — it stops right before `6`.
- The third block prints `0, 2, 4, 6, 8` — the step controls the gap between numbers, and it still excludes `10`.
- The final block prints `M`, `I`, `T` each on their own line — `for` loops work over *any* sequence, not just numbers from `range()`.

### ⚠️ Common Pitfalls
- **Assuming `range(5)` includes `5`.** It doesn't — `range(n)` always produces exactly `n` numbers, the last one being `n - 1`. If you need to count 1 through 5 inclusive, use `range(1, 6)`.
- **Using a `while` loop with a manual counter when a `for` loop with `range()` would be simpler and safer.** If you know in advance exactly how many times something should repeat, `for ... in range(...)` is almost always the better tool — there's no separate counter variable to forget to update.
- **Confusing `range(start, stop)` order** — the first number is *where counting begins*, the second is *the boundary it never reaches*, not "how many numbers to produce."

### ✅ Self-Check
1. How many times does the loop body run in `for i in range(3, 9, 2):`? List the exact values `i` takes.
2. You want a loop to run exactly 10 times, counting from 1 to 10 inclusive, printing each number. Write the `range(...)` call you'd use (describe it, don't need to run it).

<details>
<summary><b>Answer</b></summary>

1. It runs **3 times**, with `i` taking the values `3, 5, 7` — it starts at 3, adds 2 each time, and stops before reaching 9 (the next value, 9, is excluded).
2. `range(1, 11)` — starts at 1, and since `range` excludes its stop value, you need `11` as the stop to actually include `10`.

</details>

---

## 4.3 Loop Modifiers — `break`, `continue`, `pass`

| Keyword | Effect |
|---|---|
| `break` | Immediately exits the loop entirely — no more iterations happen, even if the condition/range isn't exhausted. |
| `continue` | Skips the *rest of the current iteration's body* and jumps straight to the next iteration — the loop keeps going. |
| `pass` | Does literally nothing. It's a placeholder used when Python requires a statement (e.g., an empty `if` body) but you have nothing to put there yet. |

### 🔴 LIVE CODE DEMO — Skipping items with `continue` vs. stopping with `break`

Full file: [`code/demo_break_continue_pass.py`](./code/demo_break_continue_pass.py)

```python
# demo_break_continue_pass.py

# continue: skip even numbers, only print odd ones
print("Odd numbers 1-10:")
for number in range(1, 11):
    if number % 2 == 0:
        continue          # skip everything below, jump to the next number immediately
    print(number)

print("---")

# break: stop the entire loop the moment we find what we're looking for
print("Searching for the first multiple of 7:")
for number in range(1, 100):
    if number % 7 == 0:
        print(f"Found it: {number}")
        break              # stop searching immediately -- don't check the rest of range(1, 100)
    # if we didn't break, the loop just moves on to the next number

print("---")

# pass: a deliberate no-op, used as a placeholder
for number in range(1, 4):
    if number == 2:
        pass               # intentionally does nothing here -- placeholder for logic to add later
    else:
        print(f"Handling {number}")
```

**What to observe in your terminal:**
- The first block prints only `1, 3, 5, 7, 9` — every even number was skipped via `continue` before reaching its `print()`.
- The second block prints exactly one line, `Found it: 7`, then stops — the loop never checks 8 through 99 at all, because `break` exited immediately.
- The third block prints `Handling 1` and `Handling 3`, but nothing for `2` — `pass` ran (doing nothing) instead of crashing on an empty block, but it also produced no visible output, which is expected.

### ⚠️ Common Pitfalls
- **Confusing `break` and `continue`.** `break` = "I'm done with this whole loop." `continue` = "I'm done with *this one iteration*, but keep looping." Mixing these up either ends a loop far too early or fails to skip what you meant to skip.
- **Using `pass` when you actually meant `continue`.** `pass` does not affect loop flow at all — it just avoids a syntax error in an empty block. If you wanted to skip to the next iteration, `pass` alone will not do that; code after it in the same iteration still runs.
- **Putting code after a `break` inside the same iteration and expecting it to run.** Nothing after `break` in that iteration executes — control leaves the loop immediately.

### ✅ Self-Check
1. Predict the full output:
   ```python
   for i in range(1, 6):
       if i == 3:
           break
       print(i)
   ```
2. Predict the full output:
   ```python
   for i in range(1, 6):
       if i == 3:
           continue
       print(i)
   ```

<details>
<summary><b>Answer</b></summary>

1. `1`, `2` — then the loop hits `i == 3`, breaks immediately, and `3, 4, 5` never print at all.
2. `1`, `2`, `4`, `5` — `3` is skipped via `continue`, but the loop keeps going afterward, unlike `break`.

</details>

---

**Module 4 complete — Session 2 is done.** Head to **[the Week 1 weekend assessment](../assessment/README.md)**.
