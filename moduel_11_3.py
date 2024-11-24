import inspect
from pprint import pprint
import requests


def introspection_info(obj):
    attributes = []
    methods = []
    print(f"Тип объекта: {type(obj)}")
    for atr in dir(obj):
        if callable(getattr(obj, atr)):
            methods.append(atr)
        else:
            attributes.append(atr)
    print(f"Атрибуты объекта: {attributes}")
    print(f"Методы объекта: {methods}")
    print(inspect.getmodule(obj))
    print(inspect.isclass(obj))
    print(inspect.ismodule(obj))
    print(inspect.isfunction(obj))
    print(inspect.ismethod(obj))
    print(inspect.istraceback(obj))

introspection_info(requests)