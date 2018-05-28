"""
Builder
=======

(Page. 93)

Intent
------
Separate the construction of a complex object from its representation so
that the same construction process can create different representations.

Motivation
----------
It should be easy to add a new conversion without modifying the reader.
Each kind of converter class takes the mechanism for creating and assembling
a complex object and put it behind an abstract interface. In the example
provided in the book, the builder is defined by subclasses of converters
which are responsible for parsing a document in differing formats (ascii,
TeX and Text), their responsibilities are separate from the reader.

The builder pattern captures all these relationships. Each converter class
is called a builder in the pattern, and the reader is called the director.

Applicability
-------------
Use the Builder pattern when:
 - The algorithm for creating a complex object should be independent of the
   parts that make up the object and how they're assembled.
 - The construction process must allow different representations for the
   object that's constructed.

Consequences
------------
1. It lets you vary a product's internal representation.
2. It isolates code for construction and representation.
3. It gives you finer control over the construction process.
"""

import random


# Abstract Builder
class MonsterBuilder:
    """ Typically there's an abstract Builder class that defines an operation
        for each component that a director may ask it to create. The operations
        do nothing by default. A concrete builder class overrides operations
        for components it's interested in creating.
    """
    def __init__(self):
        self.give_description()
        self.give_equipment()

    def give_description(self):
        raise NotImplementedError

    def give_equipment(self):
        raise NotImplementedError

    def __repr__(self):
        return "{0.description} | Wielding: {0.equipment}".format(self)


# Concrete Builder
class Orc(MonsterBuilder):
    descriptions = [" hungry", "n ugly", "n evil"]

    def give_description(self):
        description = random.choice(self.descriptions)
        self.description = "A{} Orc".format(description)

    def give_equipment(self):
        self.equipment = "phallic sword"


class Goblin(MonsterBuilder):
    descriptions = [" tiny", " greedy", " possessive"]

    def give_description(self):
        description = random.choice(self.descriptions)
        self.description = "A{} Goblin".format(description)

    def give_equipment(self):
        self.equipment = "knife"


# In some very complex cases, it might be desirable to pull out the building
# logic into another function (or a method on another class), rather than being
# in the base class '__init__'. (This leaves you in the strange situation where
# a concrete class does not have a useful constructor)


class ComplexMonster:
    def __repr__(self):
        return "{0.description} | Wielding: {0.equipment}".format(self)


class ComplexDragon(ComplexMonster):
    descriptions = [" mighty", " respected", "n immeasurable"]

    def give_description(self):
        description = random.choice(self.descriptions)
        self.description = "A{} Dragon".format(description)

    def give_equipment(self):
        self.equipment = "Sharp Claws"


def construct_monster(cls):
    monster = cls()
    monster.give_description()
    monster.give_equipment()
    return monster


# Client
if __name__ == "__main__":
    orc = Orc()
    print(orc)

    goblin = Goblin()
    print(goblin)

    # Using an external constructor function:
    complex_dragon = construct_monster(ComplexDragon)
    print(complex_dragon)
