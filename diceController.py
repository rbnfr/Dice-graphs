# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""
from diceModel import dice

def roll(faces):
    new_dice = dice(faces)
    return new_dice.roll()

def doRolls(dice_list, rolls):
    new_dice = dice(6)
    return dice.doRolls(dice_list, rolls)
