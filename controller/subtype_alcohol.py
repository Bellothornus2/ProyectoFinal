from flask import jsonify, Blueprint, request
from services.subtype_alcohol import (
	get_subtype_alcohol_id,
	get_all_subtype_alcohol,
	get_subtype_alcohol_last_id,
	create_subtype_alcohol,
	update_subtype_alcohol,
	delete_subtype_alcohol
)

get_subtype_alcohol_blueprint = Blueprint("get_subtype_alcohol", __name__)
get_all_subtype_alcohol_blueprint = Blueprint("get_all_subtype_alcohol", __name__)
create_subtype_alcohol_blueprint = Blueprint("create_subtype_alcohol", __name__)
update_subtype_alcohol_blueprint = Blueprint("update_subtype_alcohol", __name__)
delete_subtype_alcohol_blueprint = Blueprint("delete_subtype_alcohol", __name__)

@get_subtype_alcohol_blueprint.route("/subtype_alcohol/<id>",methods=["GET"])
def get_subtype_alcohol_function(id):
	response = get_subtype_alcohol_id(id)
	response = jsonify(response)
	return response

@get_all_subtype_alcohol_blueprint.route("/subtype_alcohol",methods=["GET"])
def get_all_subtype_alcohol_function():
	response = get_all_subtype_alcohol()
	response = jsonify(response)
	return response

@create_subtype_alcohol_blueprint.route("/subtype_alcohol", methods=["POST"])
def create_subtype_alcohol_function():
	data = request.get_json()
	name = data["name"]
	type_alcohol_id = data["type_alcohol_id"]
	create_subtype_alcohol(name,type_alcohol_id)
	last_id = get_subtype_alcohol_last_id()
	answer = get_subtype_alcohol_id(last_id)
	return answer

@update_subtype_alcohol_blueprint.route("/subtype_alcohol/<subtype_alcohol_id>", methods=["PUT"])
def update_subtype_alcohol_function(subtype_alcohol_id):
	data = request.get_json()
	name = data["name"]
	type_alcohol_id = data["type_alcohol_id"]
	update_subtype_alcohol(subtype_alcohol_id,name,type_alcohol_id)
	answer = get_subtype_alcohol_id(subtype_alcohol_id)
	return answer

@delete_subtype_alcohol_blueprint.route("/subtype_alcohol/<subtype_alcohol_id>", methods=["DELETE"])
def delete_subtype_alcohol_function(subtype_alcohol_id):
	data = get_subtype_alcohol_id(subtype_alcohol_id)
	if "error" not in data:
		delete_subtype_alcohol(subtype_alcohol_id)
	return data