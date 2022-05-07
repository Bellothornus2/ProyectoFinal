from flask import redirect, Blueprint
from services.update_daily import update_daily as update_daily_service
from services.get_all import get_all as get_all_service

update_daily_blue = Blueprint("update_daily", __name__)


@update_daily_blue.route("/update_daily", methods=["PUT"])
def update_daily():
    items = get_all_service()
    update_daily_service(items)
