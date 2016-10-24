#!/usr/bin/env python
# encoding: utf-8

"""
Prototype design pattern:
Application feature:need a lot of trace changes based on a basic prototype and get a new prototype.
Structural features: object replication mechanism[Shallow copy and Deep copy]
"""

from copy import copy, deepcopy


class test_obj:
    def __init__(self, id):
        self.id = id


class proto_type:
    def __init__(self, name, id):
        self.name = name
        self.obj = test_obj(id)

    def display(self):
        print self.name
        print self.obj.id

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if '__main__' == __name__:
    obj1 = proto_type('name1', 1)
    print "original obj1:"
    obj1.display()
    obj2 = obj1.clone()  # shallow copy.
    # because obj2 is a shallow copy,object
    #  not to be copied,lead to changes of a
    # new object affect the original value of
    # the old object
    print "original obj2:"
    obj2.display()
    obj3 = obj1.deep_clone()  # deep copy
    # because obj3 is a deep copy,it will not
    # affect the old object
    print "original obj3:"
    obj3.display()
    obj2.name = 'name2'
    obj2.obj.id = 2
    obj3.name = 'name3'
    obj3.obj.id = 3
    print "new obj1:"
    obj1.display()
    print "new obj2:"
    obj2.display()
    print "new obj3:"
    obj3.display()
    print obj1.__class__
    print obj2.__class__
    print obj3.__class__

