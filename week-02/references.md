# Week 2 — Official References & Further Reading

This page links directly to the authoritative Python documentation for every concept taught this week. Use these when the handbook explanations aren't enough, or when you need to see the full method signatures and edge cases.

## Lists

- **[Python Tutorial — Data Structures (Lists)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)**  
  The official guide to list methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `count()`, `index()`.

- **[List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)**  
  The Pythonic way to transform and filter lists in a single line.

- **[Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)**  
  Covers slicing (`[start:stop:step]`), `len()`, `min()`, `max()`, `in` operator, concatenation with `+`.

## Tuples

- **[Python Tutorial — Tuples and Sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)**  
  Why tuples exist, immutability guarantees, tuple packing and unpacking.

- **[Tuple Objects Reference](https://docs.python.org/3/library/stdtypes.html#tuples)**  
  The two tuple methods (`count()` and `index()`), and why there aren't more.

## Dictionaries

- **[Python Tutorial — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)**  
  Creating dicts, accessing values, iterating with `.keys()`, `.values()`, `.items()`.

- **[Mapping Types — dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)**  
  The full dict API: `.get()`, `.setdefault()`, `.update()`, `.pop()`, `.popitem()`, `.clear()`.

- **[PEP 584 — Dictionary Merge & Update Operators](https://peps.python.org/pep-0584/)**  
  Python 3.9+ introduced `|` and `|=` for merging dicts — modern and readable.

## Sets

- **[Python Tutorial — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)**  
  Set basics, eliminating duplicates, membership testing.

- **[Set Types — set, frozenset](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)**  
  The full set API: `.add()`, `.remove()`, `.discard()`, `.union()`, `.intersection()`, `.difference()`, `.symmetric_difference()`.

- **[Set Operations Visual Guide (Real Python)](https://realpython.com/python-sets/)**  
  A non-official but excellent visual reference for understanding set algebra.

## List vs Tuple vs Dict vs Set — When to Use What

- **[Choosing the Right Data Structure (Real Python)](https://realpython.com/python-data-structures/)**  
  A decision tree for picking the right collection type based on your use case.

## General Collection Advice

- **[Common Built-in Functions](https://docs.python.org/3/library/functions.html)**  
  `len()`, `sorted()`, `enumerate()`, `zip()`, `any()`, `all()` — these work on all collection types.

- **[Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)**  
  The official guide to `sorted()` and the `key=` parameter for custom sort orders.

## Style & Conventions

- **[PEP 8 — Naming Conventions](https://pep8.org/#naming-conventions)**  
  Still relevant: use `snake_case` for variable names, even when they hold collections.

---

**When to use these:** If you're stuck on a self-check or an assessment exercise and re-reading the handbook module isn't enough, come here and click through to the matching topic. If the official docs are too dense, try the Real Python links first — they're written for learners.
