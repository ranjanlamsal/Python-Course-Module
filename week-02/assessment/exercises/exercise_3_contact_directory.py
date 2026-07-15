"""
Exercise 3: Small Contact Directory
Practice: dictionaries, .get(), iteration with .items()

This introduces the same structure you'll use in the Contact Book project:
contacts stored as a dictionary of name -> phone number.

Task:
1. Create an empty dictionary called contacts.
2. Ask the user for a name and phone number repeatedly.
3. Stop when the user enters "done" for the name.
4. Use .get() to check whether the contact already exists.
5. Print all stored contacts once the loop finishes.

Example interaction:
Name: Alice
Phone: 555-1111
Name: Bob
Phone: 555-2222
Name: done

Expected output idea:
Alice: 555-1111
Bob: 555-2222
"""


def main():
    contacts = {}

    # TODO 1: Ask the user for a name and phone until they enter "done"
    # The loop should stop when the name is "done" (case-insensitive if you want)

    # TODO 2: Use contacts.get(name) to safely check if a name already exists
    # If it exists, print a message such as "Contact already exists"
    # Otherwise, add it to the dictionary

    # TODO 3: Print all contacts using .items()
    # Example format: Alice: 555-1111

    pass


if __name__ == "__main__":
    main()
