from flask import redirect, Blueprint, request
from services.update_item import update_item as update_item_service
from services.get_item import get_item
update_item_blueprint = Blueprint("update_item", __name__)


@update_item_blueprint.route("/item/<item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    new_name = data["name"]
    new_sell_in = data["sell_in"]
    new_quality = data["quality"]
    update_item_service(item_id, new_name, int(new_sell_in), int(new_quality))
    answer = get_item(item_id)
    return answer
