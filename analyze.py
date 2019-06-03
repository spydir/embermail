import json
import os
import itertools
import re
import auth
import input_validation

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

def download_emails(folder):
    session, username = auth.password()
    emails = session.all_mail().mail()



    for email in emails:


        writefile = folder+username + "_"+ email.uid +'.json'
        f = open(writefile, "w")
        email.fetch()
        print email.uid, input_validation.subject(email.subject)
        email_details = proccess_email(email.uid,email.sent_at,email.fr,email.to,email.subject,email.labels)
        f.write(email_details)
        f.close()

    session.logout()

    return emails