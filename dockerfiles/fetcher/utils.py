import os
from os import makedirs
from os.path import join, isdir, abspath, basename, dirname
import shutil
import json
import yaml

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

def make_empty_dir(path):
    # Check if the directory exists
    if isdir(path):
        # Remove all contents of the directory
        shutil.rmtree(path)
    # Create the directory
    os.makedirs(path, exist_ok=True)

def move_to_parent(dir_path):
    # Ensure the directory exists
    if not isdir(dir_path):
        print(f"Directory does not exist: {dir_path}")
        return

    parent_dir = dirname(dir_path)  # Get the parent directory

    # Move each item in the directory to the parent directory
    for item in os.listdir(dir_path):
        src_path = join(dir_path, item)
        dst_path = join(parent_dir, item)

        # Move the item to the parent directory
        shutil.move(src_path, dst_path)

    # Remove the now empty directory
    os.rmdir(dir_path)
    print(f"Moved contents and removed directory: {dir_path}")
