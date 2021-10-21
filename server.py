import smtplib
import os
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    msg = request.form.get('message')

    subject = f'New Message From {name}'
    body1 = f'Hello {name}!!, I hope you enjoy my website'
    message = f'Subject: {subject}\n\n{msg}'
    message1 = f'Subject: Thanks For Your Support\n\n{body1}'
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('mokalulovelyo@gmail.com', 'password')
    server.sendmail(email, 'mokalulovelyo@gmail.com', message)
    server.sendmail('mokalulovelyo@gmail.com', email, message1)
    return render_template('index.html')
        

if __name__ == '__main__':
    app.run(debug=True)