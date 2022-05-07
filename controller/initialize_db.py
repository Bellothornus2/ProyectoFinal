from flask import Blueprint, redirect
from services import initialize_db

initialize_items_blue = Blueprint("initialize_items", __name__)


@initialize_items_blue.route("/initialize_db", methods=["GET"])
def initialize_items_func():
    initialize_db.initialize_db()
    return redirect("/")
