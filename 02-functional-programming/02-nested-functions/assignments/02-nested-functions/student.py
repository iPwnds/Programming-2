from util import count, indices_of

def count_older_than(people, min_age):
    # counts the number of people who are older than min_age.
    return count(people, lambda person: person.age >= min_age)

def indices_of_cards_with_suit(cards, suit):
    # returns the indices of all the Cards whose suit equals suit.
<<<<<<< HEAD
    return indices_of(cards, lambda card: card.suit == suit)
=======
    return indices_of(cards, lambda card: card.suit == suit)
>>>>>>> ed8a254985fdbea0724333353397ffdce5e6b793
