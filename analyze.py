import json
import os
import re
import pandas

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

def number_of_subjects(files):
    list = []

    for file in files:
        f = open(file,'r')
        string = re.sub(r"[^a-zA-Z0-9{}\"\',:\[\]!@#$%^&*()-_=+;<>?/]+",' ', f.read())
        try:
            parsed_json = json.loads(string)
            list.append(parsed_json['subject'])
            print parsed_json['subject']
        except ValueError:
            print ValueError, file

    # my_series = pandas.Series(list)
    # count = my_series.value_counts()
    # print len(list)
    # print count


def analyze(dir):
    files = read_dir(dir)
    values = get_values(files,'sender')

    for value in values:
        print value

