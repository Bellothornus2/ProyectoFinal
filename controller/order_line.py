from flask import jsonify, Blueprint, request
from services.order_line import (
	get_order_line_id,
	get_all_order_line,
	get_order_line_last_id,
	create_order_line,
	update_order_line,
	delete_order_line
)

get_order_line_blueprint = Blueprint("get_order_line", __name__)
get_all_order_line_blueprint = Blueprint("get_all_order_line", __name__)
create_order_line_blueprint = Blueprint("create_order_line", __name__)
update_order_line_blueprint = Blueprint("update_order_line", __name__)
delete_order_line_blueprint = Blueprint("delete_order_line", __name__)

@get_order_line_blueprint.route("/order_line/<id>",methods=["GET"])
def get_order_line_function(id):
	response = get_order_line_id(id)
	response = jsonify(response)
	return response

@get_all_order_line_blueprint.route("/order_line",methods=["GET"])
def get_all_order_line_function():
	response = get_all_order_line()
	response = jsonify(response)
	return response

@create_order_line_blueprint.route("/order_line", methods=["POST"])
def create_order_line_function():
	data = request.get_json()
	alcohol_id = data["alcohol_id"]
	quantity = data["quantity"]
	price = data["price"]
	discount = data["discount"]
	total = data["total"]
	order_id = data["order_id"]

	create_order_line(alcohol_id,quantity,price,discount,total,order_id)
	last_id = get_order_line_last_id()
	answer = get_order_line_id(last_id)
	return answer

@update_order_line_blueprint.route("/order_line/<order_line_id>", methods=["PUT"])
def update_order_line_function(order_line_id):
	data = request.get_json()
	alcohol_id = data["alcohol_id"]
	quantity = data["quantity"]
	price = data["price"]
	discount = data["discount"]
	total = data["total"]
	order_id = data["order_id"]
	update_order_line(order_line_id,alcohol_id,quantity,price,discount,total,order_id)
	answer = get_order_line_id(order_line_id)
	return answer

@delete_order_line_blueprint.route("/order_line/<order_line_id>", methods=["DELETE"])
def delete_order_line_function(order_line_id):
	data = get_order_line_id(order_line_id)
	if "error" not in data:
		delete_order_line(order_line_id)
	return data