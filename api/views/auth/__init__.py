"""Authorization endpoints"""

from flask import Blueprint

auth_view = Blueprint("auth_view", __name__)

from .login import *
from .signup import *
