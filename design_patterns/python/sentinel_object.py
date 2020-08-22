"""
For python stdlib examples see logging modules NullHander,
or the functools.lru_cache 'sentinel' for signalling cache
misses.

Intent
------
Separate the identity and value of an object to recognize
it's significance.

Motivation
----------
On a few occasions programmers might want to distinguish
the difference between data being missing and the data
indicating that it does not exist.

For example, I might have a collection of users and their
associated addresses. If a user has not provided their
address we can represent that with None. But if we have
a vagabond user we have no way to distinguish them from
users that haven't provided their address.

Extending summaries for vagabonds and missing addresses
can be tallied as if they were normal address objects.

Sometimes when instantiating a method a variable might
default to 'None' but the method might want to know when
the user has passed 'None' to the method.

Applicability
-------------
Use the sentinel object pattern:
 - When None value will not cut it for differentiating two
   identities of None. (Vagabond and Non-yet-supplied).
 - To improve readability of statements from 'if x is None'
   to 'if x is VAGABOND'.
 - Type consistency
 - To avoid errors and asserting that object are None, this
   can help to alleviate inappropriate method calls on the
   incorrect data types. e.g. str.capitalise().

Consequences
------------
1. Improved readability.
2. Incorrect sentinel values can lead to unintentional
   outcomes. E.g. find returning -1 when not found and
   being used as an index will have result the was not
   intended.
3. An increased number of object identities.
"""


class Item:
    def __init__(self, name, two_handed=False):
        self.name = name
        self._two_handed = two_handed

    @property
    def two_handed(self):
        return self._two_handed


TWO_HANDED = Item("Two Handed Item", two_handed=True)


class Player:
    """Assuming right hand only players."""

    def __init__(self, name):
        self.name = name
        self._slots = {}

    def equip_right_hand(self, item):
        self._equip("right-hand", item)
        if item.two_handed:
            self._equip("left-hand", TWO_HANDED)

    def equip_left_hand(self, item):
        self._equip("left-hand", item)

    def right_hand(self):
        return self._get_equipt("right-hand")

    def left_hand(self):
        return self._get_equipt("left-hand")

    def _equip(self, slot, item):
        if slot in self._slots:
            equip_item = self._slots[slot]
            raise IndexError(f"Failed to equip {item.name}, {equip_item.name} already occupies {slot}")

        self._slots[slot] = item
        print(f"{self.name} equipped {item.name}")

    def _get_equipt(self, slot):
        return self._slots[slot]


# I could have simplified this by setting the slot on the item
# and calling them 'main-hand' and 'off-hand' instead of left
# and right, but that wasn't the point.
if __name__ == "__main__":
    sword = Item("Sword")
    shield = Item("Shield")
    great_sword = Item("Great Sword", two_handed=True)

    player_one = Player("Boromir")
    player_one.equip_right_hand(sword)
    player_one.equip_left_hand(shield)
    # >>>Boromir equipped Sword
    # >>>Boromir equipped Shield

    player_two = Player("Aragorn")
    player_two.equip_right_hand(great_sword)
    player_two.equip_left_hand(shield)
    # >>>Aragorn equipped Great Sword
    # >>>Aragorn equipped Two Handed Item
    # >>>Failed to equip Shield, Two handed item already occupies left-hand
