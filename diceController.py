# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""
import diceModel as dice

from random import randint

class dice:    
    
    def __init__(self, faces=6):
        self.faces = faces
        
    def roll(self, faces):
        dice = dice(faces)
        return dice.roll()
        