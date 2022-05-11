from ast import In
from peewee import SqliteDatabase
from services.alcohol import Alcohol
from services.ingredient import Ingredient
from services.ingredient_alcohol import IngredientAlcohol
from services.subtype_alcohol import SubTypeAlcohol
from services.type_alcohol import TypeAlcohol
def initialize_db():
	pass
	'''
    # enlazamos el modelo "item" a la base de datos "Ollivanders.sqlite"
    db = Database("Ollivanders.sqlite")
    Item.db = db
    # eliminamos los datos de la base de datos.
    db.execute("delete from Item")
    # guardamos todos lo items que queremos
    Item("Aged Brie", 20, 10).save()
    Item("Backstage2", 20, 10).save()
    Item("Backstage3", 10, 3).save()
    Item("Conjured Mana Cake", 40, 20).save()
    Item("Dexterity Vest +5", 1, 45).save()
    Item("Sulfuras", 3, 99).save()
    # y hacemos el commit a la base de datos ya que no es automático
    db.commit()
    # rechazamos la conexion para limpiar huellas
    db.close()
    # nuestra maqueta a recrear
    """ 
        ["Aged Brie", 20, 10],
        ["Backstage2", 20, 10],
        ["Backstage3", 10, 3],
        ["Conjured Mana Cake", 40, 20],
        ["Dexterity Vest +5", 1, 45],
        ["Sulfuras", 3, 99], 
    """
	'''
def create_tables():
	db = SqliteDatabase('ImpetuYam.sqlite')
	db.create_tables([Alcohol,Ingredient,IngredientAlcohol,SubTypeAlcohol,TypeAlcohol])