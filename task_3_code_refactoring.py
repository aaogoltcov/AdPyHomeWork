import smtplib
import imaplib


class GMail:
    def __init__(self, email, password, subject=None, recipients=None, message=None, header=None):
        self.send_email_smtp = smtplib.SMTP("smtp.gmail.com", 587)
        self.get_email_imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.email = email
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.header = header
        self.message = message

    def send_email(self):
        print("Starting to send e-mail...")
        self.send_email_smtp.starttls()
        self.send_email_smtp.login(self.email, self.password)
        self.send_email_smtp.sendmail(from_addr=self.email, to_addrs=self.recipients,
                                      msg='Subject: {}\n\n{}'.format(self.subject, self.message))
        self.send_email_smtp.quit()
        print("E-mail was sent.")

    def get_emails(self):
        print("Starting to get e-mails...")
        self.get_email_imap.login(self.email, self.password)
        self.get_email_imap.select(mailbox="inbox")
        response, data = self.get_email_imap.search(None,
                                                    '(HEADER Subject "%s")' % self.header if self.header else 'ALL')
        if data[0]:
            for mail in data[0].split():
                response, data = self.get_email_imap.fetch(mail, '(RFC822)')
                if data[0][1]:
                    print("There are e-mail:")
                    print('Message %s\n%s\n' % (mail, data[0][1].decode("utf-8")))
        else:
            print("There are no letters with current header")
        self.get_email_imap.logout()


if __name__ == '__main__':
    try:
        command = str()
        login = str(input("Please enter your e-mail: "))
        password = str(input("Please enter your password: "))
        while command != "q":
            command = str(input("Please enter your command (send / read / q): "))
            if command == "q":
                break
            elif command == "send" or command == "read":
                if command == "send":
                    recipients = str(input("Please enter your recipients with comma: "))
                    recipients = recipients.split(',')
                    message = str(input("Please enter your message: "))
                    subject = str(input("Please enter your subject: "))
                    mail = GMail(email=login, password=password, recipients=recipients,
                                 message=message, subject=subject)
                    mail.send_email()
                else:
                    header = str(input("Please enter header what you find: "))
                    mail = GMail(email=login, password=password, header=header)
                    mail.get_emails()
        print("Program is closed.")
    except (imaplib.IMAP4.error, smtplib.SMTPAuthenticationError, TypeError):
        print("[AUTHENTICATION FAILED] Invalid credentials")