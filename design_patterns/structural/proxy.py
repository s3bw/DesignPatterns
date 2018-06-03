"""
Proxy
=====

(Page. 201)

Intent
------
Provide a surrogate or placeholder for another object to control access to it.

Motivation
----------
One reason for controlling access to an object is to defer the full cost of its
creation and initialization until we actually need to use it.

The solution is to use another object, an image proxy, that acts as a stand-in
for the real image.

Applicability
-------------
Proxy is applicable whenever there is a need for a more versatile or
sophisticated reference to an object than a simple pointer. Here are several
common situations in which the Proxy pattern is applicable.
 - A *remote proxy* provides a local representative for an object in a different
   address space.
 - A *virtual proxy* creates expensive objects on demand. The ImageProxy is an
   example of such a proxy.
 - A *protection proxy* controls access to the original object. Protection
   proxies are useful when objects should have different access rights
 - A *smart reference* is a replacement for a bare pointer that performs
   additional actions when an object is accessed.

Consequences
------------
1. Remote Proxy can hide the fact that an object resides in a different address
   space.
2. Virtual Proxy can perform optimizations such as creating an object on demand.
3. Both protection and smart proxy references allow additional housekeeping
   tasks when an object is accessed.
"""

# Provides an interface to resource that is expensive to duplicate

import time


class Elf:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


class Chest:
    def __init__(self, name, contents, lock_level):
        self.name = name
        self.lock_level = lock_level
        self.contents = contents

    def show_contents(self):
        print("{} contains the following:".format(self.name))
        for index, content in enumerate(self.contents):
            print("{}. {}".format(index, content))


# Protection proxy
def access_chest(creature, chest):
    """ In the Proxy pattern, the subject defines the key functionality,
        and the proxy provides (or refuses) access to it.
    """
    if creature.strength >= chest.lock_level:
        print("{} Opened!".format(chest.name))
        chest.show_contents()
    else:
        print("Can't open {}".format(chest.name))
        print("{} doesn't have high enough strength!".format(creature.name))


if __name__ == '__main__':
    wooden_chest = Chest("wooden chest", ["hammer"], 3)
    iron_chest = Chest("iron chest", ["diamond"], 10)
    elron = Elf("elron", 8)

    access_chest(elron, wooden_chest)
    print("")
    access_chest(elron, iron_chest)
