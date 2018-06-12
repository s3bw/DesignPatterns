"""
State
=====

(Page. 291)

Intent
------
Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.

Motivation
----------
A TCPConnection object can be in one of several different states:
Established, Listening, Closed. When a TCPConnection object receives
requests from other objects, it responds differently depending on its
current state. For example the effect of an Open request depends on
whether the connection is in its Closed state or its Established state.
The State pattern describes how TCPConnection can exhibit different
behaviour in each state.

The key idea in this pattern is to introduce an abstract class called
TCPState to represent the states of the network connection. The TCPState
class declares an interface common to all classes that represent
different operational states. Subclasses of TCPState implement state-
specific behaviour. For example, the class TCPEstablished and TCPClosed
implement behaviour particular to the Established and Closed states of
TCPConnection.

The class TCPConnection delegates all state-specific requests to this
state object. TCPConnection uses its TCPState subclass instance to
perform operations particular to the state of the connection.

Whenever the connection changes state, the TCPConnection object changes
the state object it uses. When the connection goes from established to
closed, for example, TCPConnection will replace its TCPEstablished
instance with a TCPClosed instance.

Applicability
-------------
Use the State pattern in either of the following cases:
 - An object's behaviour depends on its state, and it must change its
   behaviour at run-time depending on that state.
 - Operations have large, multipart conditional statements that depend
   on the object's state. This state is usually represented by one or
   more enumerated constants. Often, several operations will contain
   this same conditional structure. The State pattern puts each branch
   of the conditional in a separate class. This lets you treat the
   object's state as an object in its own right that can vary
   independently from other objects.

Consequences
------------
1. It localizes state-specific behaviour and partitions behaviour for
   different states.
2. It makes state transitions explicit.
3. State objects can be shared.
"""


class AiState:
    """Base state. This is to share functionality."""

    def status(self):
        """Mention the current status"""
        print("{} is {}".format(self.obj.name, self._status))

    def distance(self, d):
        raise NotImplementedError

    def cast_spell(self, spell):
        if hasattr(self, spell):
            method = getattr(self, spell)
            method()
            print("Effected by the spell")
        else:
            print("Has no effect")


class SleepingState(AiState):

    def __init__(self, obj):
        self.obj = obj
        self._status= "sleeping"

    def distance(self, x):
        if x <= 5:
            self.wake_up()

    def wake_up(self):
        print("{} Woke up!".format(self.obj.name))
        self.obj.state = self.obj.grumpy_ai


class GrumpyState(AiState):

    def __init__(self, obj):
        self.obj = obj
        self._status = "grumpy"

    def distance(self, x):
        if x > 5:
            self.calm_down()

    def calm_down(self):
        self.obj.state = self.obj.neutral_ai


class NeutralState(AiState):

    def __init__(self, obj):
        self.obj = obj
        self._status = "neutral"

    def distance(self, x):
        if x <= 5:
            self.obj.state = self.obj.grumpy_ai
        else:
            print("{} is at a good distance".format(self.obj.name))

    def cast_asleep(self):
        self.obj.state = self.obj.sleeping_ai


class Monster:

    """A monster that can be in three states"""

    def __init__(self, name):
        self.name = name

        self.grumpy_ai = GrumpyState(self)
        self.sleeping_ai = SleepingState(self)
        self.neutral_ai = NeutralState(self)

        self.state = self.sleeping_ai

    def use_turn(self, d):
        print("Distance to {}: {}".format(self.name, d))
        self.state.distance(d)
        self.state.status()

    def casted(self, spell):
        print(spell, "spell")
        self.state.cast_spell(spell)


if __name__ == '__main__':
    mewlip = Monster("Mewlip")

    mewlip.use_turn(7)
    print("")

    mewlip.casted('cast_asleep')
    print("")
    for n in reversed(range(5, 7)):
        print("Moving closer")
        mewlip.use_turn(n)
        print("")

    mewlip.casted('cast_asleep')
    print("")

    for n in range(5, 7):
        print("Moving away")
        mewlip.use_turn(n)
        print("")
    mewlip.casted('cast_asleep')
    print("")

    mewlip.use_turn(7)
