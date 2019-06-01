import re

def sender(email_sender):
    sender_list = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email_sender)
    sender = sender_list[0]

    return sender

def to(email_to):

    email_list = ["Null"]
    to_list = ""

    if email_to != None:

        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", str(email_to))
        email_list = sorted(list(set(emails)))

        for email in email_list:
            if email != None:
                if email != email_list[-1]:
                    to_list = to_list + '"' + email + '"' + ","
                if email == email_list[-1]:
                    to_list = to_list + '"' + email + '"'

    return str(to_list).lower()

def subject(email_subject):
    subject_unicode = unicode(email_subject)
    subject_ascii = subject_unicode.encode('utf8', 'replace')
    subject = re.sub('[\\"+\n\r]', '', subject_ascii)

    return subject

def time(email_time):
    time = str(email_time)

    return time

def labels(email_labels):
    labels = ""

    for label in email_labels:
        clean_label = re.sub('[\\\]', '', label)
        if label != None:
            if label != email_labels[-1]:
                labels = labels + '"' + clean_label + '"' + ","
            if label == email_labels[-1]:
                labels = labels + '"' + clean_label + '"'

    return labels

