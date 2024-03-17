def parse_input(user_input):
    """Розбирає введений рядок на команду та її аргументи."""
    parts = user_input.strip().split(maxsplit=2)
    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return command, args

def add_contact(contacts, args):
    """Додає новий контакт."""
    if len(args) == 2:
        name, phone = args
        contacts[name.lower()] = phone
        print("Contact added.")
    else:
        print("Error: add command requires a name and a phone number.")

def change_contact(contacts, args):
    """Змінює номер існуючого контакту."""
    if len(args) == 2:
        name, phone = args
        if name.lower() in contacts:
            contacts[name.lower()] = phone
            print("Contact updated.")
        else:
            print("Error: contact not found.")
    else:
        print("Error: change command requires a name and a new phone number.")

def show_phone(contacts, args):
    """Виводить номер телефону за іменем контакту."""
    if len(args) == 1:
        name = args[0]
        if name.lower() in contacts:
            print(contacts[name.lower()])
        else:
            print("Error: contact not found.")
    else:
        print("Error: phone command requires a name.")

def show_all(contacts):
    """Виводить усі збережені контакти з номерами телефонів."""
    if contacts:
        for name, phone in contacts.items():
            print(f"{name.title()}: {phone}")
    else:
        print("No contacts stored.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")  # Вітальне повідомлення при запуску
    command_handlers = {
        "hello": lambda _, __: print("How can I help you?"),
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": lambda _, __: show_all(contacts),
        "close": lambda _, __: exit("Good bye!"),  # Вихід з програми з повідомленням
        "exit": lambda _, __: exit("Good bye!")
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in command_handlers:
            command_handlers[command](contacts, args)
        else:
            print("Invalid command.")  # Змінено текст повідомлення про невідому команду

if __name__ == "__main__":
    main()
