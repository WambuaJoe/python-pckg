#!/usr/bin/env python3

import cmd

class HelloWorld(cmd.Cmd):
    """ simple command processor """
    MABONZO = ['sean', 'kelly', 'mutua', 'mwangi', 'ian', 'nate']

    def do_greet(self, person):
        """ greet [person] """
        name_variable = 'Joe'
        if person and person in self.MABONZO:
            greeting = f'niaje we matako, {person.title()}'
        elif person:
            greeting = f'niaje, {person.title()}'
        else:
            greeting = 'niaje'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completions = self.MABONZO[:]
        else:
            completions = [ f for f in self.MABONZO if f.startswith(text)]
        return completions

    # def help_greet(self):
    #     print('\n'.join([
    #         'greet [person]',
    #         'greet the named person (arg)',
    #     ]))

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()

if __name__ == "__main__":
    HelloWorld().cmdloop()

