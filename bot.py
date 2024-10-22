contacts = {}


def hello():
    return "How can I help you?"


def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added."


def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Error: contact {name} not found."


def show_phone(name):
    if name in contacts:
        return contacts[name]
    else:
        return f"Error: contact {name} not found."


def show_all_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def main():
    print("Welcome to the assistant bot!")
    
    while True:
        
        user_input = input("Enter command: ").strip()
        command, *args = user_input.split()

        
        command = command.lower()

        
        if command == "hello":
            print(hello())
        
        elif command == "add":
            if len(args) == 2:
                name, phone = args
                print(add_contact(name, phone))
            else:
                print("Error: command format should be 'add <name> <phone number>'")
        
        elif command == "change":
            if len(args) == 2:
                name, new_phone = args
                print(change_contact(name, new_phone))
            else:
                print("Error: command format should be 'change <name> <new phone number>'")
        
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                print(show_phone(name))
            else:
                print("Error: command format should be 'phone <name>'")
        
        elif command == "all":
            print(show_all_contacts())
        
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()