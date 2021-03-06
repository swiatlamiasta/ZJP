# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_one_item(item)

    def update_one_item(self, item):
        if item.name == "Aged Brie":
            item.__class__ = Brie
        elif item.name == "Sulfuras, Hand of Ragnaros":
            item.__class__ = Sulfuras
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.__class__ = BackstagePass
        elif item.name == "Conjured Mana Cake":
            item.__class__ = Conjured
        item.update(item)



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def has_expired(self, item):
        return item.sell_in < 0

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def increment_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def update(self, item):
        self.decrement_quality(item)
        item.sell_in = item.sell_in - 1
        if self.has_expired(item):
            self.decrement_quality(item)


class Brie(Item):

    def update(self, item):
        self.increment_quality(item)
        item.sell_in = item.sell_in - 1
        if self.has_expired(item):
            self.increment_quality(item)
            item.sell_in = item.sell_in - 1


class BackstagePass(Item):

    def update(self, item):
        self.increment_quality(item)
        item.sell_in = item.sell_in - 1
        if item.sell_in < 11:
            self.increment_quality(item)
        if item.sell_in < 6:
            self.increment_quality(item)
        if self.has_expired(item):
            item.quality = 0


class Sulfuras(Item):

    def update(self, item):
        pass


class Conjured(Item):
    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 2
