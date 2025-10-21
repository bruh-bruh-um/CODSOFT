import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(f" Contact {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} | {contact['phone']}")

def search_contact(contacts):
    query = input("Enter name or phone to search: ").lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']} | {contact['address']}")
    else:
        print("No contacts found matching your query.")

def update_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter the number of the contact to update: ")) - 1
    if 0 <= idx < len(contacts):
        contact = contacts[idx]
        print(f"Updating {contact['name']}. Leave blank to keep current value.")
        name = input(f"New name ({contact['name']}): ") or contact['name']
        phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
        email = input(f"New email ({contact['email']}): ") or contact['email']
        address = input(f"New address ({contact['address']}): ") or contact['address']

        contacts[idx] = {"name": name, "phone": phone, "email": email, "address": address}
        save_contacts(contacts)
        print(f" Contact {name} updated successfully!")
    else:
        print("Invalid selection.")

def delete_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= idx < len(contacts):
        contact = contacts.pop(idx)
        save_contacts(contacts)
        print(f" Contact {contact['name']} deleted successfully!")
    else:
        print("Invalid selection.")

def main():
    contacts = load_contacts()
    while True:
        print("\n Contact Book Menu ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select from the menu.")

if __name__ == "__main__":
    main()
