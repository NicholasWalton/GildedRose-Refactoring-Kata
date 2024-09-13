# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


@pytest.fixture
def updated_item(name, sell_in, quality):
    item = Item(name, sell_in, quality)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    return item


@pytest.mark.parametrize("name,sell_in,quality", (("item_name", 0, 0),))
def test_name(updated_item):
    assert updated_item.name == "item_name"


class GildedRoseSuite:
    @staticmethod
    def test_item(updated_item, sell_in, expected_quality):
        assert updated_item.sell_in == sell_in - 1
        assert updated_item.quality == expected_quality


@pytest.mark.parametrize("name", ("Sausage",))
@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 9), (1, 10, 9), (0, 10, 8), (-5, 20, 18), (10, 0, 0)),
)
class TestGenericItem(GildedRoseSuite):
    pass


@pytest.mark.parametrize("name", ("Conjured Sausage",))
@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 8), (1, 10, 8), (0, 10, 6), (-5, 20, 16), (10, 0, 0)),
)
class TestGenericConjuredItem(GildedRoseSuite):
    pass


@pytest.mark.parametrize("name", ("Aged Brie",))
@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    (
        (5, 10, 11),
        (1, 10, 11),
        (0, 10, 12),
        (-5, 20, 22),
        (10, 50, 50),
    ),
)
class TestAgedBrie(GildedRoseSuite):
    pass


@pytest.mark.parametrize("name", ("Sulfuras, Hand of Ragnaros",))
@pytest.mark.parametrize(
    "sell_in,quality", ((5, 10), (1, 10), (0, 10), (-5, 20), (5, 80))
)
def test_sulfuras(updated_item, sell_in, quality):
    assert updated_item.sell_in == sell_in
    assert updated_item.quality == quality


@pytest.mark.parametrize("name", ("Backstage passes to a TAFKAL80ETC concert",))
@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    (
        (11, 10, 11),
        (9, 10, 12),
        (5, 10, 13),
        (1, 10, 13),
        (0, 10, 0),
        (-5, 20, 0),
        (5, 49, 50),
        (5, 50, 50),
    ),
)
class TestBackstagePasses(GildedRoseSuite):
    pass
