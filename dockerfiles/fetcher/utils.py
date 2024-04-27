import json
import yaml
from os import makedirs
from os.path import dirname
from datetime import timedelta

def load_yaml(fileName):
    with open(fileName, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return

def load_json(fileName):
    return json.load(open(fileName,encoding='utf-8'))

def save_json(data,fileName):
    path = dirname(fileName)
    makedirs(path, exist_ok=True)
    jfile = open(fileName, "w")
    jfile.write(json.dumps(data, indent=4))
    jfile.close()
    return

def save_text(data,fileName):
    path = dirname(fileName)
    makedirs(path, exist_ok=True)
    jfile = open(fileName, "w")
    jfile.write(data)
    jfile.close()
    return
