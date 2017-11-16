# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""
import diceModel

from random import randint

class dice:    
    
    def __init__(self, faces):
        self.faces = faces
        
    def roll(self, faces):
        dice = diceModel(faces)
        return dice.roll()
        