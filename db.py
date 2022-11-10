import json
import os
from pathlib import Path

path = os.path.join(Path(__file__).parent, 'data') + '/'

def init():
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(path+'data.json'):
        with open(path+'data.json', 'w') as file:
            json.dump([], file)

def readDb():
    with open(path + 'data.json', 'r') as file:
        return json.load(file)

def writeDb(data):
    with open(path + 'data.json', 'w') as file:
        json.dump(data, file, indent=True)

def addPost(title:str, date:str, body:list):
    Dict = {
        'title': title,
        'date': date,
        'body':body
    }

    data = readDb()
    data.append(Dict)
    writeDb(data)

def deletePost(title:str):
    data = readDb()
    for i in data:
        if i['title'] == title:
            del data[data.index(i)]
    writeDb(data)

init()