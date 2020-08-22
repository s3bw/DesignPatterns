"""
For python stdlib examples see random.py.

Intent
------
Implicit state management for users of a module.

Motivation
----------
Dealing with shared-state across different areas of the
codebase is difficult. Test will have to share a single
generator and correctly reset its state before the next
test runs.

Instantiating a second copy of the object across threads
would require protection from locks.

Modules as a collection of methods sharing global state
breaks encapsulation.

Applicability
-------------
Use the prebound-method pattern when:
 - Methods require setup of a complex object that could
   be encapsulated by a single bound method.
 - There is a need to reduce the overhead of an instantiated
   object.
 - It can be more desirable for deterministic outcomes
   created from sharing a lone instance.

Consequences
------------
1. Shared state is implicit.
2. Not appropriate for constructors bound to I/O. (These
   should not occur at import time.)

Notes:
------
This is similar to joining a Factory+Singleton pattern.
"""
import random


class Card:
    def __init__(self, name):
        self.rank, self.suit = name


class Deck:
    def __init__(self):
        self.cards = [
            Card("3H"), Card("9S"), Card("AC")
        ]
        self.to_bottom(Card("AD"))

    def shuffle_card(self, card):
        pos = random.randint(0, len(self.cards))
        self.cards.insert(pos, card)

    def to_bottom(self, card):
        self.cards.append(card)

    def peak(self):
        return self.cards[0]

    def draw(self):
        return self.card.pop()


_instance = Deck()

draw = _instance.draw
peak = _instance.peak
shuffle_card = _instance.shuffle
to_bottom = _instance.to_bottom
