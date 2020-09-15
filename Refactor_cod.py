import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Work_with_mail:
    def __init__(self, GMAIL_SMTP, GMAIL_IMAP, user_login, user_password, subject, recipients, message, title, port):
        self.GMAIL_SMTP = GMAIL_SMTP
        self.GMAIL_IMAP = GMAIL_IMAP
        self.user_login = user_login
        self.user_password = user_password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.title = title
        self.port = port

    def send_email(self):
        # отправить сообщение
        msg = MIMEMultipart()
        msg['From'] = self.user_login
        msg['To'] = ','.join(self.recipients)
        msg['Тема'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.GMAIL_SMTP, self.port)
        # идентифицируем себя для smtp клиента
        ms.ehlo()
        # защитите нашу электронную почту с помощью tls-шифрования
        ms.starttls()
        # повторно идентифицируем себя как зашифрованное соединение
        ms.ehlo()
        ms.login(self.user_login, self.user_password)
        ms.sendmail(self.user_login, self.recipients, msg.as_string())
        ms.quit()
        # отправить конец
        return 'Отправка завершена'

    def receive_email(self):
        # получить
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.user_login, self.user_password)
        mail.list()
        mail.select('INBOX')
        criterion = '(HEADER Subject "% s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'Нет писем с текущим заголовком'
        latest_email_uid = data[0].split()[- 1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        #end recieve
        return 'Письма получены'


if __name__ == "__main__":
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"
    user_login = 'login@gmail.com'
    user_password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Сообщение'
    title = None
    port = '587'
    test = Work_with_mail(GMAIL_SMTP, GMAIL_IMAP, user_login, user_password, subject, recipients, message, title, port)
    test.send_email()
    test.receive_email()