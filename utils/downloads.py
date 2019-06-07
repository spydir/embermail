import auth, input_validation
from analyze import proccess_email
from files import write_dir


def mailbox(labels):
    session, username = auth.password()

    if labels == "all_mail":
        return session.all_mail().mail(), username, session

    if labels == "inbox":
        return session.inbox().mail(), username, session

    if labels == "inbox_unread":
        return session.inbox().mail(unread=True), username, session

    if labels == "unread":
        return session.all_mail().mail(unread=True), username, session


def download(dirname, labels):
    emails, username, session = mailbox(labels)
    writedir = write_dir(dirname)

    for email in emails:

        writefile = writedir + username + "_" + email.uid +'.json'
        f = open(writefile, "w")

        try:
            email.fetch()

            print email.uid, input_validation.subject(email.subject), email.gmail.current_mailbox, email.flags

            email_details = proccess_email(email.uid,email.sent_at,email.fr,email.to,email.subject,email.labels,email.flags)
            f.write(email_details)

        except TypeError:
            pass

        f.close()

    session.logout()

    return emails
