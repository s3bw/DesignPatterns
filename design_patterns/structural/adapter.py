"""
Adapter
=======

(Page. 135)

Intent
------
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.

Motivation
----------
Sometimes a toolkits class that's designed for reuse isn't reusable only
because its interface doesn't match the domain-specific interface an
application requires.

Meanwhile, an off the shelf user interface toolkit might already provide
the sophistication we need. Ideally we would like to reuse this.

How can existing and unrelated classes work in an application that expects
classes with a different and incompatible interface?

We can do this in two ways:
1. Inheriting the local interface and external implementation
2. Composing the external instance within a local interface.

Applicability
-------------
Use the adapter pattern when
 - You want to use an existing class, and its interface does not match
   the one you need.
 - You want to create a reusable class that cooperates with unrelated
   or unforeseen classes, that is, classes that don't necessarily have
   compatible interfaces.
 - (object adapter only) You need to use several existing subclasses,
   but it's impractical to adapt their interface by subclassing every
   one. An object adapter can adapt the interface of its parent class.

Consequences
------------
1. How much adapting does Adapter do?
2. Pluggable adapters
3. Using two-way adapters to provide transparency
"""

# Useful to integrate classes that couldn't be integrated due to their
# incompatible interfaces.

class Dog:
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat:
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class AnimalAdapter(object):
    """Adapts an object by replacing methods.
    Usage:
    dog = Dog()
    dog = AnimalAdapter(dog, make_noise=dog.bark)
    """
    def __init__(self, obj, **adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original dict"""
        return self.obj.__dict__


def main():
    animals = []

    dog = Dog()
    animals.append(AnimalAdapter(dog, make_noise=dog.bark))

    cat = Cat()
    animals.append(AnimalAdapter(cat, make_noise=cat.meow))

    for animal in animals:
        print("The {} goes {}".format(animal.name, animal.make_noise()))


if __name__ == "__main__":
    main()
