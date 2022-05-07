from flask import jsonify, Blueprint
from services import get_item

get_item_blueprint = Blueprint("get_item", __name__)


@get_item_blueprint.route("/item/<id>")
def get_item_func(id):
    response = get_item.get_item(id)
    return jsonify(response)
