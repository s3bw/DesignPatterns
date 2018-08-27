"""
Visitor
=======

(Page. 317)

Intent
------
Represent an operation to be performed on the elements of an object
structure. Visitor lets you define a new operation without changing the
classes of the elements on which it operates.

Motivation
----------
Most of these operations will need to treat nodes that represent
assignment statements differently from nodes that represent variables
or arithmetic expressions. Hence there will be one class for assignment
statements, another for variable accesses, another for arithmetic
expressions, and so on.

The problem here is that distributing all these operations across the
various node classes leads to a system that's hard to understand,
maintain, and change. It will be confusing to have type-checking code
mixed with pretty-printing code or flow analysis code. Moreover, adding
a new operation usually requires recompiling all of these classes. It
would be better, if each new operation could be added separately, and
the node classes were independent of the operations that apply to them.

We can have both by packaging related operations from each class in a
separate object, called a *visitor*, and passing it to elements of the
abstract syntax tree as it's traversed. When an element "accept" the
visitor, it sends a request to the visitor that encodes the element's
class. It also includes the element as an argument. The visitor will
then execute the operation for that element- the operation that used to
be in the class of the element.

To make visitors work for more than just type-checking, we need an
abstract parent class NodeVisitor for all visitors of an abstract
syntax tree. NodeVisitor must declare an operation for each node class.

The Visitor pattern encapsulates the operations for each compilation
phase in a Visitor associated with that phase.

With the Visitor pattern, you define two class hierarchies: one for the
elements being operated on (the Node hierarchy) and one for the
visitors that define operations on the elements (the NodeVisitor
hierarchy). You create a new operation by adding a new subclass to the
visitor class hierarchy. As long as we don't have to add new Node
subclasses we can add new functionality simply by defining new
NodeVisitor subclasses.

Applicability
-------------
Use the Visitor pattern when
 - An object structure contains many classes of objects with differing
   interfaces, and you want to perform operations on these objects that
   depend on their concrete classes.
 - Many distinct and unrelated operations need to be performed on
   objects in an object structure, and you want to avoid "polluting"
   their classes with these operations. Visitor lets you keep related
   operations together by defining them in one operations in just those
   applications that need them
 - The classes defining the object structure rarely change, but you
   often want to define new operations over the structure. Changing the
   object structure classes requires redefining the interface to all
   visitors, which is potentially costly. If the object structure
   classes change often, then it's probably better to define the
   operations in those classes.

Consequences
------------
1. Visitor makes adding new operations easy.
2. A visitor gathers related operations and separates unrelated ones.
3. Adding new ConcreteElement classes is hard.
4. Visiting across class hierarchies.
5. Accumulating state.
6. Breaking encapsulation.
"""

# Separates an algorithm from an object structure on which it operates.
# https://stackoverflow.com/a/255300/3407256

# "it’s a way to design hierarchies so that new virtual-acting
# functions can be added without changing the hierarchies."
# - Scott Meyers


class Node:
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor:

    def visit(self, node, *args, **kwargs):
        meth = None

        # Python Method Resolution Order
        for cls in node.__class__.__mro__:
            meth_name = 'visit_' + cls.__name__
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print('visit_B ' + node.__class__.__name__)


def main():
    a = A()
    b = B()
    c = C()
    visitor = Visitor()
    visitor.visit(a)
    visitor.visit(b)
    visitor.visit(c)


if __name__ == '__main__':
    main()
