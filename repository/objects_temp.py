from orm import Model


class Item(Model):
    name = str
    sell_in = int
    quality = int

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
