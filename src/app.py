import hashlib
import hmac
from logging.config import dictConfig

import requests
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import Response
from flask_mail import Mail
from flask_mail import Message

from src.utils import config
from src.utils.cache import cache
from src.utils.token import get_invitation_access_token

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[flask] %(levelname)s %(asctime)s %(module)s %(message)s",
            },
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)


app.config["MAIL_SERVER"] = config.SMTP_HOST
app.config["MAIL_PORT"] = config.SMTP_PORT
app.config["MAIL_USERNAME"] = config.SMTP_USER
app.config["MAIL_PASSWORD"] = config.SMTP_PASS
app.config["MAIL_USE_TLS"] = config.SMTP_USE_TLS
app.config["MAIL_DEFAULT_SENDER"] = config.DEFAULT_FROM_EMAIL

mail = Mail(app)

cache.init_app(app)


@app.route("/invitation", methods=["POST"])
def invitation():
    req_signature = request.headers.get("x-bimdata-signature")
    if not req_signature:
        response = jsonify({"x-bimdata-signature": "Header required"})
        response.status_code = 400
        return response

    body_signature = hmac.new(
        config.INVITATION_SECRET.encode(), request.get_data(), hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(req_signature, body_signature):
        response = jsonify({"x-bimdata-signature": "Bad request signature"})
        response.status_code = 400
        return response

    invitation_data = request.get_json()
    required_fields = (
        "id",
        "client_id",
        "redirect_uri",
        "cloud_name",
        "email",
    )
    for field in required_fields:
        if field not in invitation_data:
            response = jsonify({field: "This field is required"})
            response.status_code = 400
            return response

    if config.ACCEPT_INVITATIONS:
        requests.post(
            f"{config.API_URL}/identity-provider/invitation/{invitation_data.get('id')}/accept",
            headers={"Authorization": f"Bearer {get_invitation_access_token()}"},
        )

    msg = Message(
        subject=render_template("title.txt", **invitation_data).strip(),
        sender=config.DEFAULT_FROM_EMAIL,
        recipients=[invitation_data.get("email")],
    )
    msg.body = render_template("content.txt", **invitation_data)
    msg.html = render_template("content.html", **invitation_data)
    mail.send(msg)
    return Response(), 204
