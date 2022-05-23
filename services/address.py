#SELECT MAX(ID) AS LastID FROM Persons
from peewee import SqliteDatabase,CharField,TextField,ForeignKeyField,Model,fn

from services.user import User

db = SqliteDatabase('ImpetuYam.sqlite')

class Address(Model):
	street = CharField()
	street_number = CharField()
	floor = CharField()
	door = CharField()
	zip_code = CharField()
	other_data = TextField()
	type_address = CharField() ##Only Send or Bill
	user_id = ForeignKeyField(User)
	class Meta:
		database = db

def get_address_last_id():
	db.connect()
	query = Address.select(fn.MAX(Address.id)) ##para obtener SELECT MAX(id) AS LastID FROM Item
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_address():
	db.connect()
	list_address = Address.select()
	data = {}
	data["data"] = []
	for item in list_address:
		data["data"].append({
			"id":item.id,
			"street":item.street,
			"street_number":item.street_number,
			"floor":item.floor,
			"door":item.door,
			"zip_code":item.zip_code,
			"other_data":item.other_data,
			"type_address":item.type_address,
			"user_id":item.user_id.id
		})
	db.close()
	return data

def get_address_id(address_id):
	try:
		db.connect()
		address_db = Address.get(Address.id == address_id)
		answer = {
			"data":{
				"id":address_db.id,
				"street":address_db.street,
				"street_number":address_db.street_number,
				"floor":address_db.floor,
				"door":address_db.door,
				"zip_code":address_db.zip_code,
				"other_data":address_db.other_data,
				"type_address":address_db.type_address,
				"user_id":address_db.user_id.id
			}
		}
		db.close()
	except Address.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_address(street,street_number,floor,door,zip_code,other_data,type_address,user_id):
	db.connect()
	address = Address.create(
		street=street,
		street_number=street_number,
		floor=floor,
		door=door,
		zip_code=zip_code,
		other_data=other_data,
		type_address=type_address,
		user_id=user_id)
	address.save()
	db.commit()
	db.close()

def update_address(id, street,street_number,floor,door,zip_code,other_data,type_address,user_id):
	db.connect()
	try:
		address = Address.get(Address.id==id)
		address.street = street
		address.street_number = street_number
		address.floor = floor
		address.door = door
		address.zip_code = zip_code
		address.other_data = other_data
		address.type_address = type_address
		address.user_id = user_id
		address.save()
		db.commit()
	except Address.DoesNotExist:
		pass
	db.close()

def delete_address(id):
	db.connect()
	try:
		address = Address.get(Address.id==id)
		address.delete_instance()
	except Address.DoesNotExist:
		pass
	db.close()
