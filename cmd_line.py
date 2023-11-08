#!/usr/bin/python3
import cmd
import time


class AddressBook(cmd.Cmd):
    """ create an address book """
    timestamp = time.time()
    current = time.ctime(timestamp)
    intro = f'Address Book console (main, {current})'
    prompt = '(AddBook)> '

    def __init__(self):
        super().__init__()
        self.contacts = {}

    def do_add(self, args):
        """ add a new contact\n Usage:\n\t<name> <phone>
        """
        name, phone = args.split()
        if name not in self.contacts:
            self.contacts[name] = phone
            print(f"Contact added: {name.title()} - {phone}")
        else:
            print(f"Contact {name.title()} already exists.\nUse 'update' to change contact details")

    def do_read(self, args):
        """ read all contacts """
        if not self.contacts:
            print("Contact not found")
        else:
            message = 'Stored contacts'
            print(f"{message}")
            for a in range(len(message)):
                print("-", end='')
            print()
            for name, phone in self.contacts.items():
                print(f"-> {name.title()} - {phone}")

    def do_update(self, args):
        """ update contact number\n Usage:\n\tupdate <name> <new_phone>
        """
        name, new_phone = args.split()
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"Contact update: {name.title()} - {new_phone}")
        else:
            print(f"{name.title()} not found in contacts.\nUse 'add' to create new contact")

    def do_delete(self, args):
        """ delete a contact\n Usage:\n\tdelete <name>
        """
        name = args
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact deleted: {name}")
        else:
            print(f"{name} not found in contacts.\nUse 'add' to create a new contact")

    def do_EOF(self, args):
        """ exit the program """
        print("Exiting the program...")
        return True


if __name__ == '__main__':
    AddressBook().cmdloop()
