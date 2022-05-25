from peewee import SqliteDatabase,ForeignKeyField,Model,FloatField,IntegerField,fn

from services.order import Order
from services.alcohol import Alcohol


db = SqliteDatabase('ImpetuYam.sqlite')

class OrderLine(Model):
	alcohol_id = ForeignKeyField(Alcohol)
	quantity = IntegerField()
	price = FloatField()
	discount = IntegerField()
	total = FloatField()
	order_id = ForeignKeyField(Order)
	class Meta:
		database = db

def get_order_line_last_id():
	db.connect()
	query = OrderLine.select(fn.MAX(OrderLine.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_order_line():
	db.connect()
	list_order_line = OrderLine.select()
	data = {}
	data["data"] = []
	for item in list_order_line:
		data["data"].append({
			"id":item.id,
			"alcohol_id":item.alcohol_id.id,
			"quantity":item.quantity,
			"price":item.price,
			"discount":item.discount,
			"total":item.total,
			"order_id":item.order_id
		})
	db.close()
	return data

def get_order_line_id(order_line_id):
	try:
		db.connect()
		order_line_db = OrderLine.get(OrderLine.id == order_line_id)
		answer = {
			"data":{
				"id":order_line_db.id,
				"alcohol_id":order_line_db.alcohol_id.id,
				"quantity":order_line_db.quantity,
				"price":order_line_db.price,
				"discount":order_line_db.discount,
				"total":order_line_db.total,
				"order_id":order_line_db.order_id
			}
		}
		db.close()
	except OrderLine.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_order_line(alcohol_id,quantity,price,discount,total,order_id):
	db.connect()
	try:
		order_line = OrderLine.create(
			alcohol_id = alcohol_id,
			quantity = quantity,
			price = price,
			discount = discount,
			total = total,
			order_id = order_id
		)
		order_line.save()
		db.commit()
	except:
		pass
	db.close()

def update_order_line(id, alcohol_id,quantity,price,discount,total,order_id):
	db.connect()
	try:
		order_line = OrderLine.get(OrderLine.id==id)
		order_line.alcohol_id = alcohol_id
		order_line.quantity = quantity
		order_line.price = price
		order_line.discount = discount
		order_line.total = total
		order_line.order_id = order_id
		order_line.save()
		db.commit()
	except OrderLine.DoesNotExist:
		pass
	db.close()

def delete_order_line(id):
	db.connect()
	try:
		order_line = OrderLine.get(OrderLine.id==id)
		order_line.delete_instance()
	except OrderLine.DoesNotExist:
		pass
	db.close()


