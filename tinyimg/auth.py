from flask import current_app, g, request
from .exception import InvalidToken
from werkzeug.exceptions import MethodNotAllowed
import functools

def auth_required(view):
    """Decorator that requires API consumers to provide a valid token in the JSON body of a post request."""
    @functools.wraps(view)
    def wrapped_view(token, *args, **kwargs):
        print(token)
        if token is not None and token in current_app.config["AUTHORIZED_TOKENS"]:
            return view(**kwargs)
        else:
            raise InvalidToken("The token is either missing or invalid.")
    return wrapped_view
