from flask import redirect, Blueprint, request
from services import create_alcohols,get_last_id,get_item

create_alcohol_blueprint = Blueprint("create_alcohol", __name__)


@create_alcohol_blueprint.route("/item", methods=["POST"])
def create_alcohol():
    data = request.get_json()
    name = data["name"]
    sell_in = data["sell_in"]
    quality = data["quality"]
    create_alcohols.create_alcohol(name, int(sell_in), int(quality))
    last_id = str(get_last_id.get_last_id())
    answer = get_item.get_item(last_id)
    return answer
