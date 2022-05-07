from webbrowser import get
from flask import Blueprint, request, redirect
from services import delete_item,get_item

delete_item_blueprint = Blueprint("delete_item", __name__)


@delete_item_blueprint.route("/item/<item_id>", methods=["DELETE"])
def delete_item_func(item_id):
    """ data = request.get_json()
    name = data["name"]
    sell_in = data["sell_in"]
    quality = data["quality"] """
    data = get_item.get_item(item_id)
    if "error" not in data:
        delete_item.delete_item(item_id)
    return data
