from flask import jsonify, Blueprint, request
from services.order import (
	get_order_id,
	get_all_order,
	get_order_last_id,
	create_order,
	update_order,
	delete_order
)

get_order_blueprint = Blueprint("get_order", __name__)
get_all_order_blueprint = Blueprint("get_all_order", __name__)
create_order_blueprint = Blueprint("create_order", __name__)
update_order_blueprint = Blueprint("update_order", __name__)
delete_order_blueprint = Blueprint("delete_order", __name__)

@get_order_blueprint.route("/order/<id>",methods=["GET"])
def get_order_function(id):
	response = get_order_id(id)
	response = jsonify(response)
	return response

@get_all_order_blueprint.route("/order",methods=["GET"])
def get_all_order_function():
	response = get_all_order()
	response = jsonify(response)
	return response

@create_order_blueprint.route("/order", methods=["POST"])
def create_order_function():
	data = request.get_json()
	user_id= data["user_id"]
	address_send = data["address_send"]
	address_bill = data["address_bill"]
	credit_card = data["credit_card"]
	total_amount = data["total_amount"]
	create_order(user_id,address_send,address_bill,credit_card,total_amount)
	last_id = get_order_last_id()
	answer = get_order_id(last_id)
	return answer

@update_order_blueprint.route("/order/<order_id>", methods=["PUT"])
def update_order_function(order_id):
	data = request.get_json()
	user_id= data["user_id"]
	address_send = data["address_send"]
	address_bill = data["address_bill"]
	credit_card = data["credit_card"]
	total_amount = data["total_amount"]
	update_order(order_id,user_id,address_send,address_bill,credit_card,total_amount)
	answer = get_order_id(order_id)
	return answer

@delete_order_blueprint.route("/order/<order_id>", methods=["DELETE"])
def delete_order_function(order_id):
	data = get_order_id(order_id)
	if "error" not in data:
		delete_order(order_id)
	return data