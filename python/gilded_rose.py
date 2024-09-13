# -*- coding: utf-8 -*-
MINIMUM_QUALITY = 0
CONJURED = "Conjured"
MAX_QUALITY = 50


class ItemType:
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    AGED_BRIE = "Aged Brie"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            GildedRose._update_item_quality(item)

    @staticmethod
    def _item_quality_modifier(item, degradation_rate):
        intermediate = min(MAX_QUALITY, item.quality + degradation_rate)
        item.quality = max(MINIMUM_QUALITY, intermediate)

    @staticmethod
    def _update_generic(item):
        degradation_rate = -1
        if item.sell_in <= 0:
            degradation_rate *= 2
        if item.name.startswith(CONJURED):
            degradation_rate *= 2
        GildedRose._item_quality_modifier(item, degradation_rate)

    @staticmethod
    def _update_item_quality(item):
        match item.name:
            case ItemType.AGED_BRIE:
                if item.sell_in > 0:
                    GildedRose._item_quality_modifier(item, 1)
                else:
                    GildedRose._item_quality_modifier(item, 2)
            case ItemType.BACKSTAGE_PASSES:
                if item.sell_in > 10:
                    GildedRose._item_quality_modifier(item, 1)
                elif item.sell_in > 5:
                    GildedRose._item_quality_modifier(item, 2)
                elif item.sell_in > 0:
                    GildedRose._item_quality_modifier(item, 3)
                else:
                    item.quality = 0
            case ItemType.SULFURAS:
                item.sell_in += 1
            case _:
                GildedRose._update_generic(item)

        item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
