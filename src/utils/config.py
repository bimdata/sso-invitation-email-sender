import os

API_URL = os.environ.get("API_URL")
IAM_URL = os.environ.get("IAM_URL")

SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")
SMTP_USE_TLS = os.environ.get("SMTP_USE_TLS")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

INVITATION_SECRET = os.environ.get("INVITATION_SECRET")
