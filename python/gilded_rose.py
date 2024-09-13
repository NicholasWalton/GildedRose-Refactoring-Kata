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
    def _clamp(value, min_value, max_value):
        return max(min_value, min(value, max_value))

    @staticmethod
    def _clamp_item_quality(new_quality):
        return GildedRose._clamp(new_quality, MINIMUM_QUALITY, MAX_QUALITY)

    @staticmethod
    def _update_generic(item):
        degradation_rate = -1
        if item.sell_in <= 0:
            degradation_rate *= 2
        if item.name.startswith(CONJURED):
            degradation_rate *= 2
        item.quality += degradation_rate

    @staticmethod
    def _update_item_quality(item):
        match item.name:
            case ItemType.AGED_BRIE:
                if item.sell_in > 0:
                    item.quality += 1
                else:
                    item.quality += 2
            case ItemType.BACKSTAGE_PASSES:
                if item.sell_in > 10:
                    item.quality += 1
                elif item.sell_in > 5:
                    item.quality += 2
                elif item.sell_in > 0:
                    item.quality += 3
                else:
                    item.quality = 0
            case ItemType.SULFURAS:
                return
            case _:
                GildedRose._update_generic(item)

        item.sell_in -= 1
        item.quality = GildedRose._clamp_item_quality(item.quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
