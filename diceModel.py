# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""

from random import randint

class Creator(object):    
    
    def factory(type):
        if type == "dice": 
            return dice()        
        assert 0, "I can't create " + type + " object"
    
    factory = staticmethod(factory)

class dice():
    faces = 6
    def roll(self, faces):
        return randint(1,faces)
        