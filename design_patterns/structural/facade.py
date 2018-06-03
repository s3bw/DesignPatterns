"""
Facade
======

(Page. 179)

Intent
------
Provide a unified interface to a set of interfaces in a subsystem. Facade
defines a higher-level interface that makes the subsystem easier to use.

Motivation
----------
Structuring a system into subsystems helps reduce complexity. A common design
goal is to minimize the communication and dependencies between subsystems.
One way to achieve this goal is to introduce a facade object that provides a
single, simplified interface to the more general facilities of a subsystem.

Applicability
-------------
Use the Facade pattern when
 - You want to provide a simple interface to a complex subsystem. Subsystems
   often get more complex as they evolve. Most patterns, when applied, result
   in more and smaller classes. This makes the subsystem more reusable and
   easier to customize, but it also becomes harder to use for clients that
   don't need to customize it. A facade can provide a simple default view of
   the subsystem that is good enough for most clients. Only clients needing
   more customizability will need to look beyond the facade.
 - There are many dependencies between clients and the implementation classes
   of an abstraction. Introduce a facade to decouple the subsystem from clients
   and other subsystems, thereby promoting subsystem independence and
   portability.
 - You want to layer your subsystems. Use a facade to define an entry point
   to each subsystem level. If subsystems are dependant, the you can simplify
   the dependencies between them by making them communicate with each other
   solely through their facades.

Consequences
------------
1. It shields clients from subsystem components
2. It promotes weak coupling between the subsystem and its clients.
3. It doesn't prevent applications from using subsystem classes if they need to.
"""

# The Facade pattern is a way to provide a simpler unified interface to a more
# complex system.

import time


SLEEP = 0.1


# Complex Parts
class TC1:
    def run(self):
        print("###### In Test 1 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test finished\n")

class TC2:
    def run(self):
        print("###### In Test 2 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test finished\n")

class TC3:
    def run(self):
        print("###### In Test 3 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test finished\n")


# Facade - this is just a simplified interface for the subsystem.
class TestRunner:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]


# Client
if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()
