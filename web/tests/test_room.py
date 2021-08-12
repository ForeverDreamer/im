import os
from pprint import pprint as pp

import pytest

from web.app import app
from conf import url_prefix


# count = 0


@pytest.fixture
def client():
    # global count
    # count += 1
    # with open("pytest_fixture.txt", "a") as f:
    #     f.write(str(count)+'\n')
    pp(list(os.environ.items()))
    app.config.update({'TESTING': True, 'LOGIN_DISABLED': True})

    with app.test_client() as client:
        # with app.app_context():
        #     init_db()
        yield client


def test_get_room_list_success(client):
    rv = client.get(url_prefix + '/room/')
    print(rv.status_code)
    print(rv.data)


def test_get_room_detail_success(client):
    rv = client.get(url_prefix + '/room/')
    print(rv.status_code)
    print(rv.data)
