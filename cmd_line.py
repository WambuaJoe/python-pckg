#!/usr/bin/env python3

import cmd

class HelloWorld(cmd.Cmd):
    """ simple command processor """
    # MABONZO = ['sean', 'kelly', 'mutua', 'mwangi', 'ian', 'nate']

    # def do_greet(self, person):
    #     """ greet [person] """
    #     if person.lower and person.lower in self.MABONZO:
    #         greeting = f'{person.title()}, niaje we matako'
    #     elif person:
    #         greeting = f'{person.title()}, niaje'
    #     else:
    #         greeting = 'niaje'
    #     print(greeting)

    # def complete_greet(self, text, line, begidx, endidx):
    #     if not text:
    #         completions = self.MABONZO[:]
    #     else:
    #         completions = [ f for f in self.MABONZO if f.startswith(text)]
    #     return completions

    # def help_greet(self):
    #     print('\n'.join([
    #         'greet [person]',
    #         'greet the named person (arg)',
    #     ]))

    prompt = 'prompt: '
    intro = 'Simple command processor example.'

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

    ruler = '-'

    def do_prompt(self, line):
        "Change interactive prompt"
        self.prompt = line + ': '

    def do_EOF(self, line):
        return True

    def postloop(self):
        print()

if __name__ == "__main__":
    HelloWorld().cmdloop()

