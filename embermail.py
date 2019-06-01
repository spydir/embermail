import auth
import input_validation

def proccess_email(uid,sender,subject,labels):

    email_details = '{"uid":"' + uid + \
              '","sender":"' + input_validation.sender(sender) + \
              '","subject":"' + input_validation.subject(subject) + \
              '","labels":[' + input_validation.labels(labels) + ']},'

    return email_details

def session():
    session = auth.password()
    emails = session.inbox().mail()

    f = open("inbox.json","w")

    for email in emails:
        email.fetch()
        email_details = proccess_email(email.uid,email.fr,email.subject,email.labels)

        f.write(email_details +"\n")
    f.close()

    session.logout()

    return emails

session()
