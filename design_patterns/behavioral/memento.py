"""
Memento
=======

(Page. 273)

Intent
------
Without violating encapsulation, capture and externalize an object's internal
state so that the object can be restored to this state later.

Motivation
----------
Sometimes it's necessary to record the internal state of an object. This is
required when implementing checkpoints and undo mechanisms that let users back
out of tentative operations or recover from errors. You must save state
information somewhere so that you can restore objects to their previous state.
But objects normally encapsulate some or all of their state, making it
inaccessible to other objects and impossible to save externally. Exposing this
state would violate encapsulation, which can compromise the application's
reliability and extensibility.

A memento is an object that stores a snapshot of the internal state of another
object- the memento's originator. The undo mechanism will request a memento
from the originator when it needs to checkpoint the originator's state. The
originator initializes the memento with information that characterizes its
current state. Only the originator can store and retrieve information from
the memento- the memento is "opaque" to other objects.

Applicability
-------------
Use the Memento pattern when
 - A snapshot of (some portion of) an object's state must be saved so that it
   can be restored to that state later.
 - A direct interface to obtaining the state would expose implementation details
   and break the object's encapsulation.

Consequences
------------
1. Preserving encapsulation boundaries.
2. It simplifies Originator.
3. Using mementos might be expensive.
4. Defining narrow and wide interfaces.
5. Hidden costs in caring for mementos
"""

# Provides an ability to restore an object to its previous state.

from copy import copy
from copy import deepcopy


def memento(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction:
    """A transaction guard.

    This is, in fact, just syntactic sugar around a memento closure.
    """
    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [memento(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()


class Transactional:
    """Adds transactional semantics to methods. Methods decorated with

    @Transactional will rollback to entry-state upon exceptions.
    """

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transaction(*args, **kwargs):
            state = memento(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e


class NumObj:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = '1111'  # <- invalid value
        self.increment()  # <- will fail and rollback


if __name__ == '__main__':
    num_obj = NumObj(-1)
    print(num_obj)

    a_transaction = Transaction(True, num_obj)
    try:
        for i in range(3):
            num_obj.increment()
            print(num_obj)
        a_transaction.commit()
        print('-- committed')

        for i in range(3):
            num_obj.increment()
            print(num_obj)
        num_obj.value += 'x'  # will fail
        print(num_obj)
    except Exception as e:
        a_transaction.rollback()
        print('-- rolled back')
    print(num_obj)

    print('-- now doing stuff ...')
    try:
        num_obj.do_stuff()
    except Exception as e:
        print('-> doing stuff failed!')
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print(num_obj)
