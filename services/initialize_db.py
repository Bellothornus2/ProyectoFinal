from orm import Database
from repository.objects_temp import Item


def initialize_db():
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
