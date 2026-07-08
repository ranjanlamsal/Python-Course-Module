# Presentation Slides Resources & AI Generation Prompts

## Free Ready-to-Use Presentation Resources

### Best Matches for Week 1 & Week 2

1. **Python-Lectures by rajathkmp**
   - **Link:** https://github.com/rajathkmp/Python-Lectures
   - **Format:** 8 IPython notebooks + PDF version
   - **License:** Creative Commons Attribution 3.0 (free with attribution)
   - **Topics:** Variables, Operators, Lists, Tuples, Sets, Dictionaries, Control Flow
   - **Best for:** Week 1 & 2 basics

2. **A Whirlwind Tour of Python by Jake VanderPlas**
   - **Link:** https://github.com/jakevdp/WhirlwindTourOfPython
   - **Format:** 18 Jupyter notebooks + 100-page PDF from O'Reilly
   - **License:** CC0 (Public Domain - completely free)
   - **Topics:** All Week 1 & 2 topics covered professionally
   - **Best for:** Self-paced learning with professional quality

3. **Learn Python 3 by jerry-git**
   - **Link:** https://github.com/jerry-git/learn-python3
   - **Format:** Jupyter notebooks with HTML versions
   - **License:** MIT License (very permissive)
   - **Topics:** 19+ beginner lessons covering all Week 1 & 2 content
   - **Best for:** Structured lessons with exercises

4. **Learn Python by trekhleb**
   - **Link:** https://github.com/trekhleb/learn-python
   - **Format:** Python scripts with examples and test assertions
   - **License:** MIT License
   - **Topics:** All Week 1 & 2 topics with 16k+ GitHub stars
   - **Best for:** Code examples with inline explanations

5. **Akuli's Python Tutorial**
   - **Link:** https://github.com/Akuli/python-tutorial
   - **Format:** Markdown files (can convert to HTML)
   - **License:** Freely available
   - **Topics:** 21 basic topics covering Week 1 & 2
   - **Best for:** Very beginner-friendly explanations

---

## AI Prompts for Generating Presentation Slides

### Prompt 1: Week 1 — Environment, Variables, Control Flow

```
Create a 20-slide PowerPoint presentation for Week 1 of an MIT college-level Python course. The audience is absolute beginners with no prior programming experience. The course runs for 8 sessions (2 sessions/week, 90 minutes each).

WEEK 1 COVERAGE:
- Session 1 (Thu): Environment setup (venv), variables, core types, type casting, arithmetic
- Session 2 (Fri): Conditionals, loops, break/continue/pass

SLIDE STRUCTURE:

Slide 1: Title
- Week 1: Python Basics — Environment, Variables, & Control Flow
- MIT Kathmandu — Accelerated Python Course

Slide 2: Why Virtual Environments?
- Isolation prevents dependency conflicts
- Project-specific package versions
- Clean system Python installation
- Visual: diagram showing global vs venv package isolation

Slide 3: Creating and Activating venv
- Command: python -m venv venv
- Activation: Windows vs macOS/Linux
- How to verify it's active (prompt prefix)
- Code example with terminal screenshots

Slide 4: Variables — Your First Data Container
- What is a variable? (label pointing to data)
- Dynamic typing (no declaration needed)
- Naming rules (snake_case, no reserved keywords)
- Code example: x = 10, name = "Alice"

Slide 5: Core Data Types
- int: whole numbers (42, -10)
- float: decimals (3.14, -0.5)
- str: text ("hello", 'world')
- bool: True/False
- Visual: type hierarchy diagram

Slide 6: Type Casting
- Explicit conversion: int("42"), float("3.14"), str(100)
- Common pitfall: int("hello") → ValueError
- When you need it: input() always returns strings
- Code example with input() and casting

Slide 7: Arithmetic Operators
- +, -, *, / (float division)
- // (floor division), % (modulo), ** (exponent)
- Operator precedence (PEMDAS)
- Code example: calculator expression

Slide 8: Comparison Operators
- ==, !=, <, >, <=, >=
- Returns bool (True/False)
- Common mistake: = (assignment) vs == (comparison)
- Code example: age >= 18

Slide 9: Logical Operators
- and, or, not
- Truth tables (visual diagram)
- Short-circuit evaluation
- Code example: age >= 18 and has_license

Slide 10: if/elif/else — Making Decisions
- Syntax with proper indentation
- elif chain (only first match executes)
- else as the fallback
- Code example: grade classification

Slide 11: Truthy and Falsy Values
- False: 0, 0.0, "", None, [], {}
- True: everything else
- Practical use: if name: vs if name != ""
- Code example demonstrating truthiness

Slide 12: while Loop — Conditional Repetition
- Syntax: while condition:
- Runs while condition is True
- Risk: infinite loops (missing update)
- Code example: countdown from 10

Slide 13: for Loop — Iterating Over Sequences
- Syntax: for item in sequence:
- range(): range(5), range(1, 11), range(0, 10, 2)
- More readable than while for known iterations
- Code example: print numbers 1-10

Slide 14: break — Exit Early
- Exits the innermost loop immediately
- Common use: found what you're looking for
- Code example: search for a number

Slide 15: continue — Skip to Next Iteration
- Skips the rest of the current iteration
- Jumps back to the loop condition/next item
- Code example: print only even numbers

Slide 16: pass — Placeholder for Empty Blocks
- Does nothing (syntactic placeholder)
- Useful when defining structure first
- Code example: if TODO:

Slide 17: Nested Conditionals and Loops
- if inside if (indentation matters!)
- Loop inside loop (nested iteration)
- Visual: indentation levels diagram
- Code example: multiplication table

Slide 18: Live-Coded Demo 1 — Celsius to Fahrenheit
- Full working example from Session 1
- input(), casting, arithmetic, f-string output
- Line-by-line explanation

Slide 19: Live-Coded Demo 2 — Guess the Number
- Full working example from Session 2
- while loop, counter, break, else on loop
- Line-by-line explanation

Slide 20: Week 1 Recap & Next Steps
- What we covered: venv, variables, types, operators, conditionals, loops
- Weekend project: Smart ATM Simulator
- Next week: Data structures (lists, tuples, dicts, sets)

VISUAL DESIGN REQUIREMENTS:
- Use a clean, professional MIT-style theme (dark blue/red accents)
- Code blocks: monospace font, syntax highlighting, good contrast
- Diagrams: simple, not cluttered
- No walls of text — max 5 bullet points per slide
- Include relevant icons/emojis for visual anchors (sparingly)
- Each code example should be runnable (no pseudocode)

OUTPUT FORMAT: PowerPoint (.pptx) or Google Slides link
```

---

### Prompt 2: Week 2 — Lists, Tuples, Dictionaries, Sets

```
Create a 20-slide PowerPoint presentation for Week 2 of an MIT college-level Python course. The audience has completed Week 1 (variables, types, conditionals, loops) and is now learning data structures.

WEEK 2 COVERAGE:
- Session 1 (Thu): 30-min review of Week 1 ATM project, then Lists & Tuples
- Session 2 (Fri): Dictionaries & Sets

SLIDE STRUCTURE:

Slide 1: Title
- Week 2: Data Structures — Collections & Mappings
- MIT Kathmandu — Accelerated Python Course

Slide 2: Why Data Structures Matter
- You can't build real programs with isolated variables
- Collections organize related data
- Each structure has specific strengths
- Visual: single variables vs collections diagram

Slide 3: Lists — Mutable Ordered Collections
- Syntax: [1, 2, 3, "hello", True]
- Ordered, mutable, allows duplicates
- Zero-based indexing
- Code example: fruits = ["apple", "banana", "cherry"]

Slide 4: List Indexing and Slicing
- Positive index: list[0], list[2]
- Negative index: list[-1] (last item)
- Slicing: list[1:4], list[:3], list[::2], list[::-1]
- Visual: array with index numbers diagram

Slide 5: Adding Items to Lists
- .append(item) — add to end
- .insert(index, item) — add at position
- .extend(iterable) — merge another list
- Code example showing each method

Slide 6: Removing Items from Lists
- .remove(value) — remove first occurrence
- .pop(index) — remove by position, return item
- .clear() — empty the list
- Code example showing each method

Slide 7: Sorting and Reversing Lists
- .sort() — modify in place
- sorted(list) — return new sorted list
- .reverse() — flip order in place
- Code example: numbers and strings sorting

Slide 8: List Comprehensions — The Pythonic Way
- Syntax: [expression for item in iterable if condition]
- Replaces multi-line loops
- More readable for simple transformations
- Code example: squares = [n**2 for n in range(1, 6)]

Slide 9: Common List Pitfalls
- Modifying list while iterating (use list[:])
- .sort() returns None (use sorted() for return value)
- Shallow copy issue with nested lists
- Code examples showing each pitfall

Slide 10: Tuples — Immutable Ordered Collections
- Syntax: (1, 2, 3) or 1, 2, 3 (packing)
- Ordered, immutable, allows duplicates
- Use for fixed records (coordinates, database rows)
- Code example: point = (3, 4)

Slide 11: Tuple Unpacking
- Extracting values: x, y = point
- Swapping: a, b = b, a
- Using * to capture rest: first, *rest = tuple
- Code example showing each pattern

Slide 12: When to Use Lists vs Tuples
- List: collection will grow/shrink, same type items
- Tuple: fixed size, different types, data integrity
- Tuples can be dict keys; lists cannot
- Visual: decision tree diagram

Slide 13: Dictionaries — Key-Value Mapping
- Syntax: {"name": "Alice", "age": 30}
- Unordered (Python 3.7+ preserves insertion order)
- Keys must be immutable (str, int, tuple)
- Code example: contact dictionary

Slide 14: Accessing and Modifying Dicts
- Direct access: dict["key"] (raises KeyError if missing)
- Safe access: dict.get("key", default)
- Adding/updating: dict["new_key"] = value
- Code example showing each method

Slide 15: Iterating Over Dicts
- .keys() — iterate over keys
- .values() — iterate over values
- .items() — iterate over (key, value) pairs
- Code example: for k, v in dict.items()

Slide 16: Nested Dictionaries
- Dict of dicts (common pattern)
- Example: contacts = {"alice": {"phone": "...", "email": "..."}}
- Accessing nested values: contacts["alice"]["phone"]
- Code example: multi-level structure

Slide 17: Sets — Unique Unordered Collections
- Syntax: {1, 2, 3} or set([1, 2, 2]) → {1, 2}
- No duplicates, no indexing
- Fast membership testing (in operator)
- Code example: deduplicating a list

Slide 18: Set Operations
- union (|): items in either set
- intersection (&): items in both sets
- difference (-): items in first but not second
- Visual: Venn diagram showing operations

Slide 19: Choosing the Right Data Structure
- List: ordered, mutable, duplicates OK
- Tuple: ordered, immutable, fixed structure
- Dict: key-value mapping, fast lookup
- Set: unique items, set algebra
- Visual: decision flowchart

Slide 20: Week 2 Recap & Next Steps
- What we covered: lists, tuples, dicts, sets
- Weekend project: Contact Book Manager
- Next week: Functions, file I/O, exceptions
- Common pitfall preview: mutable default arguments

VISUAL DESIGN REQUIREMENTS:
- Use the same MIT-style theme from Week 1 (consistency)
- Code blocks: monospace font, syntax highlighting
- Diagrams: Venn diagrams for sets, index diagrams for lists/tuples
- Data structure comparison tables where relevant
- No walls of text — max 5 bullet points per slide
- Each code example should be runnable
- Include memory/reference diagrams where helpful

OUTPUT FORMAT: PowerPoint (.pptx) or Google Slides link
```

---

## Notes on Using These Prompts

1. **Recommended AI Tools:**
   - **GPT-4 (ChatGPT Plus):** Best for detailed content generation
   - **Claude 3.5 Sonnet:** Excellent for technical accuracy and code examples
   - **Gamma.app:** AI-powered presentation builder (paste prompt, generates slides directly)
   - **Beautiful.ai:** AI-assisted slide design with templates

2. **After Generation:**
   - Review all code examples for correctness
   - Test each code snippet in Python REPL
   - Add your own live-coding demos
   - Adjust timing (20 slides ≈ 60-75 min with demos)

3. **Customization:**
   - Replace "MIT Kathmandu" with your actual institution
   - Adjust difficulty based on your students' pace
   - Add/remove slides as needed for your 90-minute sessions

4. **Converting Jupyter Notebooks to Slides:**
   If using the GitHub resources above, you can convert notebooks to slides:
   ```bash
   jupyter nbconvert notebook.ipynb --to slides --post serve
   ```

---

## Additional Resources

- **Canva Education:** Free Pro account for educators (has Python-themed templates)
- **SlidesCarnival:** Free PowerPoint/Google Slides templates
- **Python.org:** Official Python tutorial (can extract diagrams)
- **Real Python:** High-quality Python tutorials (some have accompanying slides)
