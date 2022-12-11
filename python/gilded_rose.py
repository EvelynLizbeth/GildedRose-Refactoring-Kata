# -*- coding: utf-8 -*-
sulf="Sulfuras, Hand of Ragnaros"
class GildedRose(object):

    def __init__(self, items):
        self.items=items
    
    def update_quality(self):
        for item in self.items:
            if item.name=="Aged brie":
                self.aged_brie(item)
            elif item.name==sulf:
                self.sulfuras(item)
            elif item.name=="Backstage passes to a TAFKAL80ETC concert":
                self.backstage(item)
            elif item.name=="Conjured Mana Cake":
                self.conjured(item)
            else:
                self.other_items(item)

            if item.quality<0:
                item.quality=0
            if item.quality>50 and  item.name != sulf:
                item.quality=50
            if item.name!=sulf:
                item.sell_in-=1

    def aged_brie(self,item):
        sell_in_= item.sell_in
        if sell_in_ >0:
            item.quality +=1
        else:
            item.quality +=2
        
    def sulfuras(self,item):
        self.sell_in=item.sell_in
        self.quality=item.quality

    def backstage(self,item):
        sell_in_= item.sell_in
        if sell_in_ >0:
            item.quality +=1
        elif sell_in_<11:
            item.quality +=2
        elif sell_in_<6:
            item.quality +=3
        else:
            item.quality=0
        
    def conjured(self,item):
        item.quality -=2
        
    def other_items(self,item):
        sell_in_=item.sell_in
        if sell_in_<0:
            item.quality-=2
        else:
            item.quality-=1
        
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality) 