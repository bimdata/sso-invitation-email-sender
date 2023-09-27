import hashlib
import hmac
from logging.config import dictConfig

import requests
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

from src.utils import config
from src.utils.cache import cache
from src.utils.mail import Mailer
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
    mailer = Mailer(receiver=invitation_data.get("email"))
    mailer.send(invitation_data)
    return Response(), 204
