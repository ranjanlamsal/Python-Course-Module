# Week 2 Reflection Log

**Instructions:** Answer these questions *after* you've completed the exercises and the Contact Book Manager project. This is not graded — it's for you to solidify what you learned and identify what's still fuzzy.

---

## 1. Conceptual Understanding

### Lists vs Tuples
**Question:** In your own words, explain when you would use a list vs a tuple. Give one real-world example of each.

**Your answer:**
```
[Write your answer here]
```

### Dictionaries vs Lists
**Question:** Why would you use a dictionary instead of a list to store contact information? What's the specific advantage?

**Your answer:**
```
[Write your answer here]
```

### Sets
**Question:** Describe a scenario from the Contact Book project (or another real-world example) where using a set would be more efficient than a list.

**Your answer:**
```
[Write your answer here]
```

---

## 2. Code Reading

**Given this code:**
```python
contacts = {
    "alice": {"phone": "555-1234", "email": "alice@example.com"},
    "bob": {"phone": "555-5678", "email": "bob@example.com"}
}

name = input("Enter name: ").lower()
phone = contacts[name]["phone"]
print(f"Phone: {phone}")
```

**Question:** What will crash this code? How would you fix it?

**Your answer:**
```
[Write your answer here]
```

---

## 3. Implementation Reflection

### What worked well?
List 2-3 things you implemented successfully in the Contact Book project without needing to look up documentation.

**Your answer:**
```
1. [Example: I successfully used .get() to avoid KeyError when searching]
2. 
3. 
```

### What was hardest?
What concept or feature took the most time to get right? Why do you think it was difficult?

**Your answer:**
```
[Write your answer here]
```

### What would you do differently?
If you were to restart the project from scratch, what would you change about your approach?

**Your answer:**
```
[Write your answer here]
```

---

## 4. Self-Assessment

Rate your confidence (1-5, where 5 = very confident) on each topic:

- [ ] Creating and indexing lists: ___/5
- [ ] List slicing (e.g., `list[1:4]`, `list[::-1]`): ___/5
- [ ] List comprehensions: ___/5
- [ ] Tuple unpacking: ___/5
- [ ] Creating and accessing dictionaries: ___/5
- [ ] Iterating over dicts with `.items()`: ___/5
- [ ] Nested dictionaries: ___/5
- [ ] Using sets for deduplication: ___/5
- [ ] Set operations (union, intersection, difference): ___/5

**For any rating ≤ 3, write one thing you could do this week to improve:**
```
[Write your plan here]
```

---

## 5. Connection to Week 1

**Question:** How did you use Week 1 concepts (loops, conditionals, input validation) in this week's project? Give 2 specific examples.

**Your answer:**
```
1. [Example: I used a while True loop for the menu, just like the ATM project]
2. 
```

---

## 6. Looking Ahead

**Question:** Next week we'll learn functions (breaking code into reusable pieces). Looking at your Contact Book code, what parts do you think would make good functions?

**Your answer:**
```
[Write your answer here]
```

---

**Congratulations on completing Week 2!** Review your answers before Thursday's session — they'll help you participate in the ATM project review.
