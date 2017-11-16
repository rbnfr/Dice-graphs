# -*- coding: utf-8 -*-
"""
Author: Ruben
"""
from random import randint
import matplotlib.pyplot as plt
import diceController as dice

points = ""
dices = 3
faces = 6
dice_list = [dice(faces) for i in range(1,dices+1)]


for i in range(1,dices+1):
    dice_list.append(dice(faces))    

possible_points = range(2,faces)
points_list = []

for i in range(10000):
    scramble1 = dice.roll(faces)
    scramble2 = dice.roll(faces)
    points = scramble1 + scramble2
    points_list.append(points)
    
#print (*points_list, sep="-")

fin = [ possible_points.index(i) for i in points_list]
plt.hist(fin, bins=range(12), align="left", color="orange")
plt.xticks(range(12), possible_points)
#
plt.xlabel("Results")
plt.ylabel("Frequency")
plt.show()


