"""
Mediator
========

(Page. 263)

Intent
------
Define an object that encapsulates how a set of objects interact. Mediator
promotes loose coupling by keeping objects from referring to each other
explicitly, and it lets you vary their interaction independently.

Motivation
----------
Object-oriented design encourages the distribution of behavior among
objects. Such distribution can result in an object structure with many
connections between objects; in the worst case, every object ends up
knowing about every other.

Though partitioning a system into many objects generally enhances
reusability, proliferating interconnections tend to reduce it again.
Moreover, it can be difficult to change the system's behaviour in any
significant way, since behaviour is distributed among many objects.

You can avoid these problems by encapsulating collective behavior in
a separate mediator object. A mediator is responsible for controlling
and coordinating the interactions of a group of objects. The mediator
serves as an intermediary that keeps objects in the group from referring
to each other explicitly. The objects only know the mediator, thereby
reducing the number of interconnections.

Objects should not know about each other only the mediator should know
about the object. Thus this is in a way parallel functionality. Not really
an example of direct interaction. (see controller in MVC pattern)

E.g. if the user click here, make x do this, make y do that and make z do
something else.

Applicability
-------------
Use the Mediator pattern when.
 - A set of objects communicate in well-defined but complex ways. The
   resulting interdependencies are unstructured and difficult to
   understand.
 - Reusing an object is difficult because it refers to and communicates
   with many other objects.
 - A behaviour that's distributed between several classes should be
   customizable without a lot of subclassing.

Consequences
------------
1. It limits subclassing.
2. It decouples colleagues.
3. It simplifies object protocols.
4. It abstracts how objects cooperate.
5. It centralizes control.
"""

# Encapsulates how a set of objects interact.


import random
import time


class Player:

    def __init__(self, name):
        self.steps = 0
        self._name = name

    def turn(self):
        print("{} moved".format(self._name))


class Monster:

    def __init__(self, name):
        self._name = name

    def turn(self):
        print("The {} is sleeping.".format(self._name))


class GameMediator:

    def __init__(self):
        self.playing = True
        self.player = None
        self.opponents = []

    def set_player(self, player):
        self.player = player

    def add_opponent(self, opponent):
        self.opponents.append(opponent)

    def turn(self):
        self.player.turn()
        for opponent in self.opponents:
            opponent.turn()
        self.tickers()

    def tickers(self):
        self.player.steps += 1


def play():
    player = Player("Rogue")
    monster_1 = Monster("Slime Creature")
    monster_2 = Monster("Demon")

    game = GameMediator()
    game.set_player(player)
    game.add_opponent(monster_1)
    game.add_opponent(monster_2)

    for _ in range(3):
        game.turn()

    print("The {} moved {} times.".format(player._name, player.steps))


if __name__ == '__main__':
    play()
