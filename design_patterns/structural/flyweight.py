"""
Flyweight
=========

(Page. 189)

Intent
------
Use sharing to support large numbers of fine-grained objects efficiently.

Motivation
----------
Some applications could benefit from using objects throughout their design, but
a naive implementation would be prohibitively expensive.

The Flyweight pattern describes how to share objects to allow their use at fine
granularities without prohibitive cost.

A flyweight is a shared object that can be used in multiple contexts
simultaneously. The flyweight acts as an independent object in each context-it's
indistinguishable from an instance of the object that's not shared. Flyweights
cannot make assumptions about the context in which they operate. The key
concept here is the distinction between *intrinsic* and *extrinsic* state.
Intrinsic state is stored in the flyweight; it consists of information that's
independent of the flyweight's context, thereby making it shareable.
Extrinsic state depends on and varies with the flyweight's context and therefore
can't be shared. Client objects are responsible for passing extrinsic state to
the flyweight when it needs it.

Flyweights model concepts or entities that are normally too plentiful to
represent with objects.

Applicability
-------------
The Flyweight pattern's effectiveness depends heavily on how and where it's
used. Apply the Flyweight pattern when _all_ the following are true:
 - An application uses a large number of objects.
 - Storage costs are high because of the sheer quantity of objects.
 - Most object state can be made extrinsic.
 - Many groups of object may be replaced by relatively few shared objects
   once extrinsic state is removed.
 - The application doesn't depend on object identity. Since flyweight objects
   maybe shared, identity tests will return true for conceptually distinct
   objects.

Consequences
------------
1. The reduction in the total number of instances that comes from sharing.
2. The amount of intrinsic state per object.
3. Whether extrinsic state is computed or stored.
"""

# Minimizes memory usage by sharing data with other similar objects.

import weakref


class FlyweightMeta(type):

    def __new__(mcs, name, parents, dct):
        """
        Set up object pool

        :param name:
            class name
        :param parents:
            class parents
        :param dict dct:
            includes class attributes, class methods, static methods, etc
        :return:
            new class
        """
        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        Serialize input parameters to a key.
        Simple implementation is just to serialize it as a string
        """
        args_list = list(map(str, args))
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if instance is None:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance


class Card(object):
    """ The object pool. Has builtin reference counting"""
    _CardPool = weakref.WeakValueDictionary()

    """Flyweight implementation. If the object exists in the
    pool just return it (instead of creating a new one)"""
    def __name__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __init__(self, value, suit):
        self.value, self.suit = value, suit

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


def with_metaclass(meta, *bases):
    """ Provide python cross-version metaclass compatibility. """
    return meta("NewBase", bases, {})


class Card2(with_metaclass(FlyweightMeta)):
    def __init__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    c1 = Card('9', 'h')
    c2 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2, c1 is c2)
    print(id(c1), id(c2))

    c1.temp = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))
    c1 = c2 = c3 = None
    c3 = Card('9', 'h')
    print(hasattr(c3, 'temp'))

    # With meta class
    instances_pool = getattr(Card2, 'pool')
    cm1 = Card2('10', 'h', a=1)
    cm2 = Card2('10', 'h', a=1)
    cm3 = Card2('10', 'h', a=2)

    assert (cm1 == cm2) != cm3
    assert (cm1 is cm2) is not cm3
    assert len(instances_pool) == 2

