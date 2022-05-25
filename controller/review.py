from flask import jsonify, Blueprint, request
from services.review import (
	get_review_id,
	get_all_review,
	get_review_last_id,
	create_review,
	update_review,
	delete_review
)

get_review_blueprint = Blueprint("get_review", __name__)
get_all_review_blueprint = Blueprint("get_all_review", __name__)
create_review_blueprint = Blueprint("create_review", __name__)
update_review_blueprint = Blueprint("update_review", __name__)
delete_review_blueprint = Blueprint("delete_review", __name__)

@get_review_blueprint.route("/review/<id>",methods=["GET"])
def get_review_function(id):
	response = get_review_id(id)
	response = jsonify(response)
	return response

@get_all_review_blueprint.route("/review",methods=["GET"])
def get_all_review_function():
	response = get_all_review()
	response = jsonify(response)
	return response

@create_review_blueprint.route("/review", methods=["POST"])
def create_review_function():
	data = request.get_json()
	user_id = data["user_id"]
	user_sentiment = data["user_sentiment"]
	user_rating = data["user_rating"]
	message = data["message"]
	alcohol_id = data["alcohol_id"]
	order_id = data["order_id"]
	user_sentiment = data["user_sentiment"]

	create_review(user_id,user_sentiment,user_rating,message,alcohol_id,order_id)
	last_id = get_review_last_id()
	answer = get_review_id(last_id)
	return answer

@update_review_blueprint.route("/review/<review_id>", methods=["PUT"])
def update_review_function(review_id):
	data = request.get_json()
	user_id = data["user_id"]
	user_sentiment = data["user_sentiment"]
	user_rating = data["user_rating"]
	message = data["message"]
	alcohol_id = data["alcohol_id"]
	order_id = data["order_id"]
	user_sentiment = data["user_sentiment"]
	update_review(review_id,user_id,user_sentiment,user_rating,message,alcohol_id,order_id)
	answer = get_review_id(review_id)
	return answer

@delete_review_blueprint.route("/review/<review_id>", methods=["DELETE"])
def delete_review_function(review_id):
	data = get_review_id(review_id)
	if "error" not in data:
		delete_review(review_id)
	return data