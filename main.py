# importing libraries
import smtplib

from flask import Flask, request, render_template
import time
import re
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)  # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.elasticemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mr032495@gmail.com'
app.config['MAIL_PASSWORD'] = '81497AB4379ABD01728D0CB5972EE6EEF6F3'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
# server = smtplib.SMTP("smtp.elasticemail.com",587)
# server.starttls()
# server.login("mr032495@gmail.com",'81497AB4379ABD01728D0CB5972EE6EEF6F3')


# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/send")
def send():
    msg = Message(
        subject='Hello',
        sender='mr032495@gmail.com',
        recipients=["mr032495@gmail.com"]
    )
    msg.body = 'Hello Flask message sent from Flask-Mail'
    #mail.send(msg)
    return 'Sent'


@app.route('/upload/', methods=['POST'])
def upload():
    if request.method == 'POST':
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
            else:
                arrinval.append(email)
        for x in name:
            check(x)
        for chekk in arrval:
            print(chekk)
            msg = Message(
                subject='Hello',
                sender='mr032495@gmail.com',
                recipients=[chekk]
            )
            msg.body = 'Hello Flask message sent from Flask-Mail'
        mail.send(msg)
        return render_template("upload.html", data = arrval,test = arrinval)
    # server.quit()

if __name__ == '__main__':
    app.run(debug=True)
