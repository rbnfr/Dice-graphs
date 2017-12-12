# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""

from random import randint

class dice(object):
    faces = ""
    def __init__(self, faces = None):
        if faces == None:
            self.faces = 6

    def roll(self):
        return randint(1, self.faces)

    def doRolls(self, dice_list, rolls):
        points_list = []
        for i in range(rolls):
            points = 0
            for dice in dice_list.values():
                points += randint(1, dice)
            points_list.append(points)
        return points_list