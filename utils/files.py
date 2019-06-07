import os, time


def read_dir(dirname):

    roots_list = []
    files_list = []
    paths_list = []

    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".json"):
                roots_list.append(root)
                files_list.append(file)
                paths_list.append(root + "/" + file)

    return roots_list, files_list, paths_list


def write_dir(dirname):

    timestr = time.strftime("%Y%m%d-%H%M%S")
    directory = dirname + timestr + "/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory


def print_files(files):
    for file in files:
        print file