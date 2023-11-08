#!/usr/bin/python3
import cmd


class MyConsole(cmd.Cmd):
    """ replicate a command line interpreter """
    intro = "AirBnB command line intepreter.\nType 'help' or ? to list commands\n"
    prompt = "(getsuga) "

    def do_create(self, line):
        """ create anything """
        print("created ", line)

    def do_EOF(self, line):
        """ exit program using Ctrl-D """
        print("Exiting console")
        return True

    def do_multiply(self, args):
        """ multiply 2 numbers """
        try:
            a, b = map(float, args.split())
            result = a * b
            print(f"Mutliplication returns {result:.4f}")
        except Exception as err:
            error_name = type(err).__name__ 
            print("Invalid input: Usage: multiply <num1> <num2>")
            print(f"[{error_name}]: {err}")

if __name__ == "__main__":
    MyConsole().cmdloop()
