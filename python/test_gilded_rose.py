# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


def create_and_update_rose(name, sell_in, quality):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return items


@pytest.mark.parametrize("name", ("foo",))
def test_foo(name):
    items = create_and_update_rose(name, 0, 0)
    assert name == items[0].name


@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 9), (1, 10, 9), (0, 10, 8), (-5, 20, 18), (10, 0, 0)),
)
def test_generic_item_ages(sell_in, quality, expected_quality):
    items = create_and_update_rose("Sausage", sell_in, quality)
    assert sell_in - 1 == items[0].sell_in
    assert expected_quality == items[0].quality


@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 11), (1, 10, 11), (0, 10, 12), (-5, 20, 22), (10, 50, 50)),
)
def test_aged_brie_ages(sell_in, quality, expected_quality):
    items = create_and_update_rose("Aged Brie", sell_in, quality)
    assert sell_in - 1 == items[0].sell_in
    assert expected_quality == items[0].quality


@pytest.mark.parametrize(
    "sell_in,quality,expected_quality",
    ((5, 10, 10), (1, 10, 10), (0, 10, 10), (-5, 20, 20)),
)
def test_sulfuras_ages(sell_in, quality, expected_quality):
    items = create_and_update_rose("Sulfuras, Hand of Ragnaros", sell_in, quality)
    assert sell_in == items[0].sell_in
    assert expected_quality == items[0].quality


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
def test_backstage_ages(sell_in, quality, expected_quality):
    items = create_and_update_rose(
        "Backstage passes to a TAFKAL80ETC concert", sell_in, quality
    )
    assert sell_in - 1 == items[0].sell_in
    assert expected_quality == items[0].quality
