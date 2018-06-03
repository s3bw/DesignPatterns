"""
Decorator
=========

(Page. 169)

Intent
------
Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending functionality.

Motivation
----------
Sometimes we want to add responsibilities to individual objects, not to an
entire class.

A more flexible approach is to enclose the component in another object that
adds the functionality. The enclosing object is called a decorator. The
decorator conforms to the interface of the component it decorates so that
its presence is transparent to the component's clients.

The decorator forwards requests to the component and may perform additional
actions *before* or *after* forwarding. Transparency lets you nest decorators
recursively, thereby allowing an unlimited number of added responsibilities.

Applicability
-------------
Use Decorator
 - To add responsibilities to individual objects dynamically and
   transparently, that is, without affecting other objects.
 - For responsibilities that can be withdrawn
 - When extension by subclassing is impractical. Sometimes a large number
   of independent extensions are possible and would produce an explosion
   of subclassies to support every combination. Or a class definition may
   by hidden or otherwise unavailable for subclassing.

Consequences
------------
1. More flexibility than static inheritance
2. Avoids feature-laden classes high up in the hierarchy
3. A decorator and its component aren't identical
4. Lots of little objects
"""

# The Decorator pattern is used to dynamically add a new feature to an
# object without changing its implementation.

class Elf:
    """Base character"""
    def __init__(self, name, hp, strength):
        self._name = name
        self._hp = hp
        self._strength = strength

    def attack(self):
        return self._strength

    def health(self):
        return self._hp

    @property
    def name(self):
        return self._name


class KnightPromotion(Elf):
    """Gives a character the knight promotion"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def attack(self):
        return self._wrapped.attack() * 2

    @property
    def _name(self):
        return "Knight {}".format(self._wrapped._name)


if __name__ == '__main__':
    elron = Elf("Elron", 10, 8)

    print(elron.name)
    print("Attack:", elron.attack())

    print("\nThe Elf has been promoted.")
    elron = KnightPromotion(elron)
    print(elron.name)
    print("Attack:", elron.attack())
