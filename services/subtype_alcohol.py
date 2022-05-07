from peewee import SqliteDatabase,CharField,ForeignKeyField,Model,fn

db = SqliteDatabase('ImpetuYam.sqlite')

class TypeAlcohol(Model):
	type_alcohol_id = ForeignKeyField()
	name = CharField()
	class Meta:
		database = db

def get_subtype_alcohol_last_id():
	db.connect()
	query = TypeAlcohol.select(fn.MAX(TypeAlcohol.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_subtype_alcohol():
	db.connect()
	list_subtype_alcohol = TypeAlcohol.select()
	data = {}
	data["data"] = []
	for item in list_subtype_alcohol:
		data["data"].append({
			"id":item.id,
			"name":item.name,
			"type_alcohol_id":item.type_alcohol_id
		})
	db.close()
	return data

def get_subtype_alcohol_id(subtype_alcohol_id):
	try:
		db.connect()
		subtype_alcohol_db = TypeAlcohol.get(TypeAlcohol.id == subtype_alcohol_id)
		answer = {
			"data":{
				"id":subtype_alcohol_db.id,
				"name":subtype_alcohol_db.name,
				"type_alcohol_id":subtype_alcohol_db.type_alcohol_id
			}
		}
		db.close()
	except ValueError:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_subtype_alcohol(name,type_alcohol_id):
	db.connect()
	subtype_alcohol = TypeAlcohol.create(
		name = name,
		type_alcohol_id = type_alcohol_id
	)
	subtype_alcohol.save()
	db.commit()
	db.close()

def update_subtype_alcohol(id, name, type_alcohol_id):
	db.connect()
	subtype_alcohol = TypeAlcohol.get(TypeAlcohol.id==id)
	subtype_alcohol.name = name
	subtype_alcohol.type_alcohol_id = type_alcohol_id
	subtype_alcohol.save()
	db.commit()
	db.close()

def delete_subtype_alcohol(id):
	db.connect()
	subtype_alcohol = TypeAlcohol.get(TypeAlcohol.id==id)
	subtype_alcohol.delete_instance()
	db.close()


