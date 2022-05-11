from peewee import SqliteDatabase,ForeignKeyField,Model,fn

from services.alcohol import Alcohol
from services.ingredient import Ingredient

db = SqliteDatabase('ImpetuYam.sqlite')

class IngredientAlcohol(Model):
	alcohol_code = ForeignKeyField(Alcohol)
	ingredient_code = ForeignKeyField(Ingredient)
	class Meta:
		database = db

def get_ingredient_alcohol_last_id():
	db.connect()
	query = IngredientAlcohol.select(fn.MAX(IngredientAlcohol.id))
	last_id = query.scalar() ##para tener un registro
	db.close()
	return last_id

def get_all_ingredient_alcohol():
	db.connect()
	list_ingredient_alcohol = IngredientAlcohol.select()
	data = {}
	data["data"] = []
	for item in list_ingredient_alcohol:
		data["data"].append({
			"id":item.id,
			"alcohol_id":item.alcohol_id,
			"ingredient_id":item.ingredient_id
		})
	db.close()
	return data

def get_ingredient_alcohol_id(ingredient_alcohol_id):
	try:
		db.connect()
		ingredient_alcohol_db = IngredientAlcohol.get(IngredientAlcohol.id == ingredient_alcohol_id)
		answer = {
			"data":{
				"id":ingredient_alcohol_db.id,
				"alcohol_id":ingredient_alcohol_db.alcohol_id,
				"ingredient_id":ingredient_alcohol_db.ingredient_id
			}
		}
		db.close()
	except ValueError:
		answer = {"error": "the record can't be retrieved"}
	return answer

def create_ingredient_alcohol(alcohol_id,ingredient_id):
	db.connect()
	ingredient_alcohol = IngredientAlcohol.create(
		alcohol_id = alcohol_id,
		ingredient_id = ingredient_id
	)
	ingredient_alcohol.save()
	db.commit()
	db.close()

def update_ingredient_alcohol(id, alcohol_id, ingredient_id):
	db.connect()
	ingredient_alcohol = IngredientAlcohol.get(IngredientAlcohol.id==id)
	ingredient_alcohol.alcohol_id = alcohol_id
	ingredient_alcohol.ingredient_id = ingredient_id
	ingredient_alcohol.save()
	db.commit()
	db.close()

def delete_ingredient_alcohol(id):
	db.connect()
	ingredient_alcohol = IngredientAlcohol.get(IngredientAlcohol.id==id)
	ingredient_alcohol.delete_instance()
	db.close()


