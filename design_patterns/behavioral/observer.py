"""
Observer
========

(Page. 281)

Intent
------
Define a one-to-many dependency between objects so that when one object
changes state, all its dependants are notified and updated
automatically.

Motivation
----------
A common side-effect of partitioning a system into a collection of
cooperating classes is the need to maintain consistency between related
objects. You don't want to achieve consistency by making the classes
tightly coupled, because that reduces their reusability.

There is no reason to limit the number of dependant objects; there may
be any number of different user interfaces to the same data.

The Observer pattern describes how to establish these relationships.
The key objects in this pattern are *subject* and *observer. A subject
may have any number of dependent observers. All observers are notified
whenever the subject undergoes a change in state. In response, each
observer will query the subject to synchronize its state with the
subject's state.

This kind of interaction is also known as *publish-subscribe*. The
subject is the publisher of notifications. It sends out these
notifications without having to know who its observers are. Any number
of observers can subscribe to receive notifications.

Applicability
-------------
Use the Observer pattern in any of the following situations:
 - When an abstraction has two aspects, one dependent on the other.
   Encapsulating these aspects in separate objects lets you vary and
   reuse them independently.
 - When a change to one objects requires changing others, and you don't
   know how many objects need to be changed.
 - When an object should be able to notify other objects without making
   assumptions about who these objects are. In other words, you don't
   want these objects tightly coupled.

Consequences
------------
1. Abstract coupling between Subject and Observer.
2. Support for broadcast communication.
3. Unexpected updates
"""

# Maintains a list of dependants and notifies them of any state changes


class Subject:

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# Example usage
class Data(Subject):

    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer:

    def update(self, subject):
        print("HexViewer: Subject %s has data 0x%x" %
              (subject.name, subject.data))


class DecimalViewer:

    def update(self, subject):
        print("DecimalViewer: Subject %s has data %s" %
              (subject.name, subject.data))


def main():
    data1 = Data('Data 1')
    data2 = Data('Data 2')
    view1 = DecimalViewer()
    view2 = HexViewer()

    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view1)
    data2.attach(view2)

    print("Setting Data 1 = 10")
    data1.data = 10
    print("Setting Data 2 = 15")
    data2.data = 15
    print("Setting Data 1 = 3")
    data1.data = 3
    print("Setting Data 2 = 5")
    data2.data = 5

    print("Detach HexViewer from data1 and data2.")
    data1.detach(view2)
    data2.detach(view2)
    print("Setting Data 1 = 10")
    data1.data = 10
    print("Setting Data 2 = 15")
    data2.data = 15


if __name__ == '__main__':
    main()
