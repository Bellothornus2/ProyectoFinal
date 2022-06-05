from peewee import SqliteDatabase,ForeignKeyField,Model,FloatField,CharField,fn

from services.order import Order
from services.alcohol import Alcohol
from services.user import User


db = SqliteDatabase('ImpetuYam.sqlite')

class Review(Model):
	user_id = ForeignKeyField(User)
	user_sentiment = CharField()
	user_rating = FloatField()
	message = CharField()
	alcohol_id = ForeignKeyField(Alcohol)
	order_id = ForeignKeyField(Order)
	class Meta:
		database = db

def get_review_last_id():
	db.connect()
	query = Review.select(fn.MAX(Review.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_review():
	db.connect()
	list_review = Review.select()
	data = {}
	data["data"] = []
	for item in list_review:
		data["data"].append({
			"id":item.id,
			"user_id":item.user_id.id,
			"user_sentiment":item.user_sentiment,
			"user_rating":item.user_rating,
			"message":item.message,
			"alcohol_id":item.alcohol_id.id,
			"order_id":item.order_id.id,
			"user_name":item.user_id.name,
			"alcohol_name":item.alcohol_id.name
		})
	db.close()
	return data

def get_review_id(review_id):
	try:
		db.connect()
		review_db = Review.get(Review.id == review_id)
		answer = {
			"data":{
				"id":review_db.id,
				"user_id":review_db.user_id.id,
				"user_sentiment":review_db.user_sentiment,
				"user_rating":review_db.user_rating,
				"message":review_db.message,
				"alcohol_id":review_db.alcohol_id.id,
				"order_id":review_db.order_id.id
			}
		}
		db.close()
	except Review.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_review(user_id,user_sentiment,user_rating,message,alcohol_id,order_id):
	db.connect()
	try:
		review = Review.create(
			user_id = user_id,
			user_sentiment = user_sentiment,
			user_rating = user_rating,
			message = message,
			alcohol_id = alcohol_id,
			order_id = order_id
		)
		review.save()
		db.commit()
	except:
		pass
	db.close()

def update_review(id, user_id,user_sentiment,user_rating,message,alcohol_id,order_id):
	db.connect()
	try:
		review = Review.get(Review.id==id)
		review.user_id = user_id
		review.user_sentiment = user_sentiment
		review.user_rating = user_rating
		review.message = message
		review.alcohol_id = alcohol_id
		review.order_id = order_id
		review.save()
		db.commit()
	except Review.DoesNotExist:
		pass
	db.close()

def delete_review(id):
	db.connect()
	try:
		review = Review.get(Review.id==id)
		review.delete_instance()
	except Review.DoesNotExist:
		pass
	db.close()


