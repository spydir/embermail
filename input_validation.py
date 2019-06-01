import re

def sender(email_sender):
    sender_list = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email_sender)
    sender = sender_list[0]

    return sender

def subject(email_subject):
    subject_unicode = unicode(email_subject)
    subject_ascii = subject_unicode.encode('utf8', 'replace')
    subject = re.sub('[\\"+\n\r]', '', subject_ascii)

    return subject

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

