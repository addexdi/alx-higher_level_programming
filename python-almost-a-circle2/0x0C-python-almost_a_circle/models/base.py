#!/usr/bin/python3
"""Python module for class Base"""
import json
import csv


class Base:
    """An empty base class template
    Args:
        id(int): can be None else the value given is assigned to id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor function for class Base"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is [] or list_dictionaries is None:
            return []
        string = json.dumps(list_dictionaries)
        return string

    @classmethod
    def save_to_file(cls, list_objs):
        filename = str(cls.__name__) + ".json"
        with open(filename, 'w') as f_obj:
            if list_objs is None:
                filename.write("[]")
            else:
                list_dict = [o.to_dictionary() for o in list_objs]
                json_obj = Base.to_json_string(list_dict)
                f_obj.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Square':
                dummy = cls(100)
            else:
                dummy = cls(100, 100)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f_obj:
                list_obj = Base.from_json_string(f_obj.read())

        except IOError:
            return []
        finally:
            return [cls.create(**o) for o in list_obj]


if __name__ == "__main__":
    from rectangle import Rectangle
    from square import Square
