import smtplib

class Gmail(object):
    def __init__(self, email, password=None, server='smtp.gmail.com', port=587):
        self.email = email
        if not password:
            self.password = self.login(email)
        else:
            self.password = password
        self.init_session(server, port)
        
    def init_session(server, port):
        self.session = smtplib.SMTP(server, port)  
        self.session.ehlo()
        self.session.starttls()
        self.session.ehlo
        self.session.login(self.email, self.password)

    def login(user):
       import getpass
       return getpass.getpass('Password for %s: ' % user)

    def send_message(self, recip, subject, body):
        from email.MIMEMultipart import MIMEMultipart
        from email.MIMEBase import MIMEBase
        from email.MIMEText import MIMEText
        from email import Encoders

        ''' This must be removed '''
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = recip if type(recip) is str else ", ".join([recip])
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
        if attach:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
            msg.attach(part)
        self.session.sendmail(
            self.email,
            self.email,
            headers + "\r\n\r\n" + body)
        self.session.close()