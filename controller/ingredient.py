from flask import jsonify, Blueprint, request
from services.ingredient import (
	get_ingredient_id,
	get_all_ingredient,
	get_ingredient_last_id,
	create_ingredient,
	update_ingredient,
	delete_ingredient
)

get_ingredient_blueprint = Blueprint("get_ingredient", __name__)
get_all_ingredient_blueprint = Blueprint("get_all_ingredient", __name__)
create_ingredient_blueprint = Blueprint("create_ingredient", __name__)
update_ingredient_blueprint = Blueprint("update_ingredient", __name__)
delete_ingredient_blueprint = Blueprint("delete_ingredient", __name__)

@get_ingredient_blueprint.route("/ingredient/<id>",methods=["GET"])
def get_ingredient_function(id):
	response = get_ingredient_id(id)
	response = jsonify(response)
	return response

@get_all_ingredient_blueprint.route("/ingredient",methods=["GET"])
def get_all_ingredient_function():
	response = get_all_ingredient()
	response = jsonify(response)
	return response

@create_ingredient_blueprint.route("/ingredient", methods=["POST"])
def create_ingredient():
	data = request.get_json()
	name = data["name"]
	create_ingredient(name)
	last_id = get_ingredient_last_id()
	answer = get_ingredient_id(last_id)
	return answer

@update_ingredient_blueprint.route("/ingredient/<ingredient_id>", methods=["PUT"])
def update_ingredient(ingredient_id):
	data = request.get_json()
	name = data["name"]
	update_ingredient(ingredient_id,name)
	answer = get_ingredient_id(ingredient_id)
	return answer

@delete_ingredient_blueprint.route("/ingredient/<ingredient_id>", methods=["DELETE"])
def delete_ingredient_function(ingredient_id):
	data = get_ingredient_id(ingredient_id)
	if "error" not in data:
		delete_ingredient(ingredient_id)
	return data