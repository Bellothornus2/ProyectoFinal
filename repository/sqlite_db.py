from .objects_temp import Item
from orm import Database


def item_manager():
    database = Database("Ollivanders.sqlite")
    manager = Item.manager(database)
    return manager
