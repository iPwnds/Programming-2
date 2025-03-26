from util import group_by, partition

def group_by_suit(cards):
    # groups cards by their suit.
    return group_by(cards, lambda card: card.suit)

def group_by_value(cards):
    # groups cards by their value.
    return group_by(cards, lambda card: card.value)

def partition_by_color(cards):
    # splits cards into two lists: the first list contains only black cards, the second list only red cards. The color of a card is determined by its suit: spades and clubs are black, hearts and diamonds are red.
<<<<<<< HEAD
    return partition(cards, lambda card: card.suit in ["spades", "clubs"])
=======
    return partition(cards, lambda card: card.suit in ['clubs', 'spades'])
>>>>>>> ed8a254985fdbea0724333353397ffdce5e6b793
