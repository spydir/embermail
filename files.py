import os, time

def read_dir(dirname):

    file_list = []
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".json"):
                file_list.append(root+"/"+file)

    return file_list

def write_dir(dirname):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    directory = dirname + timestr + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory

def print_files(files):
    for file in files:
        print file