import smtplib, ssl
from email.mime.text import MIMEText

sender = 'mr032495@gmail.com'
receivers = ['asanmohamedkhansa1234@gmail.com']

port = 465
user = 'mr032495@gmail.com'
password = '81497AB4379ABD01728D0CB5972EE6EEF6F3'

msg = MIMEText('This is test mail')

msg['Subject'] = 'Test mail'
msg['From'] = 'mr032495@gmail.com'
msg['To'] = 'asanmohamedkhansa1234@gmail.com'

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.elasticemail.com", port, context=context) as server:
    server.login(user, password)
    server.sendmail(sender, receivers, msg.as_string())
    print('mail successfully sent')