import  email.mime.multipart
import email.mime
import smtplib
import email.encoders as encode
import email.mime.text
import datetime
import email.mime.base
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase



class send_mail(object):

    def send_status(self, logfile):
        email_user = 'priya12it'
        email_password = 'Priyash@24'
        email =  'priya12it@gmail.com'
        today = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
        subject = 'Test execution status: '+today
        print ("inside send_status")
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email
        msg['Subject'] = subject
        body = 'Dear Rajani,'+ '\n\n'+ 'Attached is the log file.' '\n\n'+'Thanks,' + '\n''xa'
        print("After body")
        msg.attach(MIMEText(body, 'plain'))
        filename = logfile
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        #encoders.encode_base64(part)
        encode.encode_base64(part)
        attach_name = 'TestResults___main__.MyTestExample_2020-01-31_19-50-53.html'
        part.add_header('Content-Disposition', "attachment; filename= " + attach_name )
        msg.attach(part)
        text = msg.as_string()
        print ("before accessing outlook server")

        #mailserver = smtplib.SMTP(host='smtp.office365.com', port=587)
        mailserver = smtplib.SMTP(host='smtp.gmail.com', port=587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.login(email_user,email_password)
        mailserver.sendmail(email_user, email, text)
        mailserver.quit()

if __name__ == "__main__":
    logfile = r'xfile.txt'
    s = send_mail()
    s.send_status(logfile)
 # test_mail.send_status("output.log","mycontacts.txt")