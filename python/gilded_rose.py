# -*- coding: utf-8 -*-
MINIMUM_QUALITY = 0
CONJURED = "Conjured"
MAX_QUALITY = 50


class ItemType():
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_item_quality(item)

    def _item_quality_modifier(self, quality, modifier):
        intermediate = min(MAX_QUALITY, quality + modifier)
        return max(MINIMUM_QUALITY, intermediate)

    def _update_generic(self, item):
        degredation_rate = -1
        if item.sell_in <= 0:
            degredation_rate *= 2
        if item.name.startswith(CONJURED):
            degredation_rate *= 2

        item.quality = self._item_quality_modifier(item.quality, degredation_rate)

    def _update_item_quality(self, item):
        match item.name:
            case ItemType.AGED_BRIE:
                if item.sell_in > 0:
                    item.quality = self._item_quality_modifier(item.quality, 1)
                else:
                    item.quality = self._item_quality_modifier(item.quality, 2)
            case ItemType.BACKSTAGE_PASSES:
                if item.sell_in > 10:
                    item.quality = self._item_quality_modifier(item.quality, 1)
                elif item.sell_in > 5:
                    item.quality = self._item_quality_modifier(item.quality, 2)
                elif item.sell_in > 0:
                    item.quality = self._item_quality_modifier(item.quality, 3)
                else:
                    item.quality = 0
            case ItemType.SULFURAS:
                item.sell_in += 1
            case _:
                self._update_generic(item)

        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
