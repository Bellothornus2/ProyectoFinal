from flask import jsonify, Blueprint
from services import get_all

get_all_blue = Blueprint("get_all", __name__)


@get_all_blue.route("/")
def get_all_func():
    response = get_all.get_all()
    return jsonify(response)
