import os
import requests
import os.path
import json
import shutil
import sys
from robot.api import logger


def generate_headers(bearer_token=False):
    token = get_token()
    _header = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    return _header



def get_token():
    env_path = 'gistProject/.env.local'
    counter = 0
    if os.path.exists(env_path):
        with open(env_path) as read_obj:
            for line in read_obj:
                if 'GITHUB_TOKEN' in line:
                    tk = line.replace('GITHUB_TOKEN=', '')
                    token = tk[:-1]
                    counter += 1
                if counter == 2:
                    break
        if counter != 2:
            raise ValueError("Not enough sufficient information to create Gist connection")
    else:
        token = os.environ.get('GITHUB_TOKEN')
        if token is None:
            raise ValueError("Not enough sufficient information to create Session")
    return token


def setup_gist_session():
    session = requests.Session()
    session.headers.update(generate_headers())
    return session
