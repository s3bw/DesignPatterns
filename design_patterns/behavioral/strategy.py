"""
Strategy
========

(Page. 301)

Intent
------
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.

Motivation
----------
Clients that include the algorithms get more complex if they include
the algorithm code. This makes clients bigger and harder to maintain,
especially if they support multiple algorithms.

Different algorithms will be appropriate at different times. We don't
want to support multiple algorithms if we don't use them all.

It's difficult to add new algorithms and vary existing ones when it's
an integral part of a client.

We can avoid these problems by defining a class that encapsulates
different algorithms. An algorithm that's encapsulated in this way is
called a strategy.

Applicability
-------------
Use the strategy pattern when
 - Many related classes differ only in their behavior. Strategies
   provide a way to configure a class with one of many behaviours.
 - You need different variants of an algorithm. For example, you might
   define algorithms reflecting different space/time trade-offs.
   Strategies can be used when these variants are implemented as a
   class hierarchy of algorithms.
 - An algorithm uses data that clients shouldn't know about. Use the
   Strategy pattern to avoid exposing complex, algorithm-specific data
   structures.
 - A class defines many behaviors, and these appear as multiple
   conditional statements in its operations. Instead of many
   conditionals, move related conditional branches into their own
   Strategy class.

Consequences
------------
1. Families of related algorithms.
2. An alternative to subclassing.
3. Strategies eliminate conditional statements.
4. A choice of implementations.
5. Clients must be aware of different Strategies.
6. Communication overhead between Strategy and Context.
7. Increased number of objects.
"""

# Enables selecting an algorithm at runtime.


import types


class StrategyExample:

    def __init__(self, func=None):
        self.name = 'Strategy Example 0'
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if __name__ == '__main__':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()

