import auth
import input_validation

def proccess_email(uid,sender,subject,labels):

    email_details = '{"uid":"' + uid + \
                    '","sender":"' + input_validation.sender(sender) + \
                    '","subject":"' + input_validation.subject(subject) + \
                    '","labels":[' + input_validation.labels(labels) + ']}'

    return email_details

def download_emails():
    session, username = auth.password()
    emails = session.all_mail().mail()



    for email in emails:
        writefile = "emails/"+username + "_"+ email.uid +'.json'
        f = open(writefile, "w")
        email.fetch()
        email_details = proccess_email(email.uid,email.fr,email.subject,email.labels)
        f.write(email_details +"\n")
        f.close()
    session.logout()

    return emails

download_emails()
