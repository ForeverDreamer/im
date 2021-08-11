import os
from pprint import pprint as pp

import pytest

url_prefix = '/v1'


@pytest.fixture
def client():
    pp(list(os.environ.items()))
    from web.app import app
    app.config.update({'TESTING': True, 'LOGIN_DISABLED': True})

    with app.test_client() as client:
        # with app.app_context():
        #     init_db()
        yield client


def test_get_room_list_success(client):
    rv = client.get(url_prefix + '/room/')
    print(rv.status_code)
    print(rv.data)
