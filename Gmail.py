import imaplib
import email
import re


class Gmail:
    SMTP_SERVER = "imap.gmail.com"

    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def read_mails(self):
        try:
            mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
            mail.login(self.sender_email, self.sender_password)
            mail.select('inbox')

            type, data = mail.search(None, 'ALL')
            mail_ids = data[0].decode('utf-8')
            id_list = mail_ids.split()
            first_email_id = int(id_list[0])

            latest_email_id = int(id_list[-1])

            email_list = []

            for i in range(latest_email_id, first_email_id, -1):
                print('Reading Mail with ID: ' + str(i))
                typ, data = mail.fetch(str(i), '(RFC822)')
                for response_part in data:

                    if isinstance(response_part, tuple):

                        msg = email.message_from_string(response_part[1].decode('utf-8'))
                        email_from = msg['from']
                        email_to = msg['to']
                        email_re_to = re.findall('\S+@\S+', email_to)
                        email_re_from = re.findall('\S+@\S+', email_from)
                        email_list.append(email_re_to)
                        email_list.append(email_re_from)

            return email_list

        except Exception as e:
            print(str(e))

