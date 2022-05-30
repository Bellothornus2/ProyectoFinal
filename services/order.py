from peewee import SqliteDatabase,ForeignKeyField,Model,FloatField,CharField,fn

from services.credit_card import CreditCard
from services.user import User
from services.address import Address


db = SqliteDatabase('ImpetuYam.sqlite')

class Order(Model):
	address_send_id = ForeignKeyField(Address)
	address_bill_id = ForeignKeyField(Address)
	credit_card_id = ForeignKeyField(CreditCard)
	total_amount = FloatField()
	date_str = CharField()
	user_id = ForeignKeyField(User)
	class Meta:
		database = db

def get_order_last_id():
	db.connect()
	query = Order.select(fn.MAX(Order.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_order():
	db.connect()
	list_order = Order.select()
	data = {}
	data["data"] = []
	for item in list_order:
		data["data"].append({
			"id":item.id,
			"user_id":item.user_id.id,
			"address_send":item.address_send_id.id,
			"address_bill":item.address_bill_id.id,
			"credit_card":item.credit_card_id.id,
			"date_srt":item.date_str,
			"total_amount":item.total_amount
		})
	db.close()
	return data

def get_order_id(order_id):
	try:
		db.connect()
		order_db = Order.get(Order.id == order_id)
		answer = {
			"data":{
				"id":order_db.id,
				"user_id":order_db.user_id.id,
				"address_send":order_db.address_send_id.id,
				"address_bill":order_db.address_bill_id.id,
				"credit_card":order_db.credit_card_id.id,
				"date_srt":order_db.date_str,
				"total_amount":order_db.total_amount
			}
		}
		db.close()
	except Order.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_order(user_id,address_send,address_bill,credit_card,total_amount,date_str):
	db.connect()
	order = Order.create(
		user_id = user_id,
		address_send_id = address_send,
		address_bill_id = address_bill,
		credit_card_id = credit_card,
		total_amount = total_amount,
		date_str = date_str
	)
	order.save()
	db.commit()
	db.close()

def update_order(id, user_id,address_send,address_bill,credit_card,total_amount,date_str):
	db.connect()
	try:
		order = Order.get(Order.id==id)
		order.user_id = user_id
		order.address_send_id = address_send
		order.address_bill_id = address_bill
		order.credit_card_id = credit_card
		order.total_amount = total_amount
		order.date_str = date_str
		order.save()
		db.commit()
	except Order.DoesNotExist:
		pass
	db.close()

def delete_order(id):
	db.connect()
	try:
		order = Order.get(Order.id==id)
		order.delete_instance()
	except Order.DoesNotExist:
		pass
	db.close()


