"""
Bridge
======

(Page. 147)

Intent
------
Decouple an abstraction from its implementation so that the two can
vary independently.

Motivation
----------
When an abstraction can have one of several possible implementations,
the usual way to accommodate them is to use inheritance. An abstract
class defines the interface to the abstraction, and concrete subclasses
implement it in different ways. But this approach isn't always flexible
enough. Inheritance binds an implementation to the abstraction
permanently, which makes it difficult to modify, extend, and reuse
abstractions and implementations independently.

Clients should be able to create an instance of an object without
committing to an implementation. Thus we call it a bridge because it
bridges the abstraction and its implementation but lets them vary
independently.

Applicability
-------------
Use the Bridge pattern when:
 - You want to avoid a permanent binding between an abstraction and
   its implementation. This might be the case, for example, when the
   implementation must be selected or switched at run-time.
 - Both the abstractions and their implementations should be extensible
   by subclassing. In this case, the Bridge pattern lets you combine
   the different abstractions and implementations and extend them
   independently.
 - Changes in the implementation of an abstraction should have no
   impact on clients; that is, their code should not have to be
   recompiled.
 - (C++) you want to hide the implementation of an abstraction
   completely from clients. In C++ the representation of a class is
   visible in the class interface.
 - You have a proliferation of classes as shown earlier in the first
   diagram. Such a class hierarchy indicates the need for splitting
   an object into two parts. Rumbaugh uses the term
   "nested generalization" to refer to such class hierarchies.
 - You want to share an implementation among multiple objects
   (perhaps using reference counting), and this fact should be hidden
   from the client. A simple example is Coplien's String class, in
   which multiple objects can share the same string representation.

Consequences
------------
1. Decoupling interface and implementation
2. Improved extensibility
3. Hiding implementation details from clients.
"""


# Decouples an abstraction form its implementation


# ConcreteImplementor 1/3
class NeutralAI:

    def tick(self, name):
        print("The {} is minding his own business.".format(name))


# ConcreteImplementor 2/3
class SleepingAI:

    def tick(self, name):
        print("{} is sleeping.".format(name))


# ConcreteImplementor 3/3
class AngryAI:

    def tick(self, name):
        print("{} is complaining.".format(name))


# Refined Abstraction
class Dwarf:

    def __init__(self, name, status):
        self._name = name
        self._status = status
        self._ai = self.determine_status(status)

    def determine_status(self, status):
        if status == "sleeping":
            return SleepingAI()
        elif status == "neutral":
            return NeutralAI()
        else:
            return AngryAI()

    # low-level i,e, Implementation specific
    def use_turn(self):
        self._ai.tick(self._name)

    # High-level i.e. Abstraction specific
    def wake_up(self):
        if self._status == "sleeping":
            self._status = "awake"
            self._ai = AngryAI()
            print(self._name, "has awoken and is angry")
        else:
            print(self._name, "is already awake")


def main():
    dwarves = (
        Dwarf("dopey", "neutral"),
        Dwarf("grump", "sleeping"),
    )

    for sec in range(3):
        if sec == 1:
            print("A loud bang erupts from outside!!")
        for dwarf in dwarves:
            if sec == 1:
                dwarf.wake_up()
            else:
                dwarf.use_turn()


if __name__ == '__main__':
    main()
