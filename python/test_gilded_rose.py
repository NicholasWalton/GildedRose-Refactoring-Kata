# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


@pytest.fixture
def item(request, sell_in, quality):
    name = request.node.get_closest_marker("item_name").args[0]
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return items[0]


@pytest.mark.item_name("foo")
@pytest.mark.parametrize("sell_in,quality", ((0, 0),))
def test_foo(item):
    assert "foo" == item.name


@pytest.mark.item_name("Sausage")
@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 9), (1, 10, 9), (0, 10, 8), (-5, 20, 18), (10, 0, 0)),
)
def test_generic_item_ages(item, sell_in, expected_quality):
    assert sell_in - 1 == item.sell_in
    assert expected_quality == item.quality


@pytest.mark.item_name("Conjured Sausage")
@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 8), (1, 10, 8), (0, 10, 6), (-5, 20, 16), (10, 0, 0)),
)
def test_generic_conjured_item_ages(item, sell_in, expected_quality):
    assert sell_in - 1 == item.sell_in
    assert expected_quality == item.quality


@pytest.mark.item_name("Aged Brie")
@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 11), (1, 10, 11), (0, 10, 12), (-5, 20, 22), (10, 50, 50)),
)
def test_aged_brie_ages(item, sell_in, expected_quality):
    assert sell_in - 1 == item.sell_in
    assert expected_quality == item.quality


@pytest.mark.item_name("Sulfuras, Hand of Ragnaros")
@pytest.mark.parametrize(
    "sell_in,quality",
    ((5, 10), (1, 10), (0, 10), (-5, 20), (5, 80)),
)
def test_sulfuras_ages(item, sell_in, quality):
    assert sell_in == item.sell_in
    assert quality == item.quality


@pytest.mark.item_name("Backstage passes to a TAFKAL80ETC concert")
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
def test_backstage_ages(item, sell_in, expected_quality):
    assert sell_in - 1 == item.sell_in
    assert expected_quality == item.quality
