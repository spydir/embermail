import json
import os
import itertools
import re

def read_dir(dir):

    file_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".json"):
                file_list.append(root+"/"+file)

    return file_list

def print_files(files):
    for file in files:
        print file

def get_values(files,key):
    list = []

    for file in files:
        f = open(file,'r')
        string = re.sub(r"[^a-zA-Z0-9{}\"\',:\[\]!@#$%^&*()-_=+;<>?/]+",' ', f.read())
        try:
            parsed_json = json.loads(string)
            list.append(parsed_json[key])
        except ValueError:
            print ValueError, file

    return list

def sort_values(values):
    values_list = []
    for key, value in itertools.groupby(sorted(values)):
        item = len(list(value)), key
        values_list.append(item)

    sorted_values = sorted(values_list,reverse=True)
    return sorted_values

def analyze(dir):
    files = read_dir(dir)
    senders = get_values(files,'sender')
    subjects = get_values(files, 'subject')

    print sort_values(senders)

