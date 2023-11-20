from flask import Blueprint

auth_blueprint = Blueprint('auth_blueprint_b', __name__, url_prefix='/auth')