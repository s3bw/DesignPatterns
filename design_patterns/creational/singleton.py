"""
Singleton
=========

(Page. 123)

Intent
------
Ensure a class only has one instance, and provide a global point of
access to it.

Motivation
----------
It's important for some classes to have exactly one instance. E.g. There
should be only one file system and one window manager. An accounting
system will be dedicated to serving one company.

How do we ensure that a class has only one instance and that the instance
is easily accessible? A global variable makes an object accessible, but
it doesn't keep you from instantiating multiple objects.

A better solution is to make the class itself responsible for keeping track
of it's sole instance. The class can ensure that no other instance can be
created (by intercepting request to create new objects).

Applicability
-------------
Use the Singleton pattern when
 - There must be exactly one instance of a class, and it must be accessible
   to clients from a well-known access point.
 - When the sole instance should be extensible by subclassing, and clients
   should be able to use an extended instance without modifying their code.

Consequences
------------
1. Controlled access to sole instance
2. Reduced name space.
3. Permits refinement of operations and representation
4. Permits a variable number of instances.
5. More flexible than class operations
"""

# A pythonic way of Singleton implementation is does using a Borg Pattern
# instead of only having one instance, there are multiple that share the
# same state.

class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print("rm1: {0}".format(rm1))
    print("rm2: {0}".format(rm2))

    rm2.state = "Zombie"

    print("rm1: {0}".format(rm1))
    print("rm2: {0}".format(rm2))
