"""
Iterator
========

(Page. 249)

Intent
------
Provide a way to access the elements of an aggregate object sequentially
without exposing its underlying representations.

Motivation
----------
An aggregate object such as a list should give you a way to access its
elements without exposing its internal structure. Moreover, you might
want to traverse the list in different ways, depending on what you want
to accomplish. But you probably don't want to bloat the List interface
with operations for different traversals, even if you could anticipate
the ones you will need. You might also need to have more than one
traversal pending on the same list.

The Iterator class defines an interface for accessing the list's
elements. An iterator object is responsible for keeping track of the
current element; that is, it knows which elements have been traversed
already.

Separating the traversal mechanism from the List object lets use define
iterators for different traversal policies without enumerating then in
the List interface.

The remaining problem is how to create the iterator, we make the list
objects responsible for creating their corresponding iterator.

Applicability
-------------
Use the iterator pattern
 - To access an aggregate object's contents without exposing its internal
   representation.
 - To support multiple traversals of aggregate objects.
 - To provide a uniform interface for traversing different aggregate
   structures.

Consequences
------------
1. It supports variations in the traversal of an aggregate.
2. Iterators simplify the Aggregate interface.
3. More than one traversal can be pending on an aggregate.
"""

# Traverses a container and accesses the container's elements.

import random


class Slime:

    def __init__(self, name, hp):
        self._hp = hp
        self._name = name
        self.alive = True

    @property
    def check_alive(self):
        if not self.alive:
            print("{} has already fainted.".format(self._name))
            return False
        return True

    def affected_by(self, move):
        if self.check_alive:
            for damage in move:
                print("{} was hit with {} worth of damage.".format(self._name, damage))
                self._hp -= damage
                if self._hp <= 0:
                    self._hp = 0
                    self.alive = False
                    print("{} has fainted.".format(self._name))
                    break


class Rogue:

    def __init__(self, hp, attack):
        self._hp = hp
        self._attack = attack

    def fury_swipe(self):
        times = random.randint(2, 5)
        damage = self._attack / 2
        return multi_hit_move(damage, times)

    def back_stab(self):
        damage = self._attack * 2
        return risky_move(damage)


def risky_move(damage):
    risk = random.randint(1, 100)
    if risk > 90:
        damage *= 10
        yield damage
    else:
        yield 0


def multi_hit_move(damage, count):
    for _ in range(count):
        yield damage


if __name__ == '__main__':
    rogue = Rogue(10, 5)
    slime = Slime("Green Slime", 20)

    slime.affected_by(rogue.fury_swipe())
    slime.affected_by(rogue.fury_swipe())

    print("{} health remaining: {}".format(slime._name, slime._hp))

    slime.affected_by(rogue.back_stab())
