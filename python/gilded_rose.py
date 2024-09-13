# -*- coding: utf-8 -*-
MINIMUM_QUALITY = 0
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
MAX_QUALITY = 50


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item_quality(item)

    def _item_quality_modifier(self, quality, modifier):
        intermediate = min(MAX_QUALITY, quality + modifier)
        return max(MINIMUM_QUALITY, intermediate)

    def _update_item_quality(self, item):
        if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
            if item.name != SULFURAS:
                item.quality = self._item_quality_modifier(item.quality, -1)
        else:
            item.quality = self._item_quality_modifier(item.quality, 1)
            if item.name == BACKSTAGE_PASSES:
                if item.sell_in < 11:
                    item.quality = self._item_quality_modifier(item.quality, 1)
                if item.sell_in < 6:
                    item.quality = self._item_quality_modifier(item.quality, 1)
        if item.name != SULFURAS:
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE_PASSES:
                    if item.name != SULFURAS:
                        item.quality = self._item_quality_modifier(item.quality, -1)
                else:
                    item.quality = MINIMUM_QUALITY
            else:
                item.quality = self._item_quality_modifier(item.quality, 1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
