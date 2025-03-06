import pytest
import student
from util import Card

from util import group_by, partition


def group_by_suit(cards):
    return group_by(cards, lambda card: card.suit)


def group_by_value(cards):
    return group_by(cards, lambda card: card.value)


def partition_by_color(cards):
    return partition(cards, lambda card: card.suit in ['clubs', 'spades'])



def if_defined(name):
    return pytest.mark.skipif(name not in dir(student), reason=f'{name} not defined in student module')


@if_defined('group_by_suit')
@pytest.mark.parametrize('cards', [
    [],
    [Card(2, 'hearts')],
    [Card(2, 'hearts'), Card(3, 'clubs'), Card(6, 'spades'), Card(9, 'diamonds')],
    [Card(value, suit) for value in range(2, 11) for suit in ['hearts', 'diamonds', 'clubs', 'spades']],
])
def test_group_by_suit(cards):
    expected = group_by_suit(cards)
    actual = student.group_by_suit(cards)
    assert expected == actual


@if_defined('group_by_value')
@pytest.mark.parametrize('cards', [
    [],
    [Card(2, 'hearts')],
    [Card(2, 'hearts'), Card(3, 'clubs'), Card(6, 'spades'), Card(9, 'diamonds')],
    [Card(value, suit) for value in range(2, 11) for suit in ['hearts', 'diamonds', 'clubs', 'spades']],
])
def test_group_by_value(cards):
    expected = group_by_value(cards)
    actual = student.group_by_value(cards)
    assert expected == actual


@if_defined('partition_by_color')
@pytest.mark.parametrize('cards', [
    [],
    [Card(2, 'hearts')],
    [Card(2, 'hearts'), Card(3, 'clubs'), Card(6, 'spades'), Card(9, 'diamonds')],
    [Card(value, suit) for value in range(2, 11) for suit in ['hearts', 'diamonds', 'clubs', 'spades']],
])
def test_partition_by_color(cards):
    expected = partition_by_color(cards)
    actual = student.partition_by_color(cards)
    assert expected == actual
