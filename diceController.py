# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""
from random import randint
import diceModel

class dice():      
    faces = 6
    def createDice(faces):
        dice = diceModel.Creator.factory('dice')(faces)
        return dice.roll()
    
        