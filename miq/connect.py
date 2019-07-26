import os
import urllib3
from manageiq_client.api import ManageIQClient as MiqApi


def get_miq_client():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = os.environ.get('MIQURL') or 'https://192.168.188.175:32640/api'
    username = os.environ.get('MIQUSERNAME') or 'admin'
    password = os.environ.get('MIQPASSWORD') or 'smartvm'
    token = os.environ.get('MIQTOKEN')

    if token:
        print("\nAuthenticating with the API token")
        client = MiqApi(url, dict(token=token), verify_ssl=False)
    else:
        print("\nAuthenticating with the user credentials: " +
              username+" / "+password)
        client = MiqApi(
            url, dict(user=username, password=password), verify_ssl=False)

    return client
