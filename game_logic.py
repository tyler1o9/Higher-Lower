import random


def shuffle_deck():
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = list(range(1, 14))  # 1 = Ace, 11 = Jack, 12 = Queen, 13 = King
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck


def evaluate_guess(current_card, next_card, guess):
    if guess == "higher" and next_card["value"] > current_card["value"]:
        return True
    if guess == "lower" and next_card["value"] < current_card["value"]:
        return True
    return False
