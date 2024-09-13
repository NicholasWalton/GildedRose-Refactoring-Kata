# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


@pytest.fixture
def item(name, sell_in, quality):
    item = Item(name, sell_in, quality)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    return item


@pytest.mark.parametrize("name,sell_in,quality", (("foo", 0, 0),))
def test_foo(item):
    assert "foo" == item.name


@pytest.mark.parametrize(
    "name,sell_in,quality,expected_quality",
    (
        [
            ("Sausage", *vals)
            for vals in ((5, 10, 9), (1, 10, 9), (0, 10, 8), (-5, 20, 18), (10, 0, 0))
        ]
        + [
            ("Conjured Sausage", *vals)
            for vals in ((5, 10, 8), (1, 10, 8), (0, 10, 6), (-5, 20, 16), (10, 0, 0))
        ]
        + [
            ("Aged Brie", *vals)
            for vals in (
                (5, 10, 11),
                (1, 10, 11),
                (0, 10, 12),
                (-5, 20, 22),
                (10, 50, 50),
            )
        ]
        + [
            ("Backstage passes to a TAFKAL80ETC concert", *vals)
            for vals in (
                (11, 10, 11),
                (9, 10, 12),
                (5, 10, 13),
                (1, 10, 13),
                (0, 10, 0),
                (-5, 20, 0),
                (5, 49, 50),
                (5, 50, 50),
            )
        ]
    ),
)
def test_item(item, sell_in, expected_quality):
    assert sell_in - 1 == item.sell_in
    assert expected_quality == item.quality


@pytest.mark.parametrize(
    "name,sell_in,quality",
    [
        ("Sulfuras, Hand of Ragnaros", *vals)
        for vals in ((5, 10), (1, 10), (0, 10), (-5, 20), (5, 80))
    ],
)
def test_sulfuras_ages(item, sell_in, quality):
    assert sell_in == item.sell_in
    assert quality == item.quality
