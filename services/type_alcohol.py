from typing import Type
from peewee import SqliteDatabase,CharField,Model,fn

db = SqliteDatabase('ImpetuYam.sqlite')

class TypeAlcohol(Model):
	name = CharField()
	class Meta:
		database = db

def get_type_alcohol_last_id():
	db.connect()
	query = TypeAlcohol.select(fn.MAX(TypeAlcohol.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_type_alcohol():
	db.connect()
	list_type_alcohol = TypeAlcohol.select()
	data = {}
	data["data"] = []
	for item in list_type_alcohol:
		data["data"].append({
			"id":item.id,
			"name":item.name
		})
	db.close()
	return data

def get_type_alcohol_id(type_alcohol_id):
	try:
		db.connect()
		type_alcohol_db = TypeAlcohol.get(TypeAlcohol.id == type_alcohol_id)
		answer = {
			"data":{
				"id":type_alcohol_db.id,
				"name":type_alcohol_db.name,
			}
		}
		db.close()
	except TypeAlcohol.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_type_alcohol(name):
	db.connect()
	type_alcohol = TypeAlcohol.create(name=name)
	type_alcohol.save()
	db.commit()
	db.close()

def update_type_alcohol(id, name):
	db.connect()
	try:
		type_alcohol = TypeAlcohol.get(TypeAlcohol.id==id)
		type_alcohol.name = name
		type_alcohol.save()
		db.commit()
	except TypeAlcohol.DoesNotExist:
		pass
	db.close()

def delete_type_alcohol(id):
	db.connect()
	try:
		type_alcohol = TypeAlcohol.get(TypeAlcohol.id==id)
		type_alcohol.delete_instance()
	except TypeAlcohol.DoesNotExist:
		pass
	db.close()


