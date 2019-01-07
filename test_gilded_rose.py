# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item_quality_and_expiration_date(self):
        items = [Item("Random item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_normal_item_quality_after_expiration_date(self):
        items = [Item("Random item", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_normal_item_quality_never_negative(self):
        items = [Item("Random item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_quality_goes_up_for_improving_products(self):
        items = []
        items.append(Item("Aged Brie", 20, 30))
        items.append(Item("Backstage passes to a TAFKAL80ETC concert", 15, 20))
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = [
            {'sell_in': 19, 'quality': 31},
            {'sell_in': 14, 'quality': 21},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    def test_quality_never_higher_than_50(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)
        self.assertEqual(10, items[0].sell_in)

    def test_backstage_pass_within_10_days(self):
        items = []
        items.append(Item("Backstage passes to a TAFKAL80ETC concert", 5, 20))
        items.append(Item("Backstage passes to a TAFKAL80ETC concert", 10, 10))
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = [
            {'sell_in': 4, 'quality': 23},
            {'sell_in': 9, 'quality': 12},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

    def test_pass_after_expiration_date(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)


    def test_conjured_item(self):
        items = []
        items.append(Item("Conjured Mana Cake", 5, 20))
        items.append(Item("Conjured Mana Cake", 0, 10))
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = [
            {'sell_in': 4, 'quality': 18},
            {'sell_in': -1, 'quality': 6},
        ]

        for index, expectation in enumerate(expected):
            item = items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])


if __name__ == '__main__':
    unittest.main()
