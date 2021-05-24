from flask_login import UserMixin, LoginManager


# login_manager = None

users = {}


class User(UserMixin):
    """用户类"""
    def __init__(self, user):
        self._info = user
        self._u_id = str(self._info.pop('_id'))

    @property
    def info(self):
        return self._info

    # def verify_password(self, password):
    #     """密码验证"""
    #     return check_password_hash(self._info.get('password'), password)

    @property
    def u_id(self):
        return self._u_id

    @staticmethod
    def find_one(u_id):
        return users.get(u_id)


def init_app(app):
    # global login_manager
    login_manager = LoginManager(app)

    @login_manager.unauthorized_handler
    def unauthorized():
        return {'msg': '请登录后操作！'}, 401

    @login_manager.user_loader
    def load_user(u_id):
        return User.find_one(u_id)
