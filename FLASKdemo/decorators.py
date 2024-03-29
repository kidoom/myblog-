from functools import wraps

from flask import g, redirect, url_for


def login_required(func):
    # @wraps这个装饰器
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, 'user'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("user.login"))

    return wrapper
