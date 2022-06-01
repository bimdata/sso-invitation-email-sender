import requests

from src.utils import config
from src.utils.cache import cache


def get_invitation_access_token():
    cached_value = cache.get("invitation_access_token")
    if cached_value:
        return cached_value
    response = requests.post(
        f"{config.IAM_URL}/auth/realms/bimdata/protocol/openid-connect/token",
        data={
            "grant_type": "client_credentials",
            "client_id": config.INVITATION_CLIENT_ID,
            "client_secret": config.INVITATION_CLIENT_SECRET,
        },
    )
    response.raise_for_status()
    response = response.json()
    expires_in = response.get("expires_in") - 10  # 10 sec to be safe
    access_token = response.get("access_token")

    cache.set("invitation_access_token", access_token, timeout=expires_in)
    return access_token
