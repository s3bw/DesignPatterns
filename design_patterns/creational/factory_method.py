"""
Factory Method
==============

(Page. 103)

Intent
------
Define an interface for creating an object, but let subclasses decide
which class to instantiate. Factory Method lets a class defer instantiation
to subclasses.

Motivation
----------
Frameworks use abstract classes to define and maintain relationships between
objects. A framework is often responsible for creating these objects as well.

Consider a framework with two key abstraction classes Application and
Document. The particular Document subclass to instantiate is application-
specific, thus the Application class can't predict the subclass of
Document to instantiate. The Application only knows _when_ a new document
should be created, not _what kind_ of Document to create.

This creates a dilemma: The framework must instantiate classes, but it only
knows about abstract classes, which it cannot instantiate.

The Factory Method pattern offers a solution. It encapsulates the knowledge
of which Document subclass to create and move this knowledge out of the
framework.

Application subclasses redefine an abstract CreateDocument operation on
Application to return the appropriate Document subclass. Once an Application
subclass is instantiated, it can the instantiate application-specific
Documents without knowing their class. We call CreateDocument a
**factory method** because it's responsible for "manufacturing" an object.

Applicability
-------------
Use the Factory Method pattern when
 - A class can't anticipate the class of objects it must create
 - A class wants its subclasses to specify the objects it creates
 - Classes delegate responsibility to one of several helper subclasses,
   and you want to localize the knowledge of which helper subclass is the
   delegate.

Consequences
------------
1. Provides hooks for subclasses
2. Connects parallel class hierarchies
3. Language-specific variants and issues.
4. Using templates to avoid subclassing
5. Naming conventions
"""


class AttackMethod:

    attack = dict(weak="scratched", normal="hit", strong="struck")

    def get(self, strength):
        return self.attack.get(strength)

    def damage(self, base_damage, weapon_type):
        if weapon_type == "rare":
            return base_damage * 2
        return base_damage


class Monster:

    def __init__(self, name, strength, weapon_type):
        self.name = name
        self.strength = strength
        self.weapon_type = weapon_type

    def attack(self, damage):
        attack = AttackMethod()
        attack_type = attack.get(self.strength)
        damage = attack.damage(damage, self.weapon_type)
        return "{} {} for {} damage.".format(self.name, attack_type, damage)


weak_monster = Monster("Goblin", "weak", weapon_type="rare")
print(weak_monster.attack(2))

strong_monster = Monster("Dragon", "strong", weapon_type="common")
print(strong_monster.attack(5))

