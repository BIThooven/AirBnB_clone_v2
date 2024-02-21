#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        if not cls:
            return FileStorage.__objects

        class_name = cls.__name__
        objs = {}
        for k, v in FileStorage.__objects.items():
            if class_name in k:
                objs[k] = v
        return objs

    def new(self, obj):
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        if not obj:
            return

        for k, v in FileStorage.__objects.items():
            if v == obj:
                del FileStorage.__objects[k]
                return

    def reload(self):
        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        self.reload()
