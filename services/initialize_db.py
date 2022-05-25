from peewee import SqliteDatabase
from services.alcohol import Alcohol
from services.ingredient import Ingredient
from services.ingredient_alcohol import IngredientAlcohol
from services.subtype_alcohol import SubTypeAlcohol
from services.type_alcohol import TypeAlcohol
from services.user import User
from services.address import Address
from services.credit_card import CreditCard
from services.order import Order
from services.order_line import OrderLine
from services.review import Review

def initialize_db():
	pass

def create_tables():
	db = SqliteDatabase('ImpetuYam.sqlite')
	#db.create_tables([Alcohol,Ingredient,IngredientAlcohol,SubTypeAlcohol,TypeAlcohol])
	#db.create_tables([User])
	'''db.create_tables([
		CreditCard,
		Order,
		OrderLine,
		Review
	])'''
	#db.create_tables([Address])