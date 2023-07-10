from flask import Blueprint
from controllers.general_controller import health
from controllers.image_controller import classify
from controllers.user_controller import create_user, login, get_all

general_bp = Blueprint("general", __name__)
image_bp = Blueprint("image", __name__, url_prefix="/image")
user_bp = Blueprint("user", __name__, url_prefix="/user")

# User routes
user_bp.route("/login", methods=["POST"])(login)
user_bp.route("/get_all", methods=["GET"])(get_all)
# user_bp.route('/', methods=['GET'])(get_user)
user_bp.route("/", methods=["POST"])(create_user)

# Image routes
image_bp.route("/classify", methods=["POST"])(classify)

# General
general_bp.route("/health", methods=["GET"])(health)
