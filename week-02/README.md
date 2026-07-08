# Week 2 — Data Structures: Collections & Mappings

## Why this week matters

You cannot build real programs with isolated variables. **Lists, tuples, dictionaries, and sets** let you organize, search, and transform collections of data efficiently. By Friday you will understand when to reach for each one, and how to nest them to model real-world entities (contacts, transactions, inventory items).

## Objectives — by Friday night you should be able to:

- Add, remove, sort, and slice items in a list without looking at documentation.
- Explain why you would use a tuple instead of a list for a coordinate pair or database row.
- Build a nested dictionary structure to represent an entity with multiple attributes (e.g., a contact with name, phone, email, tags).
- Use `.get()` safely instead of direct key access to avoid `KeyError`.
- Deduplicate a list using a set, and explain why sets cannot contain other lists or dictionaries.
- Iterate over a dictionary's keys, values, or key-value pairs using `.items()`.

## Sessions

| Session | Date | Covers | Handbook |
|---|---|---|---|
| Session 1 (Thu) | **30-min Review: ATM Project** → Lists & Tuples | Review anonymized Week 1 bugs, then: list operations (append, pop, sort, slice), list comprehensions (intro), tuple immutability, unpacking | [`session-1-lists-and-tuples/`](./session-1-lists-and-tuples/) |
| Session 2 (Fri) | Dictionaries & Sets | dict CRUD, `.get()`, `.items()` iteration, nested dicts, set operations (union, intersection, difference), deduplication | [`session-2-dicts-and-sets/`](./session-2-dicts-and-sets/) |

## Weekend assessment

Once both sessions are done, work through **[`assessment/README.md`](./assessment/README.md)** — Saturday through Wednesday. It is not graded. It is the *only* material next Thursday's 30-minute review will be built from, so treat it as required, not optional (the optional part is clearly marked separately inside it).

The project this week is **Contact Book Manager** — a console app where you store, search, edit, and delete contacts using nested dictionaries and list operations.

## Further reading

See **[`references.md`](./references.md)** for the official docs that back every concept taught this week.
