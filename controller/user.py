from flask import jsonify, Blueprint, request
from services.user import (
	get_user_id,
	get_all_user,
	get_user_last_id,
	create_user,
	update_user,
	delete_user
)

get_user_blueprint = Blueprint("get_user", __name__)
get_all_user_blueprint = Blueprint("get_all_user", __name__)
create_user_blueprint = Blueprint("create_user", __name__)
update_user_blueprint = Blueprint("update_user", __name__)
delete_user_blueprint = Blueprint("delete_user", __name__)

@get_user_blueprint.route("/user/<id>",methods=["GET"])
def get_user_function(id):
	response = get_user_id(id)
	response = jsonify(response)
	return response

@get_all_user_blueprint.route("/user",methods=["GET"])
def get_all_user_function():
	response = get_all_user()
	response = jsonify(response)
	return response

@create_user_blueprint.route("/user", methods=["POST"])
def create_user_function():
	data = request.get_json()
	print(data)
	name = data["name"]
	surname = data["surname"]
	age = data["age"]
	dni = data["dni"]
	username = data["username"]
	password = data["password"]
	sex = data["sex"]
	phone_number = data["phone_number"]
	email = data["email"]
	verified_user = data["verified_user"]
	create_user(name, surname,age,dni,username,password,sex,phone_number,email,verified_user)
	last_id = get_user_last_id()
	answer = get_user_id(last_id)
	return answer

@update_user_blueprint.route("/user/<user_id>", methods=["PUT"])
def update_user_function(user_id):
	data = request.get_json()
	name = data["name"]
	surname = data["surname"]
	age = data["age"]
	dni = data["dni"]
	username = data["username"]
	password = data["password"]
	sex = data["sex"]
	phone_number = data["phone_number"]
	email = data["email"]
	verified_user = data["verified_user"]
	update_user(user_id,name, surname,age,dni,username,password,sex,phone_number,email,verified_user)
	answer = get_user_id(user_id)
	return answer

@delete_user_blueprint.route("/user/<user_id>", methods=["DELETE"])
def delete_user_function(user_id):
	data = get_user_id(user_id)
	if "error" not in data:
		delete_user(user_id)
	return data