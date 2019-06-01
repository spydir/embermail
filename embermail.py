import auth
import input_validation

def proccess_email(uid,time,sender,to,subject,labels):
    print uid,input_validation.to(to)

    email_details = '{"uid":"' + uid + \
                    '","time":"' + input_validation.time(time) + \
                    '","sender":"' + input_validation.sender(sender) + \
                    '","to":[' + input_validation.to(to) + ']' + \
                    ',"subject":"' + input_validation.subject(subject) + \
                    '","labels":[' + input_validation.labels(labels)+ ']}'

    return email_details

def download_emails():
    session, username = auth.password()
    emails = session.all_mail().mail()



    for email in emails:
        writefile = "emails/"+username + "_"+ email.uid +'.json'
        f = open(writefile, "w")
        email.fetch()
        email_details = proccess_email(email.uid,email.sent_at,email.fr,email.to,email.subject,email.labels)
        f.write(email_details)
        f.close()
    session.logout()

    return emails

download_emails()
