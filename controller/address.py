from flask import jsonify, Blueprint, request
from services.address import (
	get_address_id,
	get_all_address,
	get_address_last_id,
	create_address,
	update_address,
	delete_address
)

get_address_blueprint = Blueprint("get_address", __name__)
get_all_address_blueprint = Blueprint("get_all_address", __name__)
create_address_blueprint = Blueprint("create_address", __name__)
update_address_blueprint = Blueprint("update_address", __name__)
delete_address_blueprint = Blueprint("delete_address", __name__)

@get_address_blueprint.route("/address/<id>",methods=["GET"])
def get_address_function(id):
	response = get_address_id(id)
	response = jsonify(response)
	return response

@get_all_address_blueprint.route("/address",methods=["GET"])
def get_all_address_function():
	response = get_all_address()
	response = jsonify(response)
	return response

@create_address_blueprint.route("/address", methods=["POST"])
def create_address_function():
	data = request.get_json()
	street = data["street"]
	street_number = data["street_number"]
	floor = data["floor"]
	door = data["door"]
	zip_code = data["zip_code"]
	other_data = data["other_data"]
	type_address = data["type_address"]
	user_id = data["user_id"]
	create_address(street,street_number,floor,door,zip_code,other_data,type_address,user_id)
	last_id = get_address_last_id()
	answer = get_address_id(last_id)
	return answer

@update_address_blueprint.route("/address/<address_id>", methods=["PUT"])
def update_address_function(address_id):
	data = request.get_json()
	street = data["street"]
	street_number = data["street_number"]
	floor = data["floor"]
	door = data["door"]
	zip_code = data["zip_code"]
	other_data = data["other_data"]
	type_address = data["type_address"]
	user_id = data["user_id"]
	update_address(address_id,street,street_number,floor,door,zip_code,other_data,type_address,user_id)
	answer = get_address_id(address_id)
	return answer

@delete_address_blueprint.route("/address/<address_id>", methods=["DELETE"])
def delete_address_function(address_id):
	data = get_address_id(address_id)
	if "error" not in data:
		delete_address(address_id)
	return data