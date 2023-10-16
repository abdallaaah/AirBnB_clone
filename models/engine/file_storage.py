#!/usr/bin/python3
""" the file engine to seralize and desirlaze """
import json
import os


class FileStorge():
    """ class with private attributes and seralize and de"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj.__class__.__name__
        class_id = obj.id
        key = f"{class_name}.{class_id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w', encoding='utf-8') as file_json:
            json.dump(self.__objects, file_json, default=lambda obj: obj.to_dict())
    
    def reload(self):
        """ deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file_json:
                data = file_json.read()
                try:
                    self.__objects = json.loads(data)
                except json.JSONDecodeError:
                    print("error from expected")
                    self.__objects = {}

