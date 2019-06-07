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


def comapare_dirs(parentdir):

    proots, pfiles, ppaths = read_dir(parentdir)
    roots = sorted(set(proots))

    print roots[-2],roots[-1]

    roots1, files1, paths1 = read_dir(roots[-2])
    roots2, files2, paths2 = read_dir(roots[-1])

    for i in sorted(set(files1)&set(files2)):
        string1 = roots1[0] + '/' + i
        string2 = roots2[0] + '/' + i


        diff = email_diff(string1, string2)

        if diff != {}:
            print diff


def email_diff(email1, email2):
    difference = {}



    try:
        e1 = json.loads(open(email1, 'r').read())
        e2 = json.loads(open(email2, 'r').read())
        difference = diff(e1, e2, syntax='explicit')
        difference = e1['uid'], difference

    except ValueError:
        print ValueError

    except UnboundLocalError:
        print UnboundLocalError


    return difference