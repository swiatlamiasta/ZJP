# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_one_item(item)

    def update_one_item(self, item):
        self.update_part1(item)
        self.update_part2(item)
        if self.has_expired(item):
            self.update_expired(item)

    def has_expired(self, item):
        return item.sell_in < 0

    def update_expired(self, item):
        if item.name == "Aged Brie":
            self.increment_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif item.name == "Sulfuras, Hand of Ragnaros":
            pass
        else:
            self.decrement_quality(item)

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1

    def update_part2(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def update_part1(self, item):
        if item.name == "Aged Brie":
            self.increment_quality(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.increment_quality(item)
            if item.sell_in < 11:
                self.increment_quality(item)
            if item.sell_in < 6:
                self.increment_quality(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            pass
        else:
            self.decrement_quality(item)

    def increment_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
