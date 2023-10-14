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

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        seralized_obj = {}
        for key, obj in self.__objects.items():
            seralized_obj[key] = obj.to_dict()
        with open(__file_path, 'w', encdoing='utf-8') as file_json:
            json.dump(seralized_obj, file_json)
    
    def relod(self):
        """ deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file_json:
                data = file_json.read()
                try:
                    self.__objects = json.load(data)
                except json.JSONDecodeError:
                    self__.objects = {}

