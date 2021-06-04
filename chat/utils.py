import json

import requests as http
from flask import current_app
from flask_login import current_user


def get_bot_reply(msg):
    r = http.post(
        url=current_app.config['BOT']['url'],
        # json={'sender': f'{current_user.info["username"]}@{msg["r_id"]}', 'message': msg['msg']})
        json={'sender': current_user.info['username'], 'message': msg['msg']})
    return json.dumps(r.json())
