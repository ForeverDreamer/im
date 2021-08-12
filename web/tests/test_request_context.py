from flask import request

from web.app import app


def test_request_context():
    with app.test_request_context('/?name=Peter'):
        assert request.path == '/'
        assert request.args['name'] == 'Peter'
