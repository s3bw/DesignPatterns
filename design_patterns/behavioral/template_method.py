"""
Template Method
===============

(Page. 311)

Intent
------
Define the skeleton of an algorithm in an operation, deferring some
steps to subclasses. Template Method lets subclasses redefine certain
steps of an algorithm without changing the algorithm's structure.

Motivation
----------
A template method defines an algorithm in terms of abstract operations
that subclasses override to provide concrete behavior.

By defining some of the steps of an algorithm using abstract
operations, the template method fixes their ordering, but it lets the
application and document subclasses vary those steps to suit their
needs.

Applicability
-------------
The Template Method pattern should be used
 - To implement the invariant parts of an algorithm once and leave it
   up to subclasses to implement the behavior that can vary.
 - When common behavior among subclasses should be factored and
   localized in a common class to avoid code duplication. This is a
   good example of "refactoring to generalize". You first identify the
   differences in the existing code and then separate the differences
   into new operations. Finally, you replace the differing code with a
   template method that calls one of these new operations.
 - To control subclasses extensions. You can define a template method
   that calls "hook" operations at specific points, thereby permitting
   extensions only at those points.

Consequences
------------
1. Template methods lead to an inverted control structure.
"""

# Defines the skeleton of an algorithm, deferring steps to subclasses.


ingredients = "spam eggs apple"
line = '-' * 10


# Skeletons
def iter_elements(getter, action):
    """Template skeleton that iterates items"""
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter, action):
    """Template skeleton that iterates items in reverse order"""
    for element in getter()[::-1]:
        action(element)
        print(line)


# Getters
def get_list():
    return ingredients.split()


def get_lists():
    return [list(x) for x in ingredients.split()]


# Actions
def print_item(item):
    print(item)


def reverse_item(item):
    print(item[::-1])


def make_template(skeleton, getter, action):
    """Instantiate a template method with getter and action"""
    def template():
        skeleton(getter, action)
    return template

# Create our template functions
templates = [make_template(s, g, a)
             for g in (get_list, get_lists)
             for a in (print_item, reverse_item)
             for s in (iter_elements, rev_elements)]


for template in templates:
    template()
