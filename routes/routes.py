from flask import Blueprint
from controllers.general_controller import health
from controllers.image_controller import classify, get_all_imagens, list_classficiations_user, get_image
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
image_bp.route("/classify/get_all", methods=["GET"])(get_all_imagens)
image_bp.route("/classifications/<int:id>", methods=["GET"])(list_classficiations_user)
image_bp.route("/<string:hash>", methods=["GET"])(get_image)

# General
general_bp.route("/health", methods=["GET"])(health)
