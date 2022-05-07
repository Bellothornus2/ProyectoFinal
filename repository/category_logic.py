class Item:
    def __init__(self, name, quality, sell_in):
        self.name = name
        self.quality = quality
        self.sell_in = sell_in

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.quality, self.sell_in)


class ConjuredItem(Item):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in > 0:
            self.quality += -2
        elif self.sell_in < 0:
            self.quality += -4

        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1


class NormalItem(Item):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in > 0:
            self.quality += -1
        elif self.sell_in < 0:
            self.quality += -2
        if self.quality < 0:
            self.quality = 0
        self.sell_in -= 1


class Sulfuras(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        self.quality = 80


class AgedBrie(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in >= 0:
            self.quality += 1
        elif self.sell_in < 0:
            self.quality += 2

        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1


class Backstage(NormalItem):
    def __init__(self, name, quality, sell_in):
        Item.__init__(self, name, quality, sell_in)

    def update_quality(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in > 5:
            self.quality += 2
        elif self.sell_in > 0:
            self.quality += 3
        elif self.sell_in == 0:
            self.quality = 0

        if self.quality > 50:
            self.quality = 50
        self.sell_in -= 1
