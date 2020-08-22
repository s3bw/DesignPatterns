# Design Patterns

This repo is intended to be used as practice for implementing patterns of design as a means of study.

 - **For theory see:** Design Patterns: Elements of Reusable Object-Oriented Software.
 - **For examples see:** [faif/python-patterns](https://github.com/faif/python-patterns)
 - **For Python see:** [python-patterns.guide](https://python-patterns.guide/)

## Design Principles:

 - Program to an interface, not an implementation
 - Favour object composition over class inheritance.

## Python Patterns Guide

### Summary

An extension to the original gang-of-four design patterns. Some of these are unique
to the python language.

### See following implementations:

 - [Pre-bound Methods](design_patterns/python/prebound_methods.py)
 - [Sentinel Objects](design_patterns/python/sentinel_object.py)

## Creational Patterns

(Chapter 3, page. 77)

### Summary

Creational design patterns abstract the instantiation process. A class creational pattern uses inheritance to vary the class that's instantiated, whereas an object creational pattern will delegate instantiation to another object.
These shift emphasis away from hard-coding a fixed set of behaviours toward defining a smaller set of fundamental behaviours that can be composed into any number of more complex one. This means creating objects with particular behaviours requires more than simply instantiating a class.

There are two recurring themes in these patterns:
 - They all encapsulate knowledge about which concrete classes the system uses.
 - They hide how instances of these classes are created and put together.

All we know about the object is their interfaces as defined by abstract classes. Consequently they give you a lot of flexibility in _what_ gets created, _who_ creates it, _how_ it gets created, and _when_. They let you configure a system with "product" objects that vary widely in structure and functionality.

Sometimes creational patterns are competitors, at other times they are complementary.

### See following implementations:

 - [Abstract Factory](design_patterns/creational/abstract_factory.py)
 - [Builder](design_patterns/creational/builder.py)
 - [Factory Method](design_patterns/creational/factory_method.py)
 - [Prototype](design_patterns/creational/prototype.py)
 - [Singleton](design_patterns/creational/singleton.py)

## Structural Patterns

(Chapter 4, page. 133)

### Summary

Structural patterns are concerned with how classes and objects are composed to form larger structures. Structural class patterns use inheritance to compose interfaces or implementations.
Rather than composing interfaces or implementations, structural object patterns describe ways to compose objects to realize new functionality. The added flexibility of object composition comes from the ability to change the composition at run-time, which is impossible with static class composition.

Many structural patterns are related to some degree.

### See following implementations:

 - [Adapter](design_patterns/structural/adapter.py)
 - [Bridge](design_patterns/structural/bridge.py)
 - [Composite](design_patterns/structural/composite.py)
 - [Decorator](design_patterns/structural/decorator.py)
 - [Facade](design_patterns/structural/facade.py)
 - [Flyweight](design_patterns/structural/flyweight.py)
 - [Proxy](design_patterns/structural/proxy.py)

## Behavioral Patterns

(Chapter 5, page. 215)

### Summary

Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects. Behavioral patterns describe not just patterns of objects or classes but also the patterns of communication between them. These patterns characterize complex control flow that's difficult to follow at run-time. They shift your focus away from flow of control to let you concentrate just on the way objects are interconnected.

Behavioral class patterns use inheritance to distribute behaviour between classes.

Behavioral object patterns use object composition rather than inheritance.

Other behavioral object patterns are concerned with encapsulating behavior in an object and delegating requests to it.

### See following implementations:

 - [Chain Of Responsibility](design_patterns/behavioral/chain_of_responsibility.py)
 - [Command](design_patterns/behavioral/command.py)
 - [Interpreter](design_patterns/behavioral/interpreter.py)
 - [Iterator](design_patterns/behavioral/iterator.py) Additional: [Tree Iteration](design_patterns/behavioral/tree_iterator.py)
 - [Mediator](design_patterns/behavioral/mediator.py)
 - [Memento](design_patterns/behavioral/memento.py)
 - [Observer](design_patterns/behavioral/observer.py)
 - [State](design_patterns/behavioral/state.py)
 - [Strategy](design_patterns/behavioral/strategy.py)
 - [Template Method](design_patterns/behavioral/template_method.py)
 - [Visitor](design_patterns/behavioral/visitor.py)
