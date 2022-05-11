#SELECT MAX(ID) AS LastID FROM Persons
from peewee import SqliteDatabase,CharField,TextField,ForeignKeyField,FloatField,Model,IntegerField,fn
from services.type_alcohol import TypeAlcohol
from services.subtype_alcohol import SubTypeAlcohol

db = SqliteDatabase('ImpetuYam.sqlite')

class Alcohol(Model):
	name = CharField()
	price = FloatField()
	alcohol_grade = FloatField()
	brand = CharField()
	type_alcohol_id = ForeignKeyField(TypeAlcohol)
	subtype_alcohol_id = ForeignKeyField(SubTypeAlcohol)
	description = TextField()
	class Meta:
		database = db

def get_alcohol_last_id():
	db.connect()
	query = Alcohol.select(fn.MAX(Alcohol.id)) ##para obtener SELECT MAX(id) AS LastID FROM Item
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_alcohol():
	db.connect()
	list_alcohol = Alcohol.select()
	data = {}
	data["data"] = []
	for item in list_alcohol:
		data["data"].append({
			"id":item.id,
			"name":item.name,
			"price":item.price,
			"alcohol_grade":item.alcohol_grade,
			"brand":item.brand,
			"type_alcohol_id":item.type_alcohol_id.id,
			"subtype_alcohol_id":item.subtype_alcohol_id.id,
			"description":item.description
		})
	db.close()
	return data

def get_alcohol_id(alcohol_id):
	try:
		db.connect()
		alcohol_db = Alcohol.get(Alcohol.id == alcohol_id)
		answer = {
			"data":{
				"id":alcohol_db.id,
				"name":alcohol_db.name,
				"price":alcohol_db.price,
				"alcohol_grade":alcohol_db.alcohol_grade,
				"brand":alcohol_db.brand,
				"type_alcohol_id":alcohol_db.type_alcohol_id.id,
				"subtype_alcohol_id":alcohol_db.subtype_alcohol_id.id,
				"description":alcohol_db.description
			}
		}
		db.close()
	except Alcohol.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_alcohol(name,alcohol_grade,price,brand,type_alcohol,subtype_alcohol,description):
	db.connect()
	alcohol = Alcohol.create(
		name=name, 
		alcohol_grade=alcohol_grade,
		price=price,
		brand=brand,
		type_alcohol_id=type_alcohol,
		subtype_alcohol_id=subtype_alcohol,
		description=description)
	alcohol.save()
	db.commit()
	db.close()

def update_alcohol(id, name,alcohol_grade,price,brand,type_alcohol,subtype_alcohol,description):
	db.connect()
	try:
		alcohol = Alcohol.get(Alcohol.id==id)
		alcohol.name = name
		alcohol.alcohol_grade = alcohol_grade
		alcohol.price = price
		alcohol.brand = brand
		alcohol.type_alcohol_id = type_alcohol
		alcohol.subtype_alcohol_id = subtype_alcohol
		alcohol.description = description
		alcohol.save()
		db.commit()
	except Alcohol.DoesNotExist:
		pass
	db.close()

def delete_alcohol(id):
	db.connect()
	try:
		alcohol = Alcohol.get(Alcohol.id==id)
		alcohol.delete_instance()
	except Alcohol.DoesNotExist:
		pass
	db.close()
