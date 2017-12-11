# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""

from random import randint

class histogram(object):
    hello = "hello"
    def __init__(self):
        self.hello = "Hello"              

    def maxPoints(self, dice_list):
        index = 0
        max_points = 0
        for faces in dice_list.values():
            if faces < 4:
                print("Invalid faces at dice " + str(index) + ", are you a fucking retard?")

            self.index+=1
            max_points += faces
        
        return max_points
        