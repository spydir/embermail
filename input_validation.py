import re

def sender(email_sender):
    sender_list = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email_sender)
    sender = sender_list[0]

    return sender

def labels(email_labels):
    labels = ""

    for label in email_labels:
        if label != None:
            if label != email_labels[-1]:
                labels = labels + '"' + label + '"' + ","
            if label == email_labels[-1]:
                labels = labels + '"' + label + '"'

    return labels

def subject(email_subject):
    subject_unicode = unicode(email_subject)
    subject = subject_unicode.encode('utf8', 'replace')
    return subject