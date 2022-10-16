import json
import os
from pathlib import Path

folder_path = os.path.join(Path(__file__).parent, "data")
path  = folder_path+'/posts.json'

def setup():
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    if not os.path.exists(path):
        with open(path, 'w') as file:
            json.dump([], file)

def read_db():
    with open(path, 'r') as file:
        return json.load(file)

def write_db(data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=True)

def create_post(title:str, paras:list):
    data = read_db()
    data.append({
        'title': title,
        'body':paras
    })
    write_db(data)

