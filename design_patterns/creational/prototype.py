"""
Prototype
=========

(Page. 113)

Intent
------
Specify the kinds of objects to create using a prototypical instance,
and create new objects by copying this prototype.

Motivation
----------
Suppose a framework provides an abstract Graphic class for graphical
components, like notes and staves. Also the framework also predefines
a GraphicTool subclass for tools that create instances of graphical
objects.

The solution lies in making GraphicTool create a new Graphic by copying
or "cloning" and instance of a Graphic subclass. We call this instance
a prototype. So each tool for creating a music object is an instance
of GraphicTool that's initialized with a different prototype.

We can use the Prototype pattern to reduce the number of classes even
further. We have separate classes for whole notes and half notes, which
is unnecessary. Instead they could be instances of the same class
initialized differently

This can reduce the number of classes in the system dramatically. It
also makes it easier to add a new kind of note to the editor.

Applicability
-------------
Use the Prototype pattern when a system should be independent of how its
products are created, composed, and represented; and
 - When the classes to instantiate are specified at run-time, for example
   by dynamically loading; or
 - To avoid building a class hierarchy of factories that parallels the
   class hierarchy of products; or
 - When instances of a class can have one of only a few different
   combinations of state. It may be more convenient to install a
   corresponding number of prototypes and clone them rather than instantiating
   the class manually, each time with the appropriate state

Consequences
------------
1. Adding and removing products at run-time.
2. Specifying new objects by varying values.
3. Specifying new objects by varying structure.
4. Reduced subclassing.
5. Configuring an application with classes dynamically.
"""


# Abstract Prototype
class WeaponType:

    name = 'n iron'

    def clone(self, **attrs):
        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class PrototypeRegistry:
    """ aka Dispatcher, aka Manager.
    When the number of prototypes in a system isn't fixed, keep a registry of
    available prototypes. Clients won't manage prototypes themselves by will
    store and retrieve them from the registry. A client will ask the registry
    for a prototype before cloning it.
    """
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        """Get all objects"""
        return self._objects

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]


def main():
    # Prototype Manager
    registry = PrototypeRegistry()

    # Abstract Prototype
    prototype_weapons = WeaponType()

    # Concrete Prototypes
    default_weapons = prototype_weapons.clone(rarity="common")
    registry.register_object(default_weapons.name, default_weapons)

    wood_weapons = prototype_weapons.clone(name=" wood", rarity="uncommon")
    registry.register_object(wood_weapons.name, wood_weapons)

    steel_weapons = prototype_weapons.clone(name=" steel", rarity="rare")
    registry.register_object(steel_weapons.name, steel_weapons)

    for weapon_type, weapon in registry.get_objects().items():
        print("A{} weapon is {}".format(weapon_type, weapon.rarity))


if __name__ == "__main__":
    main()
