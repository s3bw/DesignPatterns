"""
Composite
=========

(Page. 157)

Intent
------
Compose objects into tree structures to represent part-whole hierarchies.
Composite lets clients treat individual objects and compositions of
objects uniformly.

Motivation
----------
The user can group components to form large components, which in turn
can be grouped to form still larger components. Having to distinguish
these objects makes the application more complex. The Composite
pattern describes how to use recursive composition so that clients
don't have to make this distinction.

The key to the Composite pattern is an abstract class that represents
both primitives and their containers.

Applicability
-------------
Use the Composite pattern when
 - You want to represent part-whole hierarchies of objects.
 - You want clients to be able to ignore the difference between
   compositions of objects and individual objects. Clients will treat
   all objects in the composite structure uniformly.

Consequences
------------
1. Defines class hierarchies consisting of primitive objects and
   composite objects.
2. Make the client simple.
3. Makes it easier to add new kinds of components.
4. Can make your design overly general.
"""

# The composite pattern describes a group of objects that is treated
# the same way as a single instance of the same type of object.

class Graphic:
    def render(self):
        raise NotImplementedError("You should implement something.")


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == '__main__':
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)
    graphic2.add(ellipse4)

    graphic = CompositeGraphic()

    graphic.add(graphic1)
    graphic.add(graphic2)

    graphic.render()

