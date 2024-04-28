import sys

def parse_input(user_input):
    # Парсер команд - розбивка і приведення до регістру - пробіл як розділювач
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(contacts, name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Номер телефону оновлено.")
    else:
        print(f"Контакт з ім'ям '{name}' не знайдено.")

def show_phone(contacts, name):
    if name in contacts:
        print(f"Номер телефону '{name}': {contacts[name]}")
    else:
        print(f"Контакт з ім'ям '{name}' не знайдено.")

def show_all_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Записник контактів порожній.")

def main():
    contacts = {}
    print("Welcome to the assistant bot! Введіть HELLO щоб розпочати роботу з Ботом")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "exit" or command == "close":
            print("Good bye!")
            sys.exit()
        elif command == "hello":
            print("How can I help you?\n Add Name Phone \n Change Name Phone \n Phone Name \n All \n Exit - Close \n")
        elif command == "add":
            if len(args) != 2:
                print("Неправильний формат- Використовуйте: add [ім'я] [номер телефону]")
            else:
                name, phone = args
                add_contact(contacts, name, phone)
        elif command == "change":
            if len(args) != 2:
                print("Неправильний формат - Використовуйте: change [ім'я] [новий номер телефону]")
            else:
                name, new_phone = args
                change_contact(contacts, name, new_phone)
        elif command == "phone":
            if len(args) != 1:
                print("Неправильний формат - Використовуйте: phone [ім'я]")
            else:
                name = args[0]
                show_phone(contacts, name)
        elif command == "all":
            show_all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()