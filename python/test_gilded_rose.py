# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)

    def test_backstage(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage", items[0].name)
    
    def test_conjured_Mana_Cake(self):
        items = [Item("Conjured Mana Cake", 4, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].sell_in)

    def test_Elixir_of_the_Mongoose(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
    