import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template

from src.utils import config


class Mailer:
    context = ssl.create_default_context()

    def __init__(self, receiver, *args, **kwargs):
        self.server = smtplib.SMTP(host=config.EMAIL_HOST, port=config.EMAIL_PORT)
        self.server.starttls(context=self.context)
        self.server.login(user=config.EMAIL_HOST_USER, password=config.EMAIL_HOST_PASSWORD)
        self.sender = config.DEFAULT_FROM_EMAIL
        self.receiver = receiver

    def __del__(self):
        self.server.quit()

    def send(self, data):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = render_template("title.txt", **data)
        msg["From"] = self.sender
        msg["To"] = ",".join(self.receiver)

        part = MIMEText(render_template("content.html", **data), "html")
        msg.attach(part)
        self._send(msg.as_string())

    def _send(self, msg):
        self.server.sendmail(from_addr=self.sender, to_addrs=self.receiver, msg=msg)
