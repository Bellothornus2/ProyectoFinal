from flask import jsonify, Blueprint, request
from services.credit_card import (
	get_credit_card_id,
	get_all_credit_card,
	get_credit_card_last_id,
	create_credit_card,
	update_credit_card,
	delete_credit_card
)

get_credit_card_blueprint = Blueprint("get_credit_card", __name__)
get_all_credit_card_blueprint = Blueprint("get_all_credit_card", __name__)
create_credit_card_blueprint = Blueprint("create_credit_card", __name__)
update_credit_card_blueprint = Blueprint("update_credit_card", __name__)
delete_credit_card_blueprint = Blueprint("delete_credit_card", __name__)

@get_credit_card_blueprint.route("/credit_card/<id>",methods=["GET"])
def get_credit_card_function(id):
	response = get_credit_card_id(id)
	response = jsonify(response)
	return response

@get_all_credit_card_blueprint.route("/credit_card",methods=["GET"])
def get_all_credit_card_function():
	response = get_all_credit_card()
	response = jsonify(response)
	return response

@create_credit_card_blueprint.route("/credit_card", methods=["POST"])
def create_credit_card_function():
	data = request.get_json()
	card_number = data["card_number"]
	expire_date = data["expire_date"]
	cvv = data["cvv"]
	owner_name = data["owner_name"]
	user_id = data["user_id"]
	create_credit_card(card_number,expire_date,cvv,owner_name,user_id)
	last_id = get_credit_card_last_id()
	answer = get_credit_card_id(last_id)
	return answer

@update_credit_card_blueprint.route("/credit_card/<credit_card_id>", methods=["PUT"])
def update_credit_card_function(credit_card_id):
	data = request.get_json()
	card_number = data["card_number"]
	expire_date = data["expire_date"]
	cvv = data["cvv"]
	owner_name = data["owner_name"]
	user_id = data["user_id"]
	update_credit_card(credit_card_id,card_number,expire_date,cvv,owner_name,user_id)
	answer = get_credit_card_id(credit_card_id)
	return answer

@delete_credit_card_blueprint.route("/credit_card/<credit_card_id>", methods=["DELETE"])
def delete_credit_card_function(credit_card_id):
	data = get_credit_card_id(credit_card_id)
	if "error" not in data:
		delete_credit_card(credit_card_id)
	return data