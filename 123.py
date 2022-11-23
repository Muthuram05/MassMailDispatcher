from flask import Flask, request, render_template
import smtplib, ssl
from email.mime.text import MIMEText
import re
import os

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')


port = 465
user = 'mr032495@gmail.com'
password = '81497AB4379ABD01728D0CB5972EE6EEF6F3'
sender = 'mr032495@gmail.com'

@app.route('/upload/', methods=['POST'])
def upload():
    if request.method == 'POST':
        fromtxt = request.form['fromtxt']
        subject = request.form['subject']
        message = request.form['message']
        f = request.files['file']
        f.save(f.filename)
        f = f.filename
        name = open(f, "r")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        arrval = []
        arrinval = []

        def check(email):
            if (re.match(regex, email)):
                arrval.append(email)
                msg = MIMEText(message)
                msg['Subject'] = subject
                msg['From'] = fromtxt
                msg['To'] = email
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.elasticemail.com", port, context=context) as server:
                    server.login(user, password)
                    server.sendmail(sender, email, msg.as_string())
                    # print('mail successfully sent')
            else:
                arrinval.append(email)
        for x in name:
            check(x)
        return render_template("upload.html", data = str(len(arrval)) + " Mail Sent Successfully" )


@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        f = f.filename
        name = open(f, "r")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        checkval = []
        checkinval = []
        def check(email):
            if (re.match(regex, email)):
                checkval.append(email)
            else:
                checkinval.append(email)
        for x in name:
            check(x)
    return render_template("index.html",val = checkval,inval = checkinval)




if __name__ == '__main__':
    app.run(debug=True)
