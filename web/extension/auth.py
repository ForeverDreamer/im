import functools

# from flask import current_app
from flask_login import UserMixin, LoginManager, current_user
from flask_socketio import disconnect

# from lib.message import send_error_message
from db.user import db_find_user


def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            # send_error_message({'code': 401, 'msg': '请登录后操作'})
            # emit('data', {'code': 401, 'msg': '请登录后操作'})
            disconnect()
            # return current_app.login_manager.unauthorized()
        else:
            return f(*args, **kwargs)
    return wrapped


# login_manager = None


class User(UserMixin):
    """用户类"""
    def __init__(self, user):
        self._info = user

    @property
    def info(self):
        return self._info

    # def verify_password(self, password):
    #     """密码验证"""
    #     return check_password_hash(self._info.get('password'), password)

    def get_id(self):
        return self._info['_id']

    @staticmethod
    def find_one(u_id):
        user = db_find_user({'_id': u_id})
        if user:
            return User(user)
        else:
            return None


def init_auth(app):
    # global login_manager
    login_manager = LoginManager(app)

    @login_manager.unauthorized_handler
    def unauthorized():
        return {'msg': '请登录后操作！'}, 401

    @login_manager.user_loader
    def load_user(u_id):
        return User.find_one(u_id)

    # @login_manager.request_loader
    # def load_request(request):
    #     auth = request.authorization
    #
    #     if auth is not None:
    #         username, password = auth['username'], auth['password']
    #         user = User.find_one(username)
    #         if user is not None and user.password == password:
    #             return user
    #     return None
