from flask import Blueprint, redirect
from services.initialize_db import initialize_db,create_tables

initialize_items_blueprint = Blueprint("initialize_items", __name__)
create_tables_blueprint = Blueprint("create_tables",__name__)


@initialize_items_blueprint.route("/initialize_db", methods=["GET"])
def initialize_items_function():
	initialize_db()
	#return redirect("/")

@create_tables_blueprint.route("/create_tables",methods=["GET"])
def create_tables_function():
	create_tables()
	return "Se han creado las tablas de la base de datos"