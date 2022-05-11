from flask import jsonify, Blueprint, request
from services.type_alcohol import (
	get_type_alcohol_id,
	get_all_type_alcohol,
	get_type_alcohol_last_id,
	create_type_alcohol,
	update_type_alcohol,
	delete_type_alcohol
)

get_type_alcohol_blueprint = Blueprint("get_type_alcohol", __name__)
get_all_type_alcohol_blueprint = Blueprint("get_all_type_alcohol", __name__)
create_type_alcohol_blueprint = Blueprint("create_type_alcohol", __name__)
update_type_alcohol_blueprint = Blueprint("update_type_alcohol", __name__)
delete_type_alcohol_blueprint = Blueprint("delete_type_alcohol", __name__)

@get_type_alcohol_blueprint.route("/type_alcohol/<id>",methods=["GET"])
def get_type_alcohol_function(id):
	response = get_type_alcohol_id(id)
	response = jsonify(response)
	return response

@get_all_type_alcohol_blueprint.route("/type_alcohol",methods=["GET"])
def get_all_type_alcohol_function():
	response = get_all_type_alcohol()
	response = jsonify(response)
	return response

@create_type_alcohol_blueprint.route("/type_alcohol", methods=["POST"])
def create_type_alcohol_function():
	data = request.get_json()
	name = data["name"]
	create_type_alcohol(name)
	last_id = get_type_alcohol_last_id()
	answer = get_type_alcohol_id(last_id)
	return answer

@update_type_alcohol_blueprint.route("/type_alcohol/<type_alcohol_id>", methods=["PUT"])
def update_type_alcohol_function(type_alcohol_id):
	data = request.get_json()
	name = data["name"]
	update_type_alcohol(type_alcohol_id,name)
	answer = get_type_alcohol_id(type_alcohol_id)
	return answer

@delete_type_alcohol_blueprint.route("/type_alcohol/<type_alcohol_id>", methods=["DELETE"])
def delete_type_alcohol_function(type_alcohol_id):
	data = get_type_alcohol_id(type_alcohol_id)
	if "error" not in data:
		delete_type_alcohol(type_alcohol_id)
	return data