import os

API_URL = os.environ.get("API_URL")
IAM_URL = os.environ.get("IAM_URL")

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

INVITATION_SECRET = os.environ.get("INVITATION_SECRET")
INVITATION_CLIENT_ID = os.environ.get("INVITATION_CLIENT_ID")
INVITATION_CLIENT_SECRET = os.environ.get("INVITATION_CLIENT_SECRET")

ACCEPT_INVITATIONS = (
    os.environ.get("ACCEPT_INVITATIONS") == "True"
    or os.environ.get("ACCEPT_INVITATIONS") == "true"
)
