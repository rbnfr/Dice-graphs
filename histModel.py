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
            if faces < 4 or faces != int(faces):
                print("Invalid faces at dice " + str(index + 1) + ", are you a fucking retard?")
                if (faces).is_integer() is False:
                    print("Decimal faces? Are you fucking kidding me?")
                break
            elif faces >= 100:
                print("\"Dice\"",str(index+1),"is not a dice, is a fucking sphere.")

            index+=1
            max_points += faces
        
        return max_points
        
