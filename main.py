from flask import Flask,render_template,request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
load_dotenv()

import os

from_mail = os.environ.get("FROM_MAIL")
to_mail = os.environ.get("TO_MAIL")
pass_w = os.environ.get("PASS_W")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    # Create a MIMEText object with UTF-8 encoding


    sent_msg = False
    if request.method=="POST":
        name=request.form.get('name')
        email = request.form['email']
        subject = request.form.get("subject")
        body = request.form['message']

        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'plain', 'utf-8'))


        con = smtplib.SMTP_SSL('smtp.gmail.com')
        con.login(from_mail,pass_w)

        msg['Subject'] = subject
        msg['From'] = from_mail
        msg['To'] = to_mail

        # Send the email
        con.sendmail(from_mail, to_mail, msg.as_string())

        con.quit()

        sent_msg = True


    return render_template("contact.html",sent_msg=sent_msg)



if __name__=="__main__":
    app.run(debug=True)