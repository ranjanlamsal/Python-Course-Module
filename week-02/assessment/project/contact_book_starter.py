"""
Starter file for the Week 2 Contact Book Manager project.

This file gives you the basic structure for a console-based contact book.
Your job is to implement the menu loop and the contact-management features.

Project goals:
- Store contacts in a dictionary of dictionaries
- Support add, search, update, delete, and list actions
- Use case-insensitive lookup with .lower()
- Use .get() for safe dictionary access
- Keep the program running until the user chooses Exit

Suggested build order:
1. Build the menu loop and exit option first
2. Implement Add Contact and List All Contacts
3. Implement Search Contact
4. Implement Update Contact
5. Implement Delete Contact
6. Test the full flow end-to-end
"""

contacts = {}


def show_menu():
    print("=== Contact Book Manager ===")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. List all contacts")
    print("6. Exit")


def add_contact():
    # TODO 1: Ask for name, phone, email, and optional tags
    # TODO 2: Normalize the contact name to lowercase for the dictionary key
    # TODO 3: Check whether the contact already exists using contacts.get(name)
    # TODO 4: Store the contact as a dictionary containing name, phone, email, and tags
    pass


def search_contact():
    # TODO 5: Ask the user for a name to search
    # TODO 6: Use lowercase normalization and contacts.get() for safe lookup
    # TODO 7: Print the contact details if found, otherwise print "Contact not found"
    pass


def update_contact():
    # TODO 8: Ask for the name to update
    # TODO 9: If found, ask whether to update phone or email
    # TODO 10: Update the chosen field and confirm the change
    pass


def delete_contact():
    # TODO 11: Ask for the name to delete
    # TODO 12: Confirm the deletion before removing the entry
    # TODO 13: Remove the contact from the dictionary
    pass


def list_contacts():
    # TODO 14: Print all contacts in a readable format
    # TODO 15: If no contacts exist, print "No contacts stored"
    pass


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
