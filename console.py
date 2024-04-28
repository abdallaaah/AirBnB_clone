#!/usr/bin/python3
"""Command interpreter for the HBNB project"""
import cmd
from models import base_model
from models import storage
class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with Ctrl+D (EOF)"""
        return True
    def do_create(self, arg):
        """Create instance"""
        if not arg:
            print('** class name missing **')
        else:
            if hasattr(base_model, arg):
                print(arg)
                obj = base_model.BaseModel()
                print(obj.id)
            else:
                print('** class doesn\'t exist **')

    def do_show(self, *arg):
        """Show instance by it's id"""
        input = arg[0].split()
        if len(input) == 0:
            print('** class name missing **')
        else:
            if input:
                if not hasattr(base_model, input[0]):
                    print(' ** class doesn\'t exist **')
                else:
                    if len(input) < 2:
                        print('** instance id missing **')
                    else:
                        obj_search = input[1]
                        obj_search = ('BaseModel.') + str(obj_search)
                        all_objects = storage.all()
                        if obj_search in all_objects:
                            print(base_model.BaseModel(obj_search))
                        else:
                            print('** no instance found **')

    def do_destroy(self, *arg):
        """Delete instance from the json file"""
        input = arg[0].split()
        if len(input) == 0:
            print('** class name missing **')
        else:
            if input:
                if not hasattr(base_model, input[0]):
                    print(' ** class doesn\'t exist **')
                else:
                    if len(input) < 2:
                        print('** instance id missing **')
                    else:
                        obj_search = input[1]
                        obj_search = ('BaseModel.') + str(obj_search)
                        all_objects = storage.all()
                        if obj_search in all_objects:
                            all_objects.pop(obj_search)
                        else:
                            print('** no instance found **')


    def do_all(self, line):
        """Prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')
            if not hasattr(base_model, words[0]):
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items() if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, *args):
        """update instance based on id"""
        words = args[0].split()
        if len(words) == 0:
            print('** class name missing **')
        elif len(words) < 2:
            print('** instance id missing **')
        elif len(words) < 3:
            print('** attribute name missing **')
        elif len(words) < 4:
            print('** value missing **')
        else:
            class_name = words[0]
            instance_id = words[1]

            # Check if the class exists
            if not hasattr(base_model, class_name):
                print("** class doesn't exist **")
                return

            # Construct the object search key
            obj_search = f"{class_name}.{instance_id}"
            all_objects = storage.all()

            # Check if the object exists
            if obj_search in all_objects:
                # Create a new instance of the class with the provided ID
                obj = getattr(base_model, class_name)(id=instance_id)

                # Construct the kwargs dynamically
                kwargs = {'id': obj.id}
                for i in range(3, len(words), 2):
                    kwargs[words[i - 1]] = words[i]

                # Create a new instance with updated attributes
                updated_obj = getattr(base_model, class_name)(**kwargs)
                updated_obj.save()
                storage.save()

                print('update')
                print(updated_obj)
                print(storage.all())
            else:
                print('** no instance found **')

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
