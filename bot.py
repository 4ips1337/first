
contacts = {}


def hello():
    return "How can I help you?"


def add_contact(*args):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Error: command format should be 'add <name> <phone number>'"


def change_contact(*args):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return f"Error: contact {name} not found."
    else:
        return "Error: command format should be 'change <name> <new phone number>'"


def show_phone(*args):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f"Error: contact {name} not found."
    else:
        return "Error: command format should be 'phone <name>'"


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
            print(add_contact(*args))
        
        elif command == "change":
            print(change_contact(*args))
        
        elif command == "phone":
            print(show_phone(*args))
        
        elif command == "all":
            print(show_all_contacts())
        
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()