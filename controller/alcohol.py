from flask import jsonify, Blueprint, request
from services.alcohol import (
	get_alcohol_id,
	get_all_alcohol,
	get_alcohol_last_id,
	create_alcohol,
	update_alcohol,
	delete_alcohol
)

get_alcohol_blueprint = Blueprint("get_alcohol", __name__)
get_all_alcohol_blueprint = Blueprint("get_all_alcohol", __name__)
create_alcohol_blueprint = Blueprint("create_alcohol", __name__)
update_alcohol_blueprint = Blueprint("update_alcohol", __name__)
delete_alcohol_blueprint = Blueprint("delete_alcohol", __name__)

@get_alcohol_blueprint.route("/alcohol/<id>",methods=["GET"])
def get_alcohol_function(id):
	response = get_alcohol_id(id)
	response = jsonify(response)
	return response

@get_all_alcohol_blueprint.route("/alcohol",methods=["GET"])
def get_all_alcohol_function():
	response = get_all_alcohol()
	response = jsonify(response)
	return response

@create_alcohol_blueprint.route("/alcohol", methods=["POST"])
def create_alcohol_function():
	data = request.get_json()
	name = data["name"]
	alcohol_grade = data["alcohol_grade"]
	price = data["price"]
	brand = data["brand"]
	type_alcohol = data["type_alcohol_id"]
	subtype_alcohol = data["subtype_alcohol_id"]
	description = data["description"]
	create_alcohol(name, float(alcohol_grade), float(price), brand, type_alcohol, subtype_alcohol, description)
	last_id = get_alcohol_last_id()
	answer = get_alcohol_id(last_id)
	return answer

@update_alcohol_blueprint.route("/alcohol/<alcohol_id>", methods=["PUT"])
def update_alcohol_function(alcohol_id):
	data = request.get_json()
	name = data["name"]
	alcohol_grade = data["alcohol_grade"]
	price = data["price"]
	brand = data["brand"]
	type_alcohol = data["type_alcohol"]
	subtype_alcohol = data["subtype_alcohol"]
	description = data["description"]
	update_alcohol(alcohol_id,name,alcohol_grade,price,brand,type_alcohol,subtype_alcohol,description)
	answer = get_alcohol_id(alcohol_id)
	return answer

@delete_alcohol_blueprint.route("/alcohol/<alcohol_id>", methods=["DELETE"])
def delete_alcohol_function(alcohol_id):
	data = get_alcohol_id(alcohol_id)
	if "error" not in data:
		delete_alcohol(alcohol_id)
	return data