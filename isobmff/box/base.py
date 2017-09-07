# -*- coding: utf-8 -*-
from collections import OrderedDict

class FieldMeta(type):
    def __new__(cls, name, bases, namespace):#*args, **kwargs
        return type.__new__(cls, name, bases, namespace)


class Field(metaclass=FieldMeta):
    def __init__(self, size=None):
        if size:
            self.size = size // 8 # bit to byte
        self.value = None

    def __get__(self, instance, owner=None):
        if instance:
            return self.value
        else:
            return self
    
    def __set__(self, instance, value):
        if instance:
            self.value = value
        else:
            pass

    def read(self, file):
        pass

    def write(self, file):
        pass

class BoxMeta(type):
    box_list = {}

    @classmethod
    def __prepare__(cls, name, bases, *, boxtype=None):
        return OrderedDict()

    def __new__(cls, name, bases, namespace, *, boxtype=None):
        clsobj = type.__new__(cls, name, bases, dict(namespace))
        fields = ((k, v) for k, v in namespace.items() if isinstance(v, Field))
        clsobj.fields = OrderedDict(fields)
        if boxtype:
            cls.box_list[boxtype] = clsobj
        return clsobj

    def __init__(self, name, bases, namespace, *, boxtype=None):
        super().__init__(name, bases, namespace)

class BoxIO(metaclass=BoxMeta):
    def read(self, file):
        for name, field in self.fields.items():
            field.read(file)
            print(name)
