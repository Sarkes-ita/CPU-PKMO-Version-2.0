import json


def load_types(path="data/types.json"):
    with open(path, "r") as f:
        return json.load(f) #it becomes a python object, in this case a dict