# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""
from histModel import histogram

def maxPoints(dice_list):
    hist = histogram()
    return hist.maxPoints(dice_list)

def minPoints(dice_list) -> int:
    return len(dice_list)