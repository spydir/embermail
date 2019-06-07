import json, os, itertools, re, auth, input_validation, files


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
    files = read_dir(dir)
    senders = get_values(files,'sender')
    subjects = get_values(files, 'subject')
    print_values(senders,10)

def proccess_email(uid,time,sender,to,subject,labels):
    # print uid,input_validation.to(to)

    email_details = '{"uid":"' + uid + \
                    '","time":"' + input_validation.time(time) + \
                    '","sender":"' + input_validation.sender(sender) + \
                    '","to":[' + input_validation.to(to) + ']' + \
                    ',"subject":"' + input_validation.subject(subject) + \
                    '","labels":[' + input_validation.labels(labels)+ ']}'

    return email_details

