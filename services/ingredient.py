from peewee import SqliteDatabase,CharField,Model,fn

db = SqliteDatabase('ImpetuYam.sqlite')

class Ingredient(Model):
	name = CharField()
	class Meta:
		database = db

def get_ingredient_last_id():
	db.connect()
	query = Ingredient.select(fn.MAX(Ingredient.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_ingredient():
	db.connect()
	list_ingredient = Ingredient.select()
	data = {}
	data["data"] = []
	for item in list_ingredient:
		data["data"].append({
			"id":item.id,
			"name":item.name
		})
	db.close()
	return data

def get_ingredient_id(ingredient_id):
	try:
		db.connect()
		ingredient_db = Ingredient.get(Ingredient.id == ingredient_id)
		answer = {
			"data":{
				"id":ingredient_db.id,
				"name":ingredient_db.name,
			}
		}
		db.close()
	except ValueError:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_ingredient(name):
	db.connect()
	ingredient = Ingredient.create(name=name)
	ingredient.save()
	db.commit()
	db.close()

def update_ingredient(id, name):
	db.connect()
	ingredient = Ingredient.get(Ingredient.id==id)
	ingredient.name = name
	ingredient.save()
	db.commit()
	db.close()

def delete_ingredient(id):
	db.connect()
	ingredient = Ingredient.get(Ingredient.id==id)
	ingredient.delete_instance()
	db.close()


