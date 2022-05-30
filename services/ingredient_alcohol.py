from peewee import SqliteDatabase,ForeignKeyField,Model,fn

from services.alcohol import Alcohol
from services.ingredient import Ingredient

db = SqliteDatabase('ImpetuYam.sqlite')

class IngredientAlcohol(Model):
	alcohol_id = ForeignKeyField(Alcohol)
	ingredient_id = ForeignKeyField(Ingredient)
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
			"alcohol_id":item.alcohol_id.id,
			"ingredient_id":item.ingredient_id.id
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
				"alcohol_id":ingredient_alcohol_db.alcohol_id.id,
				"ingredient_id":ingredient_alcohol_db.ingredient_id.id
			}
		}
		db.close()
	except IngredientAlcohol.DoesNotExist:
		answer = {"error": "the record can't be retrieved"}
	return answer

def get_alcohol_by_ingredient(ingredient_id):
	try:
		db.connect()
		ingredient_alcohol_db = IngredientAlcohol.select().where(IngredientAlcohol.ingredient_id == ingredient_id)
		data = {}
		data["data"] = []
		list_alcohol_id = []
		for item in ingredient_alcohol_db:
			list_alcohol_id.append(item.alcohol_id.id)
		alcohol_db = Alcohol.select().where(Alcohol.id.in_(list_alcohol_id))
		for item in alcohol_db:
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
	except:
		data = {"error":"something went wrong"}
	return data

def create_ingredient_alcohol(alcohol_id,ingredient_id):
	db.connect()
	try:
		ingredient_alcohol = IngredientAlcohol.create(
			alcohol_id = alcohol_id,
			ingredient_id = ingredient_id
		)
		ingredient_alcohol.save()
		db.commit()
	except:
		pass
	db.close()

def update_ingredient_alcohol(id, alcohol_id, ingredient_id):
	db.connect()
	try:
		ingredient_alcohol = IngredientAlcohol.get(IngredientAlcohol.id==id)
		ingredient_alcohol.alcohol_id = alcohol_id
		ingredient_alcohol.ingredient_id = ingredient_id
		ingredient_alcohol.save()
		db.commit()
	except IngredientAlcohol.DoesNotExist:
		pass
	db.close()

def delete_ingredient_alcohol(id):
	db.connect()
	try:
		ingredient_alcohol = IngredientAlcohol.get(IngredientAlcohol.id==id)
		ingredient_alcohol.delete_instance()
	except IngredientAlcohol.DoesNotExist:
		pass
	db.close()


