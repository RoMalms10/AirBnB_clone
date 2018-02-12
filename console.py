#!/usr/bin/env python3
""" My cmd module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNB command line interpreter """

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exit when EOF happens """
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Do nothing if empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
