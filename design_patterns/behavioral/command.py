"""
Command
=======

(Page. 227)

Intent
------
Encapsulate a request as an object, thereby letting you parameterize clients
with different requests, queue or log requests, and support undoable
operations.

Motivation
----------
Sometimes it's necessary to issue requests to objects without knowing anything
about the operation being requested or the receiver of the request.

The Command pattern lets toolkit objects make requests of unspecified
application objects by turning the request itself into an object. This object
can be stored and passed around like other objects. The key to this pattern
is an abstract Command class, which declares an interface for executing
operations. In the simplest form this interface includes an abstract Execute
operation. Concrete Command subclasses specify a receiver-action pair by
storing the receiver as an instance variable and by implementing Execute
to invoke the request. The receiver has the knowledge required to carry out
the request.

The Command pattern decouples the object that invokes the operation from the
one having the knowledge to perform it. This gives us a lot of flexibility in
designing our user interface.

We can also support command scripting by composing commands into larger ones.
All of this is possible because the object that issues a request only needs
to know how to issue it; it doesn't need to know how the request will be
carried out.

Applicability
-------------
Use the Command pattern when you want to.
 - Parameterize objects by an action to perform. You can express such
   parameterization in a procedural language with a callback function
   that is, a function that's registered somewhere to be called at a
   later point. Commands are an object-oriented replacement for callbacks
 - Specify, queue, and execute requests at different times. A Command
   object can have a lifetime independent of the original request. If
   the receiver of a request can be represented in an address space-
   independent way, then you can transfer a command object for the
   request to a different process and fulfill the request there.
 - Support undo. The Command's execute operation can store state for
   reversing its effect in the command itself. The Command interface
   must have an added Unexecute operation that reverses the effect
   of a previous call to Execute. Execute by traversing this list
   backwards and forwards calling Unexecute and Execute, respectively.
 - Support logging changes so that they can be reapplied in case of a
   system crash. By augmenting the Command interface with load and
   store operations, you can keep a persistent log of changes.
   Recovering from a crash involves reloading logged commands from
   disk and reexecuting them with the Execute operation.
 - Structure a system around high-level operations built in primitives
   operations. Such a structure is common in information systems that
   support transactions. A transaction encapsulates a set of changes
   to data. The Command pattern offers a way to model transactions.
   Commands have a common interface, letting you invoke all transactions
   the same way. The pattern also makes it easy to extend the system
   with new transactions.

Consequences
------------
1. Command decouples the object that invokes the operation from the one
   that knows how to perform it.
2. Commands are first-class objects. They can be manipulated and
   extended like any other object.
3. You can assemble commands into a composite command.
4. It's easy to add new Commands, because you don't have to change
   existing classes.
"""

# Encapsulates all information needed to perform an action or trigger
# an event.


import os
from os.path import lexists


class Wizard:

    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y

    def move(self, co_ords):
        dx, dy = co_ords
        self._x += dx
        self._y += dy
        print(self._name, "moved to {}, {}".format(self._x, self._y))

    def at_origin(self):
        if self._x == 0 and self._y == 0:
            print(self._name, "is at origin.")
        else:
            print(self._name, "is not at origin.")


class MoveCommand:

    direction = {'left': [-1, 0],
                 'right': [+1, 0],
                 'up': [0, +1],
                 'down': [0, -1]}

    def __init__(self, creature, dest):
        self._creature = creature
        self._movement = self.direction[dest]

    def undo(self):
        self._movement = [i*-1 for i in self._movement]
        self._creature.move(self._movement)

    def execute(self):
        self._creature.move(self._movement)


def main():
    command_stack = []

    wizard = Wizard('Gandalf', 0, 0)

    command_stack.append(MoveCommand(wizard, 'up'))
    command_stack.append(MoveCommand(wizard, 'up'))
    command_stack.append(MoveCommand(wizard, 'up'))
    command_stack.append(MoveCommand(wizard, 'right'))
    command_stack.append(MoveCommand(wizard, 'right'))

    wizard.at_origin()
    for cmd in command_stack:
        cmd.execute()
    wizard.at_origin()

    for cmd in reversed(command_stack):
        cmd.undo()
    wizard.at_origin()


if __name__ == "__main__":
    main()
