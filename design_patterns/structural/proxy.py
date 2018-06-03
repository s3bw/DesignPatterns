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


class SalesManager:
    def talk(self):
        print("Sales Manager is ready to talk")


class Proxy:
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def talk(self):
        print("Proxy checking for Sales Manager availability")
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(0.1)
            self.sales.talk()
        else:
            time.sleep(0.1)
            print("Sales Manager is busy")


if __name__ == '__main__':
    p = Proxy()
    p.talk()
    p.busy = 'Yes'
    p.talk()
