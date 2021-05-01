# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""

from random import randint
from dataclasses import dataclass

@dataclass(init = True)
class dice:
    faces: int = 6

    def roll(self) -> int:
        return randint(1, self.faces)

    def doRolls(self, dice_list:list, rolls:int) -> list:
        points_list = []
        for i in range(rolls):
            points = 0 
            for dice in dice_list.values():
                points += randint(1, dice)
            points_list.append(points)
        return points_list

    def storeFrequency (self, possible_points, points_list):
        points_freq = {}
        for i in possible_points:
            points_freq[i] = points_list.count(i)
        return points_freq
        