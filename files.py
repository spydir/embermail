import os

def read_dir(dir):

    file_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".json"):
                file_list.append(root+"/"+file)

    return file_list

def write_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    return dir

def print_files(files):
    for file in files:
        print file