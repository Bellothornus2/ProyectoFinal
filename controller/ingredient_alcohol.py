from flask import jsonify, Blueprint, request
from services.ingredient_alcohol import (
	get_ingredient_alcohol_id,
	get_all_ingredient_alcohol,
	get_ingredient_alcohol_last_id,
	create_ingredient_alcohol,
	update_ingredient_alcohol,
	delete_ingredient_alcohol
)

get_ingredient_alcohol_blueprint = Blueprint("get_ingredient_alcohol", __name__)
get_all_ingredient_alcohol_blueprint = Blueprint("get_all_ingredient_alcohol", __name__)
create_ingredient_alcohol_blueprint = Blueprint("create_ingredient_alcohol", __name__)
update_ingredient_alcohol_blueprint = Blueprint("update_ingredient_alcohol", __name__)
delete_ingredient_alcohol_blueprint = Blueprint("delete_ingredient_alcohol", __name__)

@get_ingredient_alcohol_blueprint.route("/ingredient_alcohol/<id>",methods=["GET"])
def get_ingredient_alcohol_function(id):
	response = get_ingredient_alcohol_id(id)
	response = jsonify(response)
	return response

@get_all_ingredient_alcohol_blueprint.route("/ingredient_alcohol",methods=["GET"])
def get_all_ingredient_alcohol_function():
	response = get_all_ingredient_alcohol()
	response = jsonify(response)
	return response

@create_ingredient_alcohol_blueprint.route("/ingredient_alcohol", methods=["POST"])
def create_ingredient_alcohol():
	data = request.get_json()
	alcohol_id = data["alcohol_id"]
	type_alcohol_id = data["ingredient_id"]
	create_ingredient_alcohol(alcohol_id,type_alcohol_id)
	last_id = get_ingredient_alcohol_last_id()
	answer = get_ingredient_alcohol_id(last_id)
	return answer

@update_ingredient_alcohol_blueprint.route("/ingredient_alcohol/<ingredient_alcohol_id>", methods=["PUT"])
def update_ingredient_alcohol(ingredient_alcohol_id):
	data = request.get_json()
	alcohol_id = data["alcohol_id"]
	type_alcohol_id = data["ingredient_id"]
	update_ingredient_alcohol(ingredient_alcohol_id,alcohol_id,type_alcohol_id)
	answer = get_ingredient_alcohol_id(ingredient_alcohol_id)
	return answer

@delete_ingredient_alcohol_blueprint.route("/ingredient_alcohol/<ingredient_alcohol_id>", methods=["DELETE"])
def delete_ingredient_alcohol_function(ingredient_alcohol_id):
	data = get_ingredient_alcohol_id(ingredient_alcohol_id)
	if "error" not in data:
		delete_ingredient_alcohol(ingredient_alcohol_id)
	return data