#!/usr/bin/python3
""" My cmd module """
import cmd
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """ HBNB command line interpreter """

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ Exit when EOF happens """
        print()
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Do nothing if empty line """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it and prints the id """
        if not arg:
            print("** class name missing **")
        elif arg not in models.class_dict:
            print("** class doesn't exist **")
        else:
            a = models.class_dict[arg]()
            models.storage.save()
            print(a.id)

    def do_show(self, arg):
        """ Prints string representation of instance based on name and id """
        arg = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in models.class_dict:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            temp_dict = models.storage.all()
            if key in temp_dict:
                print(temp_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Destroys an instance based off name and id """
        arg = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in models.class_dict:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            temp_dict = models.storage.all()
            if key in temp_dict:
                del temp_dict[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """ Print all instances of a class (or all intances if no class) """
        arg = shlex.split(arg)
        temp_dict = models.storage.all()
        obj_list = []
        if len(arg) == 0:
            for key, value in temp_dict.items():
                obj_list.append(value)
            print(obj_list)
        elif arg[0] not in models.class_dict:
            print("** class doesn't exist **")
        else:
            for key, value in temp_dict.items():
                if arg[0] in key:
                    obj_list.append(value)
            print(obj_list)

    def do_update(self, arg):
        """ Update instance """
        arg = shlex.split(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in models.class_dict:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            temp_dict = models.storage.all()
            if key not in temp_dict:
                print("** no instance found **")
            elif len(arg) == 2:
                print("** attribute name missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                value = temp_dict.get(key)
                setattr(value, arg[2], arg[3])
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
