"""
Chain Of Responsibility
======================

(Page. 217)

Intent
------
Avoid coupling the sender of a request to its receiver by giving more
than one object a chance to handle the request. Chain the receiving
objects and pass the request along the chain until an object handles it.

Motivation
----------
It's natural to organize help information according to its generality-
from the most specific to the most general.

The problem here is that the object that ultimately provides the help
isn't known explicitly to the object that initiates the help request.

The idea of this pattern is to decouple senders and receivers by
giving multiple objects a chance to handle a request. The request gets
passed along a chain of objects until one of them handles it.

The first object in the chain receives the request and either handles it
or forwards it to the next candidate on the chain, which does likewise.
The object that made the request has no explicit knowledge of who will
handle it-we say the request has an implicit receiver

To forward the request along the chain, and ensure receivers remain
implicit, each object on the chain shares a common interface for
handling requests and for accessing its successor on the chain.

As a result, Chain of Responsibility can simplify object interconnections.
Instead of objects maintaining references to all candidate receivers, they
keep a single reference to their successor.

Applicability
-------------
Use a Chain of Responsibility when
 - More than one object may handle a request, and the handler isn't
   known a priori. The handler should be ascertained automatically.
 - You want to issue a request to one of several objects without
   specifying the receiver explicitly.
 - The set of objects that can handle a request should be specified
   dynamically.

Consequences
------------
1. Reduced coupling
2. Added flexibility in assigning responsibilities to objects.
3. Receipt isn't guaranteed.
"""

from abc import ABC
from abc import abstractmethod


class Spell:
    def __init__(self, name):
        self.name = name
        self.chain = ConcreteHandler1(
            ConcreteHandler2(
                ConcreteHandler3(
                    ConcreteHandler4()
                )
            )
        )

    def cast(self, creature):
        self.chain.handle(creature)


class Magician:
    def __init__(self, name, intelligence):
        self.name = name
        self.intelligence = intelligence

    def cast_spell(self, spell):
        print("{} casts {} spell".format(self.name, spell.name))
        spell.cast(self)


class AbstractHandler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, creature):
        reaction = self._handle(creature)
        if not reaction:
            self._successor.handle(creature)

    @abstractmethod
    def _handle(self, spell):
        raise NotImplementedError("Must provide implementation in subclass")


class ConcreteHandler1(AbstractHandler):
    def _handle(self, creature):
        if creature.intelligence < 10:
            print("Spell backfires")
            return True


class ConcreteHandler2(AbstractHandler):
    def _handle(self, creature):
        if creature.intelligence < 20:
            print("Small fire ball is cast")
            return True


class ConcreteHandler3(AbstractHandler):
    def _handle(self, creature):
        if creature.intelligence < 30:
            print("A fire ball blazes across the room")
            return True


class ConcreteHandler4(AbstractHandler):
    def _handle(self, creature):
        print("A Massive column of fire burns through the wall!")
        return True


if __name__ == '__main__':
    fire_spell = Spell("Fire Ball")

    merlin = Magician("Merlin", 8)
    albus = Magician("Albus", 18)
    howl = Magician("Howl", 28)
    gandalf = Magician("Gandalf", 38)

    wizards = [merlin, albus, howl, gandalf]
    for wizard in wizards:
        wizard.cast_spell(fire_spell)
        print("")
