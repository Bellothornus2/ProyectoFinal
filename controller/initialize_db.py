from flask import Blueprint, redirect
from services.initialize_db import initialize_db

initialize_items_blueprint = Blueprint("initialize_items", __name__)


@initialize_items_blueprint.route("/initialize_db", methods=["GET"])
def initialize_items_function():
	initialize_db()
	#return redirect("/")
