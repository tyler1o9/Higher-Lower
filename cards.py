import random


def initialize_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = list(range(1, 14))
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck
