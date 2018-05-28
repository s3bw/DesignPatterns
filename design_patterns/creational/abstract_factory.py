"""
Abstract Factory
================

(Page. 83)

Intent
------
Provide an interface for creating families of related or dependant objects
without specifying their concrete classes.

Motivation
----------
Instantiating look-and-feel-specific classes of widgets throughout the
application makes it hard to change the look and feel later.

This problem is solved by defining an abstract WidgetFactory call that
declares an interface for creating each basic kind of widget.

There is a concrete subclass of WidgetFactory for each look-and-feel
standard, the subclasses implements the operations to create the
appropriate widget. This also enforces dependencies encapsulated by
each concrete subclass.

Applicability
-------------
Use the Abstract Factory pattern when
 - A system should be independent of how its products are created, composed
   and represented.
 - A system should be configured with one of multiple families of products.
 - A family of related product objects is designed to be used together,
   and you need to enforce this constraint.
 - You want to provide a class library of products, and you want to reveal
   just their interfaces, not their implementations.

Consequences
------------
1. It isolates concrete classes.
2. It makes exchanging product families easy.
3. It promotes consistency among products.
4. Supporting new kinds of products is difficult.
"""

import random


class FishShop:
    """ A fish shop"""

    def __init__(self, animal_factory=None):
        #: fish_factory is our abstract factory. We can set it at will.
        self.fish_factory = animal_factory

    def show_pet(self):
        """ Creates and shows a pet using the abstract factory
        """
        fish = self.fish_factory()
        print("We have a lovely {}".format(fish))
        print("This is a {} {}".format(fish.colour, fish))


class Guppy:
    colours = ["blue", "white", "green"]

    @property
    def colour(self):
        return random.choice(self.colours)

    def __str__(self):
        return "Guppy"


class Betta:
    colours = ["yellow", "pink", "black"]

    @property
    def colour(self):
        return random.choice(self.colours)

    def __str__(self):
        return "Betta"


# Additional factories:
def random_fish():
    return random.choice([Guppy, Betta])()


if __name__ == "__main__":
    # A shop that sells only guppies
    guppy_shop = FishShop(Guppy)
    guppy_shop.show_pet()
    print("")

    # A shop selling random fish
    fish_shop = FishShop(random_fish)
    for _ in range(3):
        fish_shop.show_pet()
        print("=" * 20)
