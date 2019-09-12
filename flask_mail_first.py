import os
from flask import Flask, flash, render_template, redirect, url_for
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
import sendgrid

assert 'SYSTEMROOT' in os.environ
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

app.config.update(
    MAIL_SERVER=os.getenv('MAIL_USERNAME'),
    MAIL_PORT=587,            # STARTTLS加密
    MAIL_USE_TLS=True,        # STARTTLS加密
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),  # 从本地文件.env中获得MAIL_USERNAME的值
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),  # 同上
    MAIL_DEFAULT_SENDER=('th', os.getenv('MAIL_USERNAME'))
)

# app.config.update(
#     MAIL_SERVER='smtp.sendgrid.net',
#     MAIL_PORT=587,
#     MAIL_USE_TLS=True,
#     MAIL_USERNAME='apikey',
#     MAIL_PASSWORD=os.getenv('SENDGRID_API_KEY') # 从环境变量读取API密钥
# )

mail = Mail(app)

# message = Message(subject='hello, world!', recipients=['th <1290017556@qq.com>'],body='Across the Great Wall we  reach every corner in the world.')
# message = Message(subject='hello, world!', recipients=['th <1290017556@qq.com>'],body='Across the Great Wall we  reach every corner in the world.')
# mail.send(message)
# orm)
# class SubscribeForm(FlaskForm):
#     name = 'hel'

# def send_mail(subject, to, body):
#     message = Message(subject, recipients=[to], body=body)
#     mail.send(message)

# @app.route('/subscribe',methods=['GET','POST'])
# def subscribe():
#     form = SubscribeForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         flash('Welcome on bcard!')
#         send_mail('Subscribe Success!',email,'Hello, thank you for subscribing Flask Weekly!')
#         return redirect(url_for('index'))
#     return render_template('index.html',form=f
