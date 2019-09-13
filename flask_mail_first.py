import os
from threading import Thread

from flask import Flask
from flask_mail import Mail, Message

assert 'SYSTEMROOT' in os.environ
app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
))

mail = Mail(app)


# 异步
def send_async_email(app, message):
    with app.app_context():
        mail.send(message)


@app.route('/mail')
def send_mail():
    message = Message(subject='hello, world!',
                      sender=app.config["MAIL_USERNAME"],
                      recipients=['1290017556@qq.com'],
                      body='Across the Great Wall we  reach every corner in the world.')

    thread = Thread(target=send_async_email, args=[app, message])
    thread.start()
    return "Sent　Succeed"


# 手动挡
# with app.app_context():
#     message = Message(subject='hello, world!',
#                       sender=app.config["MAIL_USERNAME"],
#                       recipients=['823301694@qq.com'],
#                       body='Across the Great Wall we  reach every corner in the world.')
#
#     thread = Thread(target=send_async_email, args=[app, message])
#     thread.start()
