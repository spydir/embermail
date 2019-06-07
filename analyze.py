import json, itertools, re
from utils.files import read_dir,print_files
from utils import input_validation
from jsondiff import diff


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


def print_values(values, number):
    for i in sort_values(values)[:number]:
        print i


def analyze(dir):
    roots,files,paths = read_dir(dir)
    senders = get_values(paths,'sender')
    subjects = get_values(paths, 'subject')
    print_values(senders,10)


def proccess_email(uid,time,sender,to,subject,labels,flags):
    # print uid,input_validation.to(to)

    email_details = '{"uid":"' + uid + \
                    '","time":"' + input_validation.time(time) + \
                    '","sender":"' + input_validation.sender(sender) + \
                    '","to":[' + input_validation.to(to) + ']' + \
                    ',"subject":"' + input_validation.subject(subject) + \
                    '","labels":[' + input_validation.labels(labels, flags) + ']}'

    return email_details


def comapare_dirs(dir1,dir2):
    roots1, files1, paths1 = read_dir(dir1)
    roots2, files2, paths2 = read_dir(dir2)

    for i in list(set(files1)&set(files2)):
        string1 = roots1[0] + '/' + i
        string2 = roots2[0] + '/' + i
        print email_diff(string1, string2)


def email_diff(email1, email2):

    e1 = open(email1,'r')
    e2 = open(email2,'r')


    difference = diff(json.loads(e1.read()), json.loads(e2.read()))

    return difference