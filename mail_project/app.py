# importing libraries
from flask import Flask, render_template, request
from flask_mail import Mail, Message

   
app = Flask(__name__)
mail= Mail(app)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def login():
    return render_template('login.html')
   
@app.route("/home", methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        email= request.form["Email"]
        name= request.form["Name"]
        app.config['MAIL_USERNAME'] = email
        app.config['MAIL_PASSWORD'] = name
    return render_template('index.html')
   

@app.route("/send_message",methods = ['GET','POST'])
def send_message():
    if request.method == 'POST':
        from_email= request.form["from_email"]
        to_email= request.form["to_email"]
        msg= request.form["Message"]
        subject= request.form["Name"]
        message = Message(subject, sender = from_email, recipients = [to_email])
        message.body = msg
        mail = Mail(app)
        mail.send(message)
    return render_template('home.html')
   
if __name__ == '__main__':
   app.run(debug = True)