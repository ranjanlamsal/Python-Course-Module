# Project 2 — Contact Book Manager

**Goal:** Build a console application that manages a contact book using nested dictionaries, with search, update, and delete functionality.

---

## Requirements

### Core Features (Minimum Viable Product)

Your program must:

1. **Store contacts as a dictionary of dictionaries:**
   ```python
   contacts = {
       "alice": {
           "name": "Alice Smith",
           "phone": "555-1234",
           "email": "alice@example.com",
           "tags": ["work", "urgent"]
       },
       "bob": {
           "name": "Bob Johnson",
           "phone": "555-5678",
           "email": "bob@example.com",
           "tags": ["friend"]
       }
   }
   ```
   Use lowercase keys for lookup (e.g., `"alice"` maps to the full contact record).

2. **Display a menu** with these options:
   - Add a new contact
   - Search for a contact by name (case-insensitive)
   - Update an existing contact's phone or email
   - Delete a contact
   - List all contacts
   - Exit

3. **Add a contact:**
   - Prompt for name, phone, email, and tags (optional, comma-separated)
   - Check if the contact already exists (case-insensitive) — if so, ask if they want to overwrite
   - Store it in the `contacts` dict with a lowercase key (e.g., `"alice"` for "Alice Smith")

4. **Search for a contact:**
   - Prompt for a name
   - Look it up case-insensitively (convert input to lowercase before checking)
   - If found, display all fields (name, phone, email, tags)
   - If not found, show "Contact not found"

5. **Update a contact:**
   - Prompt for the name to update
   - If found, ask which field to update (phone or email)
   - Update the field and confirm

6. **Delete a contact:**
   - Prompt for the name to delete
   - If found, confirm deletion
   - Remove from the dict

7. **List all contacts:**
   - Print all contacts in a readable format (name, phone, email, tags)
   - If no contacts exist, print "No contacts stored"

8. **Exit:**
   - Print a goodbye message and break the loop

### Input Validation

- If the user enters an invalid menu choice, print an error and show the menu again
- Handle empty inputs gracefully (don't crash)

---

## Constraints & Rules

- **No file I/O yet** — data only exists while the program runs (we'll add persistence in Week 3)
- **Use `.get()` for safe dict access** when you're not sure a key exists
- **Use `.lower()` for case-insensitive search** — don't rely on exact case matching
- **Use a `while True` loop with `break` on "Exit"** — same pattern as the ATM project

---

## Example Run

```
=== Contact Book Manager ===
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. List all contacts
6. Exit

Choose an option: 1
Name: Alice Smith
Phone: 555-1234
Email: alice@example.com
Tags (comma-separated, or leave blank): work, urgent
Contact added successfully!

Choose an option: 2
Search name: alice
--- Contact Found ---
Name: Alice Smith
Phone: 555-1234
Email: alice@example.com
Tags: work, urgent

Choose an option: 5
--- All Contacts ---
1. Alice Smith | 555-1234 | alice@example.com | Tags: work, urgent

Choose an option: 6
Goodbye!
```

---

## Deliverable

- **File:** `contact_book.py` in the `week-02/assessment/project/` folder
- **Commit message:** `"feat: complete Contact Book Manager project"`
- **Test it end-to-end** before submitting — make sure all menu options work

---

## Tips

- Start with the menu loop first (print options and capture input)
- Implement "Add" and "List all" before the other features (they're the easiest)
- Use a helper function like `find_contact(name)` to avoid repeating lookup logic
- Don't try to build everything at once — test each feature as you go

---

## Optional Extensions (not required, but good practice)

If you finish early:

- Add a "tag filter" option (list all contacts with a specific tag)
- Sort contacts alphabetically when listing
- Allow bulk delete (delete all contacts with a certain tag)
- Add input validation (e.g., phone number must be digits, email must contain `@`)

See **[Optional Challenges](../challenges/)** for detailed specs on these.
